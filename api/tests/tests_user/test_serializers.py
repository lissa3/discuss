from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status

import json
from api.account.user_serializer import UserProfileSerializer
from api.account.profile_serializer import ProfileSerializer

from profiles.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializerTestCase(TestCase):
    """compare expected and received data after ser-on"""
    def setUp(self):        
        self.user = User.objects.create(email="zoo@mail.com") 
        self.profile = Profile.objects.last()        
        
    def test_user_serializer(self):      
        """ check weather user info comes with his profile """  
        serial_user = UserProfileSerializer(self.user).data
        expected_data = {
            "id":self.user.id,
            "email":self.user.email,
            "first_name":self.user.first_name,
            "last_name":self.user.last_name,
            "profile":{
                "unid":self.profile.unid,           
                "user_id": self.user.id, 
                "first_name":"",
                "last_name":"",
                "display_name":"",
                "image":None,
                "website":"",
                "linkedin_profile":"",
                "name":self.user.get_name
            }
            
        }           
        self.assertEqual(serial_user, expected_data)

    def test_user_serializer_via_profile_attr(self):      
        """ check weather user info comes with his profile via obj user"""  
        serial_user = UserProfileSerializer(self.user).data
        expected_data = {
            "id":self.user.id,
            "email":self.user.email,
            "first_name":self.user.first_name,
            "last_name":self.user.last_name,
            "profile":{
                # here 
                "unid":self.user.profile.unid,           
                "user_id": self.user.id, 
                "first_name":"",
                "last_name":"",
                "display_name":"",
                "image":None,
                "website":"",
                "linkedin_profile":"",
                "name":self.user.get_name
            }
            
        }           
        self.assertEqual(serial_user, expected_data)

    

