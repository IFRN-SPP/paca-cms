from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email
