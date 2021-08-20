from members.models import Member
from programs.models import Program
from django.utils import timezone
from datetime import timedelta
import random
import json

f = open('seeder/data/members.json')

data = json.load(f)

# print(Program.objects.order_by('?').first())

for i in data:
    p = Program.objects.order_by('?').first()
    member = Member.objects.create(program=p, username=i['email'])
    
    member.created_at = timezone.now() - timedelta(days=random.randint(0, 30))
    member.save()

    print('Member is created')