from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# Create your models here.

class Dot(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    total_raccordement_client = models.IntegerField(default=0)
    auto = models.IntegerField(default=0)
    binome = models.IntegerField(default=0)
    dhdb = models.IntegerField(default=0)
    ftth = models.IntegerField(default=0)
    sans_specialite = models.IntegerField(default=0)
    q_o_s = models.IntegerField(default=0)
    norme = models.IntegerField(default=0)
    objectif = models.IntegerField(default=0)

    def __str__(self):
        return self.name


def base_dot():
    return Dot.objects.get(name='ALGER CENTRE')


class User(AbstractUser):
    dot = models.ForeignKey(
        Dot,
        on_delete=models.CASCADE,
        blank=False,
        default=base_dot
    )

    def __str__(self):
        return f" {self.username} : {self.dot}"


class Cmp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    dot = models.ForeignKey(Dot, on_delete=models.CASCADE)
    total_raccordement_client = models.IntegerField(default=0)
    auto = models.IntegerField(default=0)
    binome = models.IntegerField(default=0)
    dhdb = models.IntegerField(default=0)
    ftth = models.IntegerField(default=0)
    sans_specialite = models.IntegerField(default=0)
    q_o_s = models.IntegerField(default=0)
    norme = models.IntegerField(default=0)
    objectif = models.IntegerField(default=0)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Cmp)
def add_data_to_dot(sender, instance, created, **kwargs):
    temp = Dot.objects.get(id=instance.dot_id)
    temp.total_raccordement_client += instance.total_raccordement_client
    temp.auto += instance.auto
    temp.binome += instance.binome
    temp.dhdb += instance.dhdb
    temp.ftth += instance.ftth
    temp.sans_specialite += instance.sans_specialite
    temp.q_o_s += instance.q_o_s
    temp.norme += instance.norme
    temp.objectif += instance.objectif
    temp.save()


class File(models.Model):
    file_name = models.FileField(upload_to='static')

    def __str__(self):
        return self.file_name.name.split('/')[1]

