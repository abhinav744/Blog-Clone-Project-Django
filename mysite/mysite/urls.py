from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views #importing some views from the authorization app

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),  # Right here,when you log out, the next page is the home page.
]
