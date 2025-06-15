# your_app_name/management/commands/createsuperadmin.py
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

        if not all([username, email, password]):
            raise CommandError(
                "Missing one or more required environment variables for superuser creation: "
                "DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD."
            )

        try:
            # Attempt to get the user, or create it if it doesn't exist
            user, created = User.objects.get_or_create(username=username, defaults={'email': email})

            # If user was just created, set the password and make it a superuser
            if created:
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
            else:
                # If user already exists, update their email (if changed) and password
                if user.email != email:
                    user.email = email
                user.set_password(password) # <--- THIS IS THE LINE TO ADD/UNCOMMENT
                user.is_superuser = True # Ensure it's still superuser
                user.is_staff = True # Ensure it's still staff
                user.save()
                self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists. Password updated.')) # Change message
        except Exception as e:
            raise CommandError(f'Error creating/updating superuser "{username}": {e}')