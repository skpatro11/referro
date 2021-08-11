import random
from members.models import Member
from programs.models import Program
from orders.models import Order


for i in range(0, 1000):
    member = Member.objects.all()[random.randint(0, 51)]
    claim_amount = member.program.incentive
    charge_amount = float(member.program.incentive) + 0.05 * float(member.program.incentive)
    # print(claim_amount, charge_amount)
    order = Order.objects.create(member=member, program=member.program, claim_amount=claim_amount, charge_amount=charge_amount)
    print(order.id)
