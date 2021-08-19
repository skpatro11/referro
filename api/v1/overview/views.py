from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from programs.models import Program


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
    print(context)
    return Response(data=context)
