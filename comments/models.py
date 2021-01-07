from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ideas.models import Idea

User = get_user_model()

class Comment(MPTTModel):
    idea = models.ForeignKey(Idea,on_delete= models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    # tree structure
    parent = TreeForeignKey("self",
                        on_delete=models.SET_NULL,
                        null=True,
                        blank=True,
                        related_name="children"
                        )
    #record second comments to whom,str
    reply_to = models.ForeignKey(User,
                        null=True,
                        blank=True,
                        on_delete=models.CASCADE,
                        related_name='reply_ers'
                        )
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(blank=True,default=False)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['created']


    def __str__(self):
            return self.body[:15]





