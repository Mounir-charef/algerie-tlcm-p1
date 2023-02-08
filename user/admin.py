from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rangefilter.filters import DateRangeFilter


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


class CmpAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('dot', )


class DotAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', )


class InformationAdmin(admin.ModelAdmin):
    list_filter = (('date', DateRangeFilter), ('cmp', admin.RelatedFieldListFilter))
    date_hierarchy = 'date'


class InformationDotAdmin(admin.ModelAdmin):
    list_filter = (('date', DateRangeFilter), 'dot')
    date_hierarchy = 'date'


admin.site.site_header = 'Algérie Télécom panneau d\'administrateur'
admin.site.register(models.User, Admin)
admin.site.register(models.Dot, DotAdmin)
admin.site.register(models.Cmp, CmpAdmin)
admin.site.register(models.File)
admin.site.register(models.Information, InformationAdmin)
admin.site.register(models.InformationDot, InformationDotAdmin)
