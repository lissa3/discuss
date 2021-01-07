from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Idea
from comments.models import Comment
from .forms import CommentForm
# from .forms import CommentForm
# delete
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

User = get_user_model()

class IdeaList(ListView):
    model = Idea

class IdeaDetail(DetailView):
    """ idea:get |=> re-direct to edit or delete"""
    model = Idea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.all()
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Idea,slug=slug)
        
    def post(self,request,**kwargs):
        """
        parent and comment in request.POST.get: are optional and come as a string}
        this post method for all forms(id=newForm) from front (not ajax)
        """ 
           
        if request.POST.get('parent'):
            parent_id = int(request.POST.get('parent'))
            parent_comment = get_object_or_404(Comment,id=parent_id)
            reply_to_user_id = parent_comment.user.id                      
        else:
            parent_id = None 
            reply_to_user_id = None  
        
        if request.POST.get('comment'):
            comment_id = int(request.POST.get('comment'))            
            comment = get_object_or_404(Comment,id=comment_id)
            update_comment_body = request.POST.get('body')
        else:
            comment = None     

        form = CommentForm(request.POST)
        if form.is_valid() and comment:
            comment.body = update_comment_body
            comment.save()
            return redirect(self.get_object().get_absolute_url())
        elif form.is_valid and comment == None:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.idea = self.get_object()
            comment.parent_id = parent_id 
            if reply_to_user_id:
                comment.reply_to_id = reply_to_user_id            
            comment.save()  
        else:
            print("invalid comment")
            print("think about feedback") 
            return JsonResponse({"errorMsg":"form is not valid"})   

        return redirect(self.get_object().get_absolute_url())
            
              
        
                    
                         
        # return   reverse('ideas:detail',kwargs={'slug':self.slug})  
        
# if form.is_valid():
#     instance = form.save()
#     ser_instance = serializers.serialize('json', [ instance, ])
#     # send to client side.
#     return JsonResponse({"instance": ser_instance}, status=200)
# else:
#     return JsonResponse({"error": form.errors}, status=400)
        
            





@csrf_exempt
def foo(request):
    if request.method =="POST":
        payload = request.body
        py_dict = json.loads(payload)      
               
        email = py_dict.get('email','no email')
        password = py_dict.get('password','no password')       
        return JsonResponse({"psw":password,"email":email})
       
    else:     
        ans = {"name":"It was get request"} 
        return  JsonResponse(ans)
        
    





