from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()   

class UniqueDisplayNameTest(TestCase):
    def test_user_has_profile(self):
        user1 = User.objects.create(email="zoo@mail.com",password="abdhdhdhd")
        user2 = User.objects.create(email="zoo@yahoo.com",password="fgfggfgf")
        user1_display_name = user1.get_name
        user2_display_name = user2.get_name        
        self.assertNotEqual(user1_display_name,user2_display_name)

