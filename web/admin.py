from django.contrib import admin
from .models import Change_type, Change_content,User

# Register your models here.
admin.site.register(Change_type)
admin.site.register(Change_content)
admin.site.register(User)