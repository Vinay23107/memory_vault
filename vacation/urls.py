"""
URL configuration for vacation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vac_images/', views.vac_images, name='vac_images'),
    path('login/', views.mylogin, name='mylogin'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('add_album/', views.add_album, name='add_album'),
    path('edit_album/', views.edit_album, name='edit_album'),
    path('handle_edit_album/', views.handle_edit_album, name='handle_edit_album'),
    path('handle_add_album/', views.handle_add_album, name='handle_add_album'),
    path('delete_album/', views.delete_album, name='delete_album'),
    path('my_album/', views.my_album, name='my_album'),
    path('my_image/', views.my_image, name='my_image'),
    path('add_image/', views.add_image, name='add_image'),
    path('handle_add_image/', views.handle_add_image, name='handle_add_image'),
    path('edit_image/', views.edit_image, name='edit_image'),
    path('handle_edit_image/', views.handle_edit_image, name='handle_edit_image'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('view_image/', views.view_image, name='view_image'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)