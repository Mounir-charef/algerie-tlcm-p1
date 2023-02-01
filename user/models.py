from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        CENTRAL = "ADMIN", "Admin"
        UTILISATEUR = "USER", "User"

    base_role = Role.CENTRAL

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class Utilisateur(User):
    base_role = User.Role.UTILISATEUR

    class Meta:
        proxy = True

    def welcome(self):
        return "only for simple user"
