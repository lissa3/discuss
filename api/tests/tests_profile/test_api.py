from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APITestCase
import json
from profiles.models import Profile
from api.account.profile_serializer import ProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializerTesCase(APITestCase):
    """(C*)RUD operations around given profile object"""
    def setUp(self):        
        self.user1 = User.objects.create(email="zoo@mail.com")        
        self.user2 = User.objects.create(email="daspy@mail.com")
        self.user_staff = User.objects.create(email="mystaff@mail.com",is_staff=True)
                 
        self.profile = Profile.objects.filter(user_id=self.user1.id).last()
# ################## GET <=> READ ##########################################################        
   
    def test_get_single_profile_owner(self):      
        """ user profile owner can READ profile"""
        self.client.force_authenticate(user=self.user1)         
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        response = self.client.get(url)
        serial_profile = ProfileSerializer(self.profile).data             
        self.assertEqual(response.status_code, status.HTTP_200_OK)              
        self.assertEqual(response.data, serial_profile)

    def test_get_single_profile_staff(self):      
        """ user staff can READ profile of others"""
        self.client.force_authenticate(user=self.user_staff)         
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        response = self.client.get(url)
        serial_profile = ProfileSerializer(self.profile).data             
        self.assertEqual(response.status_code, status.HTTP_200_OK)              
        self.assertEqual(response.data, serial_profile)

    def test_get_profile_by_not_owner(self):      
        """ user NOT profile owner can't READ profile"""
        self.client.force_authenticate(user=self.user2) 
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)                     

# ################### DELETE #############################################
    def test_delete_profile_by_owner(self):      
        """ user profile owner can DELETE his profile"""
        start_count =Profile.objects.count()
        self.client.force_authenticate(user=self.user1) 
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        resp = self.client.delete(url)
        final_count = Profile.objects.count()
        self.assertEqual(resp.status_code, 204) 
        self.assertNotEqual(start_count,final_count)

    def test_delete_profile_by_staff(self):      
        """ user staff can DELETE given profile"""
        start_count =Profile.objects.count()
        self.client.force_authenticate(user=self.user_staff) 
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        resp = self.client.delete(url)
        final_count = Profile.objects.count()
        self.assertEqual(resp.status_code, 204) 
        self.assertNotEqual(start_count,final_count)


    def test_delete_profile_by_not_owner(self):      
        """ user = !profile owner can't  DELETE profile of others"""
        start_count =Profile.objects.count()
        self.client.force_authenticate(user=self.user2) 
        url = reverse('profile-detail',kwargs={"pk":self.user1.id})
        resp = self.client.delete(url)
        final_count = Profile.objects.count()
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)  
        self.assertEqual(start_count,final_count)

# ################### UPDATE <=> PUT ##################################
    def test_put_update_profile(self):
        """ user == owner of the profile can change his profile"""
        self.client.force_authenticate(user=self.user1)
        initial_user_name = self.user1.get_name  
        url = reverse('profile-detail',kwargs={"pk":self.user1.id} )
        modified_profile = {
            "unid":self.profile.unid,
            "user_id":self.user1.id,
            "first_name":"ann",
            "last_name":"joe"                      

        }
        modified_user_name = "Ann Joe"
        json_edited_idea = json.dumps(modified_profile)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.profile.refresh_from_db()
        self.user1.refresh_from_db() 
        final_user_name = self.user1.get_name     
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertNotEqual(initial_user_name,modified_user_name)            
        self.assertEqual(final_user_name,modified_user_name)  

    def test_put_update_display_name(self):
        """ user == owner of the profile can change his display name"""
        self.client.force_authenticate(user=self.user1)
        initial_display_name = self.user1.profile.display_name  
        url = reverse('profile-detail',kwargs={"pk":self.user1.id} )
        modified_profile = {
            "unid":self.profile.unid,
            "user_id":self.user1.id,
            "display_name":"blue sky"                    
        }
        json_edited_idea = json.dumps(modified_profile)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.profile.refresh_from_db()
        self.user1.refresh_from_db() 
        final_display_name = self.user1.profile.display_name 
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertNotEqual(initial_display_name,final_display_name)            
        

    def test_put_update_profile(self):
        """ user not owner of given profile CAN'T CHANGE the profile"""
        self.client.force_authenticate(user=self.user2)
        initial_user_name = self.user1.get_name  
        url = reverse('profile-detail',kwargs={"pk":self.user1.id} )
        modified_profile = {
            "unid":self.profile.unid,
            "user_id":self.user1.id,
            "first_name":"boze",
            "last_name":"wolf"                      

        }
        modified_user_name = "Boze Wolf"
        json_edited_idea = json.dumps(modified_profile)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.profile.refresh_from_db()
        self.user1.refresh_from_db() 
        final_user_name = self.user1.get_name 
        self.assertEqual(resp.status_code,status.HTTP_403_FORBIDDEN )
        self.assertEqual(initial_user_name,final_user_name)            
        self.assertNotEqual(final_user_name,modified_user_name) 

    def test_put_update_profile(self):
        """ user == staff can change any profile"""
        self.client.force_authenticate(user=self.user_staff)
        initial_user_name = self.user1.get_name  
        url = reverse('profile-detail',kwargs={"pk":self.user1.id} )
        modified_profile = {
            "unid":self.profile.unid,
            "user_id":self.user1.id,
            "first_name":"xxx",
            "last_name":"yyy"                      

        }
        modified_user_name = "Xxx Yyy"
        json_edited_idea = json.dumps(modified_profile)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.profile.refresh_from_db()
        self.user1.refresh_from_db() 
        final_user_name = self.user1.get_name     
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertNotEqual(initial_user_name,modified_user_name)            
        self.assertEqual(final_user_name,modified_user_name)            
  
        
        

             
        
