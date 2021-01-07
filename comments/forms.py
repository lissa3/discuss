from django import forms
from .models import Comment
# from mptt.forms import TreeNodeChoiceField


from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    _attrs = {'rows':2,'cols':20,
    'class':'form-control'}
    body = forms.CharField(widget=forms.Textarea(attrs=_attrs))     

    class Meta:
        model = Comment
        fields = ['body']
    def save(self,*args,**kwargs):
        Comment.objects.rebuild()  
        return super().save(*args,**kwargs)     

# class CommentForm(forms.ModelForm):
#     _attrs = {'rows':2,'cols':20,
#     'class':'form-control',
#     'placeholder':'leave your comment'}
#     body = forms.CharField(widget=forms.Textarea(attrs=_attrs)) 
      

#     class Meta:
#         model = Comment
#         # hier is also error (invalid form)
#         fields = ['body','parent']

#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         # bootstrap class: display :none == 'd-none'
#         self.fields['parent'].widget.attrs.update(
#             {'class':'d-none'}
#         )
#         self.fields['parent'].label = ''
#         self.fields['parent'].required = False
#         self.fields['body'].label = ''

    # def save(self,*args,**kwargs):
    #     Comment.objects.rebuild()  
    #     return super().save(*args,**kwargs)  

# <div class="delForm-{{cId}}">

# <form  action="{% url 'comments:edit-comment' %}" method="POST" class="edit_form_comment" data-pId={{pId}} data-cId={{cId}}>
#             {% csrf_token %}
#         <div class="form-group">
#                     <input type="text" name="post_id" hidden value="{{pId}}">
#                     <input type="text" name="comm_id" hidden value="{{cId}}">
#                     {{edit_form.body }}
#         </div>
#         <button  type="submit" class = "btn btn-success">Edit </button>

# </form><br>
# <!-- let op: button should be outside form; otherwise triggered submit -->
# <button class="btn btn-primary" onclick="goBack({{cId}})">Go Back</button>
# </div>
