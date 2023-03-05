from django.shortcuts import render, redirect
import datetime
import time
import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# add now
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
# add 2023-2-1
from django.contrib import messages
from PandoraBox import settings
from channels.models import Channel
from contents.models import Content
from userdetails.models import Userdetail
from contents.forms import Contentform
from subscriptions.models import Subscription
from django.views.decorators.http import require_http_methods
# @require_http_methods(["GET"])


def search_view(request):
    # userdetail = User_detail.objects.all().order_by('id')
    keywords = request.GET['keywords']
    querylist = Content.objects.filter(
        tag__icontains=keywords).order_by('-dateupload')
    paginator = Paginator(querylist, 3)
    page = request.GET.get('page')
    paged_querylist = paginator.get_page(page)

    context = {
        'listings': paged_querylist,
        'keywords': keywords
    }
    return render(request, "contents/search.html", context)


 


def contentlist_view(request):
    content_list = Content.objects.all()
    paginator = Paginator(content_list, 2)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'contentlist.html', {'page_obj': page_obj})


def content_insert_view(request, template_name='contents/content_ins_form.html'):
    if request.method == 'POST':
        form = Contentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('channels')
    else:
        form = Contentform()
    return render(request, template_name, {'form': form})



def content_insertb_view(request):
    if request.method == 'POST':
        channel     = request.POST['channel']
        user        = request.POST['user']
        title       = request.POST['title']
        description = request.POST['description']
        level       = request.POST['level']
        image       = request.POST['image']
        video       = request.POST['video']
        videolink   = request.POST['videolink']
        youtubelink = request.POST['youtubelink']
        dateupload  = request.POST['dateupload']
        tag         = request.POST['tag']
        content = Content.objects.create(channel=channel, user=user, title=title, description=description, level=level, image=image, video=video, videolink=videolink, youtubelink=youtubelink, dateupload=dateupload, tag=tag)
        messages.success(request, 'content record is now inserted!')
        return redirect('creators')
    else:
        context = {
            'vchannel': 'testchannel',
            'vuser' : 'test'
        }    
        return render(request, 'contents/content_insert.html')
    


def content(request, content_id):
    content = Content.objects.all().filter(id=content_id)
    channel_id = Content.objects.values_list(
        'channel_id').filter(id=content_id)[0]
    if Subscription.objects.values_list(
            'level').order_by('-level').filter(channel_id=channel_id, user_id=request.user.id).exists():
        subscription = Subscription.objects.values_list(
            'level').order_by('-level').filter(channel_id=channel_id, user_id=request.user.id)[0]
        subscription = subscription[0]
    else:
        subscription = 0
    print(subscription)
    context = {
        'content': content,
        'subscription': subscription,
    }
    return render(request, 'contents/content.html', context)


def content_update_view(request, id):
    content = Content.objects.all().filter(id=id).first()
    form = Contentform(request.POST, instance=content)
    if form.is_valid():
        form.save()
        return redirect("creatorbox")
    return render(request, "contents/content_update.html", {'content': content})
