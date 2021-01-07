from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    """let op: parent is important, otherwise to track of """
    _attrs = {'rows':2,'cols':20,
    'class':'form-control',
    'placeholder':'leave your comment'}
    body = forms.CharField(widget=forms.Textarea(attrs=_attrs)) 
     

    class Meta:
        model = Comment
        fields = ['body']

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['parent'].widget.attrs.update(
    #         {'class':'d-none'}
    #     )
    #     self.fields['parent'].label = ''
    #     self.fields['parent'].required = False
    #     self.fields['body'].label = ''
    
    def save(self,*args,**kwargs):
        Comment.objects.rebuild()  
        return super().save(*args,**kwargs)