from profiles.models import Profile
from api.account.profile_serializer import ProfileSerializer
from api.account.user_serializer import UserCreateSerializer
from django.shortcuts import get_object_or_404
# from django.core.exceptions import PermissionDenied 
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrIsStaff
from rest_framework import generics
from rest_framework.exceptions import APIException,PermissionDenied
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model() 


class UserInfoView(generics.RetrieveUpdateDestroyAPIView):
    """ info about auth user AND info of his profile (see ser-or)
    via adjusted user serial-er """
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()     
   
    def get_object(self):
        try:
            obj = get_object_or_404(
                self.queryset,
                id =self.request.user.id,
                )
            # print("user",obj)
            self.check_object_permissions(self.request, obj)
        except APIException:
            # print("no object found")
            raise PermissionDenied
            return     
        return obj


class ProfileRetrUpdateDestrView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrIsStaff,]
    queryset = Profile.objects.all() 
    
   
    def get_object(self):
        try:
            obj = get_object_or_404(
                self.queryset,
                user_id=self.kwargs.get('pk'),
                )
            self.check_object_permissions(self.request, obj)
        except APIException:
            print("no object found")
            raise PermissionDenied
            return      
            
        return obj






    
    