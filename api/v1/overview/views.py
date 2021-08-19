from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from programs.models import Program
from django.utils import timezone
from datetime import timedelta
from api.v1.exceptions import ProgramNotFound


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def programs_detail_count(request):
    programs = request.user.programs.all()
    context = {}
    for p in programs:
        context[p.name] = {
            'members': p.get_member_count(),
            'orders': p.get_order_count()
        }
    return Response(data=context)


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def program_members_stats(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
        if program not in request.user.programs.all():
            return Response(data={'detail': 'Not assigned'}, status=status.HTTP_403_FORBIDDEN)
        members = program.members.all()
        context = {}
        for i in range(0, 30):
            date = timezone.now() - timedelta(days=i)
            # print(members.filter(created_at__day=date.day).count())
            context[str(date.day) + '/' + str(date.month)] = members.filter(created_at__day=date.day).count()
        return Response(data=context)
    except Program.DoesNotExist:
        raise  ProgramNotFound


@api_view(('GET',))
@permission_classes((IsAuthenticated,))
def program_orders_stats(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
        if program not in request.user.programs.all():
            return Response(data={'detail': 'Not assigned'}, status=status.HTTP_403_FORBIDDEN)
        orders = program.program_orders.all()
        context = {}
        for i in range(0, 30):
            date = timezone.now() - timedelta(days=i)
            # print(members.filter(created_at__day=date.day).count())
            context[str(date.day) + '/' + str(date.month)] = orders.filter(created_at__day=date.day).count()
        return Response(data=context)
    except Program.DoesNotExist:
        raise  ProgramNotFound