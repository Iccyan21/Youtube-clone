from django.urls import path
from .views import video_list,upload_video, VideoDetail,user_detail, channel_subscribe,add_comment
from django import views


urlpatterns = [
    path('', video_list, name='video_list'),
    path('upload_video/',upload_video, name="upload_video"),
    path('detail/<int:pk>/', VideoDetail, name='video_detail'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('user/<int:pk>/subscribe/', channel_subscribe, name='channel_subscribe'),
    path('videos/<int:pk>/comment/', add_comment, name='add_comment'),
]
