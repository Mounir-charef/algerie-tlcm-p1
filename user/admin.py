from django.contrib import admin
from .models import User, Utilisateur, UtilisateurProfile
# Register your models here.

admin.site.register(User)
admin.site.register(Utilisateur)
admin.site.register(UtilisateurProfile)
