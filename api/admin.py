from django.contrib import admin

from .models import ConstructionCompany, Building, Comment
# Register your models here.

admin.site.register([ConstructionCompany, Building, Comment])