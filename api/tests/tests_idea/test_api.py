from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ideas.models import Idea,Category
from api.serializers import IdeaSerializer
from rest_framework.exceptions import ErrorDetail
from django.contrib.auth import get_user_model
import json

User = get_user_model()

        
class IdeaTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="chat")
        url = 'http://127.0.0.1:8000/auth/jwt/create/'
        self.user1 = User.objects.create(email="zoo@mail.com",password="viola34")
        self.user2 = User.objects.create(email="giraf@mail.com",password="yahoo34")
        self.idea1 = Idea.objects.create(
            title="first idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 1",
            main_text = "Main text one"            

        )
        self.idea2 = Idea.objects.create(
            title="second idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 2",
            main_text = "Main text two"           

        )
        
    def test_get_all_ideas(self):
        url = reverse('idea-list')
        response = self.client.get(url)          
        local_serialized_data = IdeaSerializer([self.idea1,self.idea2],many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_serialized_data,response.data)

    def test_get_one_idea(self):        
        ideas = Idea.objects.all()
        url = reverse('idea-detail',kwargs={"pk":self.idea1.id})
        response = self.client.get(url)          
        local_serialized_data = IdeaSerializer(ideas.filter(id=self.idea1.id).last()).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(local_serialized_data,response.data)

    def test_create_idea(self):
        """in setUp idea (author == req.user)""" 
        self.assertEqual(2,Idea.objects.all().count())    
        url = reverse('idea-list')        
        new_idea = {
            "title": "to delete",
            "lead_text":"greet testsn",
            "categ":self.category.id,
            "main_text":"test it again",
            
        }
        json_data = json.dumps(new_idea)     
        self.client.force_authenticate(user=self.user1)  
        response = self.client.post(url,data=json_data,content_type="application/json")
        author_new_idea = Idea.objects.last().author
        new_idea = Idea.objects.last()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(3,Idea.objects.all().count())  
        self.assertEqual(self.user1,Idea.objects.last().author)  
        

    def test_put_update_idea(self):
        """in setUp idea (user is auth-ed; author == req.user)"""
        self.client.force_authenticate(user=self.user1)  
        url = reverse('idea-detail', args=(self.idea2.id,))
        modified_idea = {
            "title":"second idea modified",
            "author":self.user1.id,
            "categ":self.category.id,
            "lead_text":"Greet 2 modified",
            "main_text":"Main text two"           

        }
        json_edited_idea = json.dumps(modified_idea)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.idea2.refresh_from_db()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(self.idea2.lead_text,"Greet 2 modified")

    def test_put_update_idea_not_author(self):
        """ Important to add:  user is auth-ed but not the author of the idea)"""
        self.client.force_authenticate(user=self.user2)  
        url = reverse('idea-detail', args=(self.idea2.id,))
        modified_idea = {
            "title":"second idea modified",
            "author":self.user1.id,
            "categ":self.category.id,
            "lead_text":"Greet 2 modified",
            "main_text":"Main text two"           

        }
        json_edited_idea = json.dumps(modified_idea)
        resp = self.client.put(url, data=json_edited_idea, content_type='application/json')
        self.idea2.refresh_from_db()
        error_msg = {'detail': ErrorDetail(string='You do not have permission to perform this action.',\
                        code='permission_denied')}
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.idea2.lead_text,"Greet 2")
        self.assertEqual(resp.data,error_msg)        


    def test_delete_idea(self):
        """author of the idea == req.user can DELETE his idea"""
        self.client.force_authenticate(user=self.user1)  
        initial_count_ideas = Idea.objects.count()
        url = reverse('idea-detail', args=(self.idea2.id,))     
        resp = self.client.delete(url)
        final_count_ideas = Idea.objects.count()
        self.assertEqual(resp.status_code, 204)
        self.assertNotEqual(initial_count_ideas,final_count_ideas)

    def test_delete_idea_by_not_author(self):
        """auth-ed user but not author of the idea CAN'DELETE idea of others"""

        self.client.force_authenticate(user=self.user2)  
        initial_count_ideas = Idea.objects.count()
        url = reverse('idea-detail', args=(self.idea2.id,))     
        resp = self.client.delete(url)
        final_count_ideas = Idea.objects.count()
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(initial_count_ideas,final_count_ideas)
       

    def test_delete_idea_by_staff(self):
        """staff can DELETE any idea"""
        self.user3 = User.objects.create(username="boo@faoo.com", is_staff=True)
        self.client.force_authenticate(user=self.user3)  
        initial_count_ideas = Idea.objects.count()
        url = reverse('idea-detail', args=(self.idea2.id,))     
        resp = self.client.delete(url)
        final_count_ideas = Idea.objects.count()
        self.assertNotEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        
        

class IdeaApiSearchOrderingTestCase(APITestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="chat")
        self.user1 = User.objects.create(email="zoo@mail.com")
        self.idea1 = Idea.objects.create(
            title="first idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 1",
            main_text = "Main text one",
            status = 1            

        )
        self.idea2 = Idea.objects.create(
            title="second idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 2 rio",
            main_text = "Main text two" ,
            status=1           

        )
        self.idea3 = Idea.objects.create(
            title="third idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 3 ",
            main_text = "Main text three rio",
            status=2            

        )
    def test_get_search(self):
        """search: test to catch word in title/lead_text/main_text
        """
        url = reverse('idea-list')        
        serializer_data = IdeaSerializer([self.idea2,self.idea3], many=True).data        
        resp = self.client.get(url, data={"search": "rio"})        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)

    def test_get_filter(self):
        """search: test to get filter for status;
        """
        url = reverse('idea-list')       
        serializer_data = IdeaSerializer([self.idea1,self.idea2], many=True).data        
        resp = self.client.get(url, data={"status": "1"})        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)
        self.assertEqual(len(serializer_data),len(resp.data))

    def test_get_order(self):
        """search: test to get filter for status;
        """
        url = reverse('idea-list')       
        serializer_data = IdeaSerializer([self.idea3,self.idea2,self.idea1], many=True).data       
        resp = self.client.get(url, data={"ordering":"-created_at"})        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, resp.data)
        
        

 

