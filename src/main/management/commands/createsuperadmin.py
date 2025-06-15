import os 
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'create a superuser if one does not already exists, using environment variable.'
    
    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        
        if not all([username,email,password]):
            raise CommandError(
                "Missing one or more required environment variables for superuser creation: "
                "DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD."
            )
        
        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_superuser(username=username,email=email, password=password)
            except Exception as e:
                raise CommandError(f'Error creating superuser "{username}":{e}')
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists. Skipping creation'))