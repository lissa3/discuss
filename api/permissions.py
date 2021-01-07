from rest_framework.permissions import BasePermission
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAuthorOrIsStaffOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `author` attribute.
    has_object permission (for obj with id)
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # Instance must have an attribute named `author`.
        
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.author==request.user or request.user.is_staff)
        )
             
        
class IsOwnerOrIsStaff(BasePermission):
    """
    Instance must have an attribute named `user_id`.
    Only user == owner of the obj OR user == staff can RUD operations on obj
    """
    
    def has_object_permission(self, request, view, obj):        
        return bool(
            request.user and request.user.is_authenticated and 
            (obj.user_id==request.user.id or request.user.is_staff)
        )
                   
