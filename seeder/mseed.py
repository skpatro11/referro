import random
from members.models import Member
from programs.models import Program
import json

f = open('seeder/members.json',)

data = json.load(f)

list = ['D86791EE16', '7E0F97F3E3', '613AA568A0', '326FD8931D']

for i in data:
    try:
        program = Program.objects.get(id=list[random.randint(0, 3)])
        member = Member.objects.create(program=program, username=i['email'])
        print(member.id)
    except Program.DoesNotExist:
        pass
