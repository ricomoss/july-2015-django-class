from django.conf.urls import url

from food import views

urlpatterns = [
    url(r'^menu/$', views.MealListView.as_view(), name='meals'),
    url(r'^detail/(?P<pk>\d+)$', views.MealDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.MealEditView.as_view(), name='edit'),
]
