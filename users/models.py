from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager



class User(AbstractBaseUser,PermissionsMixin):
    """ super_name is only for superusers"""
    email = models.EmailField(_('email address'), unique=True,max_length=255)    
    super_name = models.CharField(max_length=124,default="",blank=True,)
    username = models.CharField(max_length=120,default="",blank=True)
    first_name = models.CharField(max_length=100,default="",blank=True)
    last_name = models.CharField(max_length=100,default="",blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS: to create superuser: list containing other fields than UUSERNAME_FIELD
    REQUIRED_FIELDS = ['super_name']   
    
    objects = CustomUserManager() 

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True 
        

    @property
    def get_name(self): 
        if self.profile.display_name:
            return self.profile.display_name.capitalize() 
        elif self.profile.first_name and self.profile.last_name:
            return '{} {}'.format(
                self.profile.first_name.capitalize(),
                self.profile.last_name.capitalize()) 
        else:
            return self.username

    def get_ava_letter(self):
        return self.get_name[0]  

    def get_full_name(self):
        # The user is identified by their email address
        if self.username:
            return self.username
        return self.email

     

    def get_short_name(self):
        # The user is identified by their email address
        if self.username:
            return self.username
        short_name = self.email.split('@')[0]
        return short_name     

    def __str__(self):
        return self.email


