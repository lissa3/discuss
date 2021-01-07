from django.test import TestCase
from ideas.models import Idea,Category
from api.serializers import IdeaTestSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class IdeaTestSerializerTesCase(TestCase):
    """ note: had to dismiss created_at field for the purpose of testing"""
    def setUp(self):
        self.category = Category.objects.create(name="chat")
        self.user1 = User.objects.create(email="zoo@mail.com")
        self.idea1 = Idea.objects.create(
            title="first idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 1",
            main_text = "Main text one", 
            status = 1,                                 

        )
        self.idea2 = Idea.objects.create(
            title="second idea",
            author=self.user1,
            categ = self.category,
            lead_text = "Greet 2",
            main_text = "Main text two",
                     

        )
        
    def test_idea_serializer(self):        
        ideas = Idea.objects.all()        
        serial_ideas = IdeaTestSerializer(ideas, many=True).data
        # print(serial_ideas)
        expected_data = [
            {"id": self.idea1.id,
            "title": "first idea",
            "author": self.user1.id,
            "lead_text":"Greet 1",
            'categ':self.idea1.categ.id,
            "main_text":"Main text one",
            "owner_idea":self.user1.get_name,
            "status":1
            },
            {"id": self.idea2.id,
            "title": "second idea",
            "author": self.user1.id,
            "lead_text":"Greet 2",
            "categ":self.idea2.categ.id,
            "main_text":"Main text two",
            "owner_idea":self.user1.get_name,
            "status":0
            }
             
        ]
        # print("**************")
        # print("exp",expected_data)
        self.assertEqual(serial_ideas, expected_data)
"""
local 
[OrderedDict([('id', 2), ('title', 'second idea'), ('author', 1), ('lead_text', 'Greet 2 rio'), ('main_text', 'Main text two'), ('owner_idea', 'zoo'), ('categ', 1), ('created_at', '2020-09-19T22:02:00.195277Z'), ('status', 1), ('thumbnail', None)]), 
OrderedDict([('id', 3), ('title', 'third idea'), ('author', 1), ('lead_text', 'Greet 3 '), ('main_text', 'Main text three rio'), ('owner_idea', 'zoo'), ('categ', 1), ('created_at', '2020-09-19T22:02:00.196072Z'), ('status', 2), ('thumbnail', None)])]

server resp 
[OrderedDict([('id', 2), ('title', 'second idea'), ('author', 1), ('lead_text', 'Greet 2 rio'), ('main_text', 'Main text two'), ('owner_idea', 'zoo'), ('categ', 1), ('created_at', '2020-09-19T22:02:00.195277Z'), ('status', 1), ('thumbnail', None)]), 
OrderedDict([('id', 3), ('title', 'third idea'), ('author', 1), ('lead_text', 'Greet 3 '), ('main_text', 'Main text three rio'), ('owner_idea', 'zoo'), ('categ', 1), ('created_at', '2020-09-19T22:02:00.196072Z'), ('status', 2), ('thumbnail', None)])]


"""

