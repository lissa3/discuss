from django.test import TestCase
from profiles.models import Profile
from api.account.profile_serializer import ProfileSerializer
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()



class ProfileSerializerTesCase(TestCase):
    """compare expected and received data after ser-on"""
    def setUp(self):        
        self.user = User.objects.create(email="zoo@mail.com")        
        self.profile = Profile.objects.last()
        
    def test_profile_serializer(self):      
        """ let op: not arr but dict"""     
        serial_profile = ProfileSerializer(self.profile).data
        expected_data = {
                "unid": self.profile.unid,            
                "user_id": self.user.id, 
                "first_name":"",
                "last_name":"",
                "display_name":"",
                "image":None,
                "website":"",
                "linkedin_profile":"",
                "name":self.user.get_name
            }           
        self.assertEqual(serial_profile, expected_data)


