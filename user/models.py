from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class UtilisateurManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.UTILISATEUR)


class Utilisateur(User):
    base_role = User.Role.UTILISATEUR

    utilisateur = UtilisateurManager()

    class Meta:
        proxy = True


class UtilisateurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    utilisateur_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Utilisateur)
def create_user_profil(sender, instance, created, **kwargs):
    if created and instance.role == "USER":
        UtilisateurProfile.objects.create(user=instance)


class Dot(models.Model):
    name = models.CharField(max_length=50)


class Cmp(models.Model):
    name = models.CharField(max_length=50)
    dot = models.ForeignKey(Dot, on_delete=models.CASCADE)
