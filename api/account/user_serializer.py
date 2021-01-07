from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSer
# from djoser.serializers import UserSerializer as DjoserUserSer
from .profile_serializer import ProfileSerializer
from rest_framework import serializers as ser

User = get_user_model()

# custom part for djoser module(see settings for built-in)
class UserCreateSerializer(DjoserUserCreateSer):        
   #print("inside UserCreate ser-er")
   class Meta(DjoserUserCreateSer.Meta):
        model = User
        fields=('id','email','password','first_name','last_name')

class UserProfileSerializer(DjoserUserCreateSer):
    """inside UserSerializer inherited from djoser"""
    profile = ProfileSerializer()
    class Meta(DjoserUserCreateSer.Meta):
        model = User
        fields=('id','email','first_name','last_name','profile')

      

