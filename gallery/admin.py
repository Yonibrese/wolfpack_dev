from django.contrib import admin
from . import models


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']


admin.site.register(models.Developer, DeveloperAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.Language, LanguageAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.Projects, ProjectAdmin)