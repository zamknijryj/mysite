from django.contrib.auth.urls import url
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog'),
    url(r'(?P<pk>[^/]+)', PostDetail.as_view(), name='post'),
    url(r'(?P<pk>[^/]+)/(?P<slug>[-\w]+)$',
        PostDetail.as_view(), name='post_detail'),
]
