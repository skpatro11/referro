from members.models import Member
from programs.models import Program
from orders.models import Order
from django.utils import timezone
from datetime import timedelta
import random

for i in range(0, 1000):
    m = Member.objects.order_by('?').first()
    amount = random.randint(100, 300)
    order = Order.objects.create(member=m, program=m.program, charge_amount=amount, claim_amount=amount)

    order.created_at = timezone.now() - timedelta(days=random.randint(0, 30))
    order.save()

    print('Order created with order - ', order.id)