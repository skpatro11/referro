from authentication.models import User

user = User.objects.create(name='Admin', email='admin@example.com', password='12345')

user.is_admin = True
user.save()
