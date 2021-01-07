from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from users.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

# class ProfileAdmin(admin.ModelAdmin):
#     pass 


# New
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine,) 
    
    def get_inline_instance(self,request,obj=None):
        if not obj:
            return list()
        return super().get_inline_instance (request,obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# admin.site.register(Profile,ProfileAdmin)


