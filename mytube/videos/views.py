from django.shortcuts import render
from .models import Video, Comment
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import VideoForm
from django.views.generic import DetailView
from accounts.models import User
from django.db import models

def video_list(request):
    videos = Video.objects.all()
    params = {
        'videos':videos
    }
    return render(request, 'videos/video_list.html', params)


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('videos:video_list')
    else:
        form = VideoForm()
    return render(request, 'videos/upload_video.html', {'form': form})

def VideoDetail(request , pk):
    VideoDetail_data = get_object_or_404(Video, pk=pk)
    Comment_data = Comment.objects.all()
    VideoDetail_data.views += 1  # 再生回数を1増やす
    VideoDetail_data.save()
    
    params = {
        'VideoDetail_data':VideoDetail_data,
        'Comment_data': Comment_data,
    }
    return render(request, 'videos/video_detail.html', params)

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    videos = Video.objects.filter(user=user)
    params = {
        'user': user,
        'videos': videos,
    }
    return render(request, 'videos/user_detail.html', params)


def channel_subscribe(request, pk):
    user = get_object_or_404(User, pk=pk)
    subscriber = request.user
    if subscriber != user:
        user.subscribers = list(user.subscribers)
        user.subscribers.append(subscriber)
        user.subscribers = tuple(user.subscribers)
        
    return redirect('/videos/video_detail/', pk=user.pk)

def add_comment(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            comment = Comment.objects.create(
                user=request.user,
                video=video,
                text=comment_text,
            )
            comment.save()
    
            return redirect('video_detail', pk=pk)

    return redirect('video_detail', pk=pk)