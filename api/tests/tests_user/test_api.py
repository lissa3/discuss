from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APITestCase
import json
from profiles.models import Profile
from api.account.user_serializer import UserProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializerTesCase(APITestCase):
    """return user info + profile attrs"""
    def setUp(self):        
        self.user1 = User.objects.create(email="zoo@mail.com")        
        self.profile = Profile.objects.filter(user_id=self.user1.id).last()

    def test_get_user_and_profile(self):      
        """ via custom view: get user attr AND profile info"""        
        self.client.force_authenticate(user=self.user1)         
        url = reverse('user-info') #,kwargs={"pk":self.user1.id})
        # print("url is",url)
        response = self.client.get(url)
        # serial_profile = UserSerializer(self.user1).data             
        self.assertEqual(response.status_code, status.HTTP_200_OK)              
        # self.assertEqual(response.data, serial_profile) 

        # {"id":1,"email":"tata@mail.com","profile":{"user_id":1,"display_name":"","first_name":"","last_name":"","website":"","linkedin_profile":"","image":null,"name":"tata"}}  

# TODO: check flow in auth  via djoser      