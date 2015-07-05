from django.conf.urls import url

from food import views

urlpatterns = [
    url(r'^menu/$', views.MealView.as_view(), name='meals'),
    url(r'^detail/(?P<pk>\d+)$', views.MealDetailView.as_view(), name='detail'),
]
