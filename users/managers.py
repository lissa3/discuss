from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """ create user with  unique email as identifier"""
    def create_user(self,email,password=None,**kwargs): 
        #print("got kwargs:",kwargs)  #{'username': 'lissa3'} 
        # # ? case when user auth via social net with username but 
        # wants to keep email private?
        # # if (not email) and kwargs['username]: |=> email ==> "socal@mail.com"        
        if not email:
            raise ValueError(_('The email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)   
        if kwargs.get('username'):
            user.username = kwargs.get('username')
        user.is_active = False         
        user.set_password(password)        
        user.save(using=self._db) 
        return user

    def create_superuser(self,email,super_name,password=None):
        """ create superuser based on unique email as identifier"""       
        if not super_name or super_name=="":
            raise ValueError(_('The super_name is required and should be unique'))
        user = self.create_user(email,password)
        user.super_name = super_name
        user.is_superuser = True
        user.is_staff =True
        user.is_admin = True
        user.is_active =True   
        user.save(using=self._db)     
        return user

    # has_delete_permission    

        
