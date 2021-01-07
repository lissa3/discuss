import random
import string
from django.utils.text import slugify
import os

def get_random_str(size):
    """create random sting from letters and digits"""
    chars = string.ascii_letters+string.digits
    final_str = [random.choice(chars) for _ in range(size)]
    return "".join(final_str)

def get_random_num(size):
    """create random sting from letters and digits"""
    chars = string.digits
    final_digits = [random.choice(chars) for _ in range(size)]
    return "".join(final_digits)


def make_unid(instance,size = 5):
    """
    create unique id for instance based on random letters and digits
    which have attr = uid
    """
    klass = instance.__class__
    start_unid = get_random_str(size)
    if klass.objects.filter(unid=start_unid).exists():
        instance.unid = get_random_str(size)
        return make_unid(instance)
    return start_unid 

def make_slug(instance,new_slug=None):
    """
    instance of model with slug attr and char(title)
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
        
    Klass = instance.__class__
    qs_exist = Klass.objects.filter(slug=slug).exists()
    if qs_exist:        
        extra = get_random_str(4)        
        new_slug = f"{slug}-{extra}"        
        return make_slug(instance,new_slug=new_slug)     
    return slug
    
# def make_unique_slug(instance,size=6):
#     """create unique slug based on random digits and letters"""
#     Klass = instance.__class__
#     slug_ = get_random_str(size)
#     qs_exist = Klass.objects.filter(slug= slug_).exists()
#     if qs_exist:
#         instance.slug = get_random_str(size)      
#         return make_unique_slug(size) 
#     return slug_       

        

def make_username(instance,new_username=None):
    """
    create unique display name(dn) for instance based on random digits;
    dn == email but in case user created 2 accounts based on different host
    like sally@mail.com and sally@yahoo.com
    dn will be sally and sally1234
    """      
    if new_username is not None:
        username = new_username
    else:
        name = instance.email
        head,tail = name.split("@")
        username = head
                   
    Klass = instance.__class__
    qs_exist = Klass.objects.filter(username= username).exists()
    if qs_exist:
        username = f"{username}@{get_random_num(4)}"        
        return make_username(instance,new_username=username)
    return username 

def upload_img(instance,filepath):
    """make path to uploaded file (avatar) and adjust file name if needed 
    note: used user id instead of instance (because it doesn't have it yet)
    """
    filename = os.path.basename(filepath)         # 'abababa.jpeg'
    name,ext = os.path.splitext(filename)         # tuple ('abababa', '.jpeg')
    if len(name) > 5:
         name = name[:5]
    new_file_name = name + ext    
    # timestemp = timezone.now().strftime("%Y-%m-%d")
    
    klass = (instance.__class__.__name__).lower()
    if klass == 'idea':
        user_folder = f'idea_{instance.author.id}'
        return  os.path.join('ideapot',user_folder,new_file_name)
    elif klass == 'profile':
        user_folder = f'profile_{instance.user.id}'
        return  os.path.join('avatar',user_folder,new_file_name)

def create_color():
    red = random.randint(0, 266)
    green = random.randint(0, 266)
    blue = random.randint(0, 266)
    return f'({red},{green},{blue})'