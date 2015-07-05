from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from accounts import views as accounts_views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', accounts_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', accounts_views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', accounts_views.RegisterView.as_view(), name='register'),
    url(r'^food/', include('food.urls', namespace='food')),
    url(r'^admin/', include(admin.site.urls)),
]
