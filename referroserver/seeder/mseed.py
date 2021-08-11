import random
from members.models import Member
from programs.models import Program
import json

f = open('seeder/members.json',)

data = json.load(f)

list = ['F23478EAEC', '64630D2D87', '44BB9EDF96', '1503C375C1']

for i in data:
    try:
        program = Program.objects.get(id=list[random.randint(0, 3)])
        member = Member.objects.create(program=program, username=i['email'])
        print(member.id)
    except Program.DoesNotExist:
        pass
