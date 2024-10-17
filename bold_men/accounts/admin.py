from django.contrib import admin
from .models import Profile, User, Individual, Client, Employee
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

User = get_user_model()

class UserAdminConfig(UserAdmin):

    """
    Represent a custom user admin configuration inherits from the UserAdmin
    """

    model = User
    search_fields = ('email','username',)
    list_filter = ('email','username', 'is_active','is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_staff',)
    fieldsets = (
            (None, {'fields': ('email', 'username')}),
            ('Permissions', {'fields':('is_staff', 'is_active', 'groups',)}),
            ('Personal', {'fields': ('full_name', 'bio',)}),
            )
    formfield_overrides = {
            User.bio: {'widget': Textarea(attrs={'rows':10, 'col':40})}
            }

    # To change the arrangement when adding to a new user from the admin
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')
                }),
            )

    

# find . -type d -name "migrations" -exec rm -rf {} \;
# find . -type d -name "__pycache__" -exec rm -rf {} \;      

admin.site.register(User, UserAdminConfig)
admin.site.register(Individual)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Profile)
