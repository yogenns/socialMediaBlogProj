from django.conf.urls import url
from . import views
app_name = 'posts'

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='all'),
    url('new/',views.CreatePost.as_view(),name='create'),
    url('by/(?P<username>[-\w]+)',views.UserPosts.as_view(),name='for_user'),
    url('by/(?P<username>[-\w]+)/(?P<pk>\d+)/',views.PostDetail.as_view(),name='single'),
    url('delete/(?P<pk>\d+)/',views.DeletePost.as_view(),name='delete'),
]