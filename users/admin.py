from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    # form = None
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active', )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('phone_number', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('phone_number', )}),
    )
    
    
admin.site.register(CustomUser, CustomUserAdmin)
