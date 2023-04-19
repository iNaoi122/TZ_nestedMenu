from django.contrib import admin
from .models import *


# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url')


admin.site.register(Branch)
admin.site.register(Menu)
