from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserModel(AbstractBaseUser):
    def get_username(self) -> str:
        return self.first_name + self.last_name

    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = get_username()


    