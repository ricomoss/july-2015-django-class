from django.conf.urls import url, include

from common import views

review_patterns = [
    url(r'^review/(?P<meal_id>\d+)$', views.ReviewListView.as_view(), name='index'),
]

urlpatterns = [
    url(r'^common/', include(review_patterns, namespace='review')),
]
