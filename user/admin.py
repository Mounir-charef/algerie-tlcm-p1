from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.


class Admin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'dot', 'email', 'first_name', 'last_name'),
            },
        ),
    )


admin.site.register(models.User, Admin)
admin.site.register(models.Dot)
admin.site.register(models.Cmp)
admin.site.register(models.File)
admin.site.register(models.Information)
admin.site.register(models.InformationDot)
