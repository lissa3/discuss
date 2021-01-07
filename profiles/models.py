from django.db import models
from utils.models import TimeStamp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from utils.broadcast_utils.base_utils import upload_img
from PIL import Image

User = get_user_model()

class Profile(TimeStamp):
    """ 
    unid instead for safer url;
    badge_bg (creat random bg-color by creating profile object)
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # primary_key=True,
        related_name= 'profile'
        )
    unid = models.CharField(max_length=6,blank=True)
    display_name = models.CharField(max_length=50,default="",blank=True)
    first_name = models.CharField(max_length=100,default="",blank=True)
    last_name = models.CharField(max_length=100,default="",blank=True)
    active = models.BooleanField(default=True)    
    image = models.ImageField(blank=True,null=True,upload_to=upload_img)
    linkedin_profile = models.CharField(max_length=100,default="",blank=True)
    website = models.CharField(max_length=100,default="",blank=True)
    badge_bg = models.CharField(max_length=30,default="",blank=True)

    def __str__(self):
        return f"{self.unid} == {self.user.email}"

    def get_absolute_url(self):
        return reverse('profiles:profile-info', kwargs={'profile_unid': self.unid})

    @property
    def get_avatar_url(self,*args,**kwargs):
        """ return path to profile image """
        if self.image:
            return f'/media/{self.image}'
        else:
            return '/static/img/avatar.png' 

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        # print('coming to save and re-sizing')
        if self.image: # and not kwargs.get('update_fields'):
            # print('you are uploading an image')
            image= Image.open(self.image.path) #?.path?
            (x,y) = image.size
            new_x = 320
            new_y = int(new_x*(y/x))
            resized_image = image.resize((new_x,new_y),Image.ANTIALIAS)
            resized_image.save(self.image.path) 
                
               
    @property
    def get_name(self): 
        if self.first_name and self.last_name:
            return '{} {}'.format(
                self.first_name.capitalize(),
                self.last_name.capitalize()) 
        elif self.display_name:
            return self.display_name.capitalize() 
        else:
            return self.user.username
            
    def get_ava_letter(self):
        return self.user.get_name[0]            
         



    



