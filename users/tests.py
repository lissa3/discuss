from django.test import TestCase
from django.core import mail
from django.contrib.auth import get_user_model


User = get_user_model()   

class UserProfileTest(TestCase):
    def test_user_has_profile(self):
        user = User.objects.create(email="zoo@mail.com",password="abdhdhdhd")
        # print("created user")
        # user.save()
        self.assertTrue(hasattr(user,'profile'))

class SendEmailTest(TestCase):
    def test_send_mail(self):
        # Use Django send_mail function to construct a message
        # Note that you don't have to use this function at all.
        # Any other way of sending an email in Django would work just fine. 
        # print('starting checking email func')
        mail.send_mail(
            'Hi, everyone',
            'Here is the message body.',
            'from@example.com',
            ['to@example.com']
        )

        # Now you can test delivery and email contents
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == 'Hi, everyone'
        assert mail.outbox[0].body == 'Here is the message body.'
        assert mail.outbox[0].from_email == 'from@example.com'
        assert mail.outbox[0].to == ['to@example.com']


