from django.shortcuts import render
from contents.models import Content
from channels.models import Channel
from userdetails.models import Userdetail
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
#def index(request):
#    return render(request, 'pages/index.html')

def index(request):
    channels = Channel.objects.all().order_by('-start_date')
    paginator = Paginator(channels, 6)
    page = request.GET.get('page')
    paged_channels = paginator.get_page(page)
    context = {
        'channels': paged_channels  # channels
    }
    return render(request, 'pages/index.html', context)



def otherservices(request):
    return render(request, 'pages/otherservices.html')



def support(request):
    return render(request, 'pages/support.html')

#def creators(request):
#    return render(request, 'creators/creators.html')


def creatorbox(request):
    contents = Content.objects.order_by(
        '-dateupload').filter(user_id=request.user.id)
    user_infos = Userdetail.objects.filter(user_id=request.user.id)
    channel_infos = Channel.objects.order_by(
        'id').filter(user_id=request.user.id)
    context = {
        'contents': contents,
        'user_infos': user_infos,
        'channels': channel_infos
    }
    print(channel_infos)
    print(request.user.id)
    return render(request, 'pages/creatorbox.html', context)

