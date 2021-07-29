from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import studyUserForm, part_1Form, part_2Form, part_3Form
from .models import studyUser, Session, part_1, part_2, part_3
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# Sona ID Admin
class studyUserResource(resources.ModelResource):
    class Meta:
        model = studyUser
class studyUserAdmin (ImportExportModelAdmin):
    resource_class = studyUserResource
admin.site.register(studyUser, studyUserAdmin)

# Session ID Admin
class sessionResource(resources.ModelResource):
    class Meta:
        model = Session
class sessionAdmin(ImportExportModelAdmin):
    resource_class = sessionResource
admin.site.register(Session, sessionAdmin)
    
# part_1 Admin
class part_1Resource(resources.ModelResource):
    class Meta:
        model = part_1 
class part_1Admin(ImportExportModelAdmin):
    resource_class = part_1Resource
admin.site.register(part_1, part_1Admin)

# part_2 Admin
class part_2Resource(resources.ModelResource):
    class Meta:
        model = part_2 
class part_2Admin(ImportExportModelAdmin):
    resource_class = part_2Resource
admin.site.register(part_2, part_2Admin)

# part_3 Admin
class part_3Resource(resources.ModelResource):
    class Meta:
        model = part_3 
class part_3Admin(ImportExportModelAdmin):
    resource_class = part_3Resource
admin.site.register(part_3, part_3Admin)
