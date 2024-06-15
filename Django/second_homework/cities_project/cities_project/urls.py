from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cities import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
