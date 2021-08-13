import random
from members.models import Member
from programs.models import Program
import json

f = open('seeder/members.json',)

data = json.load(f)

list = ['D01EBBC7A7', '6163CA34BE']

for i in data:
    try:
        program = Program.objects.get(id=list[random.randint(0, 1)])
        member = Member.objects.create(program=program, username=i['email'])
        print(member.id)
    except Program.DoesNotExist:
        pass
