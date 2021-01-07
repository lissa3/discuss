class UpdateCustomerProfile(permissions.BasePermission):
"""Allow customers to edit their own profile """
    def has_permission(self, request, view):
    """Check if user is authenticated and has permisson to access customer model """
        if view.action == 'list':
        return request.user.is_authenticated and request.user.is_superuser
        elif view.action == 'create':
        return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
        return request.user.is_authenticated
        else:
        return False
#My customer view set:
class CustomerViewSet(viewsets.ModelViewSet):
"""Handle creating reading and updating Users in system"""
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.filter()
    permission_classes = (permissions.UpdateCustomerProfile,)
# But I get an error saying:
# "detail": "Authentication credentials were not provided."
# even If I add the token in Authorisation field of Header.
# UPDATE:
# If I add authentication_classes = (TokenAuthentication,) to my CustomerViewSet I get an error:
# "detail": "You do not have permission to perform this action."
# I'm confused, I want to leverage the current authorisation of an User to authorise creation of a customer. i.e Only An authenticated user should be able to create his Customer profile
# How can I fix this?
#You should add authentication_classes attribute to the view
from rest_framework.authentication import TokenAuthentication

class CustomerViewSet(viewsets.ModelViewSet):
"""Handle creating reading and updating Users in system"""
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.filter()
    permission_classes = (permissions.UpdateCustomerProfile,)
    authentication_classes = (TokenAuthentication,)