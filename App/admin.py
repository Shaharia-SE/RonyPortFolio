from django.contrib import admin

# Register your models here.
from .models import about
from .models import Info

admin.site.register(about)
admin.site.register(Info)
