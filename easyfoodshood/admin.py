from django.contrib import admin
from .models import Food

admin.site.register(Food)
admin.site.site_header = 'Easy Food Shood Administration'