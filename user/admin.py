from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Utilisateur)
admin.site.register(models.UtilisateurProfile)
admin.site.register(models.Dot)
admin.site.register(models.Cmp)

