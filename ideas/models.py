from django.db import models
from django.contrib.auth import get_user_model
from utils.models import TimeStamp
from taggit.managers import TaggableManager
from mptt.models import MPTTModel,TreeForeignKey
from utils.broadcast_utils.base_utils import upload_img
# from django.shortcuts import reverse
from django.urls import reverse
# from tinymce import HTMLField

User = get_user_model()

class CategoryManager(models.Manager):
    pass
    # def get_category_count(self):
    #     ''' make qs ready for iter-n through objects - objects.count
    #         to display total posts for each category
    #     '''
    #     return Category.objects.annotate(count=Count('ideas'))


class Category(MPTTModel):
    name = models.CharField(max_length=120,unique=True)
    parent = TreeForeignKey('self',
                        on_delete = models.CASCADE,
                        null=True,
                        blank=True,
                        related_name = 'children'
                        )
    objects = CategoryManager()

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']

    class Meta:
        verbose_name_plural = 'Categories'    
        
    def __str__(self):
        return self.name


class IdeaManager(models.Manager):
    pass

    # def search(self,words):
    #     '''can be used for no results of first-line-search based on title,overview '''
    #     lookup = ( models.Q(content__icontains=words)|
    #                 models.Q(tags__name__icontains=words)
    #                 )
    #     #print(Idea.objects.filter(lookup).distinct())
    #     return Idea.objects.filter(lookup).distinct() 
STATUS_CHOICES = (
    (0,'in progres'),
    (1,'in review'),
    (2,'published')
    
)        

class Idea(TimeStamp,models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    categ = models.ForeignKey(Category,
                            related_name='ideas',
                            on_delete = models.PROTECT,  
                            blank=True)    
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255,blank=True,unique=True)
    lead_text = models.CharField(max_length=254)
    main_text = models.TextField()    
    view_count = models.IntegerField(blank=True,default=0)
    thumbnail = models.ImageField(blank=True,null=True,upload_to=upload_img)
    featured = models.BooleanField(blank=True,default=False)
    likes = models.IntegerField(blank=True,default=0)
    dislikes = models.IntegerField(blank=True,default=0)   
    is_public = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    tags = TaggableManager(blank=True,verbose_name="Tags",help_text="Tags should be separated by comma")
    
    objects = IdeaManager()

    def __str__(self):
        return self.title

    # 
    # class Meta:
    #     ordering = ['-created_at'] 
    
    @property
    def get_idea_image(self,*args,**kwargs):
        """ return path to idea image """
        if self.thumbnail:
            return f'/media/{self.thumbnail}/'
    
    def get_absolute_url(self):       
        return reverse('ideas:detail', kwargs={'slug':self.slug})

        
