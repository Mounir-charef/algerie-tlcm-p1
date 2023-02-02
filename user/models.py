from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

class Dot(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


def base_dot():
    return Dot.objects.get(name='ALGER CENTRE')


class User(AbstractUser):
    # class Role(models.TextChoices):
    #     CENTRAL = "ADMIN", "Admin"
    #     UTILISATEUR = "USER", "User"

    # base_role = Role.CENTRAL
    # role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    dot = models.ForeignKey(
        Dot,
        on_delete=models.CASCADE,
        blank=False,
        default=base_dot
    )

    def __str__(self):
        return f" {self.username} : {self.dot} "


class Cmp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    dot = models.ForeignKey(Dot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class File(models.Model):
    file_name = models.FileField(upload_to='static')

    def __str__(self):
        return self.file_name.name.split('/')[1]

# class UtilisateurManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(role=User.Role.UTILISATEUR)
#
#
# class Utilisateur(User):
#     base_role = User.Role.UTILISATEUR
#
#     utilisateur = UtilisateurManager()
#
#     class Meta:
#         proxy = True
#
#
# class UtilisateurProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     utilisateur_id = models.IntegerField(null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# @receiver(post_save, sender=Utilisateur)
# def create_user_profil(sender, instance, created, **kwargs):
#     if created and instance.role == "USER":
#         UtilisateurProfile.objects.create(user=instance)
