from django.contrib.auth.models import UserManager

class UserManager(UserManager):

    def create_user(self, email=None, **extra_fields):
        if not email:
            raise ValueError('Электронная почта не заполнена')