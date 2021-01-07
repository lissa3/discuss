"""united URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#rest
from rest_framework import  routers
from api.viewsets import IdeaViewSet #UserViewSet,
from api.views import ProfileRetrUpdateDestrView,UserInfoView
# oAuth
from django.conf.urls import url
from users.views import auth




# The API URLs are now determined automatically by the router.
router = routers.DefaultRouter()
# router.register(r'all-users', UserViewSet) # just for test purposes
# router.register(r'profiles', ProfileViewSet)
# router.register(r'profiles', ProfileRetrUpdateDestrView)
router.register(r'ideas',IdeaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ideas.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('comments/',include('comments.urls')),      
    
]

urlpatterns += [
    # required for drf in general:
    # api point:/api-auth/login/ (browser drf admin) and /api-auth/logout/ (browser drf admin) |=> re-direct to profile if present (but anyway you can see the admin page)
    path('api-auth/', include('rest_framework.urls')),
    # path to djoser end-points
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),#extra (check if it's needed)
    path('auth/', include('djoser.social.urls')),
    # jwt auth
    path('auth/', include('djoser.urls.jwt')),
    # oAuth (kudrya )
    url('', include('social_django.urls', namespace='social')),
    path('auth-github/',auth),
    # api for profile,userinfo (profile + user)
    path('api-profile/<int:pk>/',ProfileRetrUpdateDestrView.as_view(),name="profile-detail"),
    path('api-user/',UserInfoView.as_view(),name="user-info"),
    # the rest of the endpoints
    path('api/v1/',include(router.urls)),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

admin.site.index_title = "World of Ideas" 
admin.site.site_header = "Where is my site header?"   
admin.site.site_title = "HomeAdmin"   


#Your URL pattern
#djoser urls
# ************************************
# step N 1: register user

# url: auth/users/
# other features
# url: auth/users/...кучи разных экстра для создания и опереций над юзерами
# like: confirm email, reset psw
# step N2
# activate
# auth/users/activate
# http://127.0.0.1:8080/activate/NDM/5ir-d995..
#*************************************
# from front 
# auth/users/activation/ + params(uid,token)
# step N 3(login and logout)
# login logout via djoser regular token (see table in db)

"""
auth/ token/login/?$ [name='login']
auth/ token/logout/?$ [name='logout']
# step N3 (jwt) |==> no table in db
# for jwt token
auth/ jwt/create/? [name='jwt-create']
auth/ jwt/refresh/? [name='jwt-refresh']
auth/ jwt/verify/? [name='jwt-verify']
# psw reset
flow == flow by signup (also via email)
auth/ ^users/reset_password/$ [name='user-reset-password']
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']

#end djoser

[<URLPattern '^api/v1/users//$' [name='user-list']>, 
<URLPattern '^api/v1/users\.(?P<format>[a-z0-9]+)/?$' [name='user-list']>,
 <URLPattern '^api/v1/users//(?P<pk>[^/.]+)/$' [name='user-detail']>,
 <URLPattern '^api/v1/users//(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='user-detail']>, <URLPattern '^$' [name='api-root']>, 
 <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>] 
 is invalid. Ensure that urlpatterns is a list of path() and/or re_path() instances.
 """