from django.contrib import admin

from profile_api import models

# Register your models here.
### To enable django admin for our profile_api app
admin.site.register(models.UserProfile)