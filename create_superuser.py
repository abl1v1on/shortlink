from django.core.management import call_command
from django.contrib.auth import get_user_model


User = get_user_model()

if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'root@example.com', 'root')
