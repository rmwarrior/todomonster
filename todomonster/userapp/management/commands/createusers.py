from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        print('Удаляем всех пользователей')
        User.objects.all().delete()
        user_count = options['count']
        print('Создаем суперпользователя')
        User.objects.create_superuser('admin', 'admin@mail.ru', 'admin',
                                      first_name='admin', last_name='admin', birthday_year=1977)
        print('Создаем тестовых пользователей')
        for i in range(user_count):
            User.objects.create_user(f'user{i}', f'user{i}@mail.ru', f'user{i}',
                                     first_name=f'user{i}', last_name=f'user{i}', birthday_year=2000)

        print('Ok')
