from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@example.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("123qwe")
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Admin user created: {user.email}"))
