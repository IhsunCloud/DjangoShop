from django.urls import path

from .views import * 

app_name = 'weblog'


urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('post/<slug:slug>/', SinglePostView.as_view(), name='single-post'),
]