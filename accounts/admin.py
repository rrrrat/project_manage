from django.contrib import admin
from accounts.models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(UserRole)