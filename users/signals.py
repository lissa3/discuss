from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver
from utils.broadcast_utils.base_utils import make_unid,make_username,create_color
from profiles.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


# before profile get saved in db |==> create unid,displayname,random bg color for avatar
@receiver(pre_save,sender= User)
def add_username(sender,instance,**kwargs):
    if not instance.username:
        instance.username = make_username(instance)
     
