from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from .models import Comment
from ideas.models import Idea
from .forms import CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
def show_comment(request):
    return render(request,'comments/comment.html')

class EditComment(View):
    """vars in request not in kwargs from front via ajax"""
    
    def get(self,request,*args,**kwargs):
        """return pre-filled edit form for comment"""
       
        idea_id = request.GET.get('ideaId')
        comment_id = request.GET.get('commId')
        parentNodeId = request.GET.get('parentNodeId')
        idea = get_object_or_404(Idea,id=idea_id)
        comment = get_object_or_404(Comment,id=comment_id,idea = idea)
        form = CommentForm(instance = comment)
        context = {'form':form,
                'ideaSlug':idea.slug,
                'parentId':parentNodeId,
                'commId':comment_id,"comBody":comment.body
                }
        html= render_to_string("comments/comment_form.html",context=context,request=request)
        return JsonResponse({"html":html})  

     

        
    


# class EditComment(View):
#     def get(self,request,*args,**kwargs):
#         # kwargs {'slug': 'iFPN16', 'id': 11}
#         idea_slug = kwargs.get('slug')
#         idea = get_object_or_404(Idea,slug=idea_slug)
#         comment_id = kwargs.get('id')
#         comment = get_object_or_404(Comment,id=comment_id,idea = idea)
#         return JsonResponse({"body":comment.body})       
        
#     def post(self,request,*args,**kwargs):
#         idea_slug = kwargs.get('slug')
#         idea = get_object_or_404(Idea,slug=idea_slug)
#         comment_id = kwargs.get('id')
#         comment = get_object_or_404(Comment,id=comment_id,idea = idea)
#         print("post calling with the same args")
#         form  = CommentForm(request.POST)
#         if form.is_valid:
#             print("form is valid")
#             comment = form.save(commit=False)
#             comment.idea_id = idea.id
#             comment.user_id = request.user.id
#             comment.save()
#             print("saving ...")
#             print(comment)
#             return JsonResponse({"status":"ok"})
#         else:
#             return JsonResponse({"err":"form invalid"})

