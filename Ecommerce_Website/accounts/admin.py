from django.contrib import admin
from .models import (Profile, Address, Child)

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =('id', 'user', 'user_contact_number','user_sex', 'pancard_name','pancard_number','aadharcard_name', 'aadharcard_number',)

class AddressAdmin(admin.ModelAdmin):
    list_display =('id','user','name','mobile_no','pincode','locality','address','city','state','landmark','alternate_no')

class ChildAdmin(admin.ModelAdmin):
    list_display  = ('id','user','child_name','child_birth_date')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Child, ChildAdmin)