from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Channel
# from userdetails.models import Userdetail
from memberships.models import Membership
from contents.models import Content
from subscriptions.models import Subscription
from userdetails.models import Userdetail
from channels.forms import ChannelForm
from django.contrib import messages
# Create your views here.


def channels(request):
    channels = Channel.objects.all().order_by('id')
    paginator = Paginator(channels, 6)
    page = request.GET.get('page')
    paged_channels = paginator.get_page(page)
    context = {
        'channels': paged_channels  # channels
    }
    return render(request, 'channels/channels.html', context)

# /([0-9])\.+/g
# {% <command>%} {% endcomment%}


def channel(request, id, link):
    channel = get_object_or_404(Channel, link=link)
    memberships = Membership.objects.all().order_by('level').filter(channel_id=id)
    rcontents = Content.objects.all().order_by(
        '-dateupload').filter(channel_id=id)[:5]
    contents = Content.objects.all().order_by('-dateupload').filter(channel_id=id)
    paginator = Paginator(contents, 3)
    page = request.GET.get('page')
    paged_contents = paginator.get_page(page)

    contentsLV = Content.objects.all().order_by(
        '-dateupload').filter(channel_id=id).count()

    contentsLV1 = Content.objects.all().order_by(
        '-dateupload').filter(channel_id=id, level=1).count()

    contentsLV2 = Content.objects.all().order_by(
        '-dateupload').filter(channel_id=id, level=2).count()

    contentsLV3 = Content.objects.all().order_by(
        '-dateupload').filter(channel_id=id, level=3).count()

    if Subscription.objects.values_list(
            'level').order_by('-level').filter(channel_id=id, user_id=request.user.id).exists():
        subscription = Subscription.objects.values_list(
            'level').order_by('-level').filter(channel_id=id, user_id=request.user.id)[0]
        subscription = subscription[0]
    else:
        subscription = 0

    context = {
        'channel': channel,
        'memberships': memberships,
        'contents': paged_contents,
        'recent_contents': rcontents,
        'subscription': subscription,
        'contentsLV': contentsLV,
        'contentsLV1': contentsLV1,
        'contentsLV2': contentsLV2,
        'contentsLV3': contentsLV3,
    }

    return render(request, 'channels/channel.html', context)


def subscription(request):
    if request.method == "POST":
        channel_id = request.POST['channel_id']
        channel_url = request.POST['channel_url']
        membership_level = request.POST['membership_level']

        #
        obj, created = Subscription.objects.update_or_create(
            user_id=request.user.id, channel_id=channel_id, level=membership_level
        )
        print('/channels/' + channel_id + '/' + channel_url)
        if created:
            print("aaa")
            return redirect('/channels/' + channel_id + '/' + channel_url + '#membership')

        # obj.save()
        #
        else:
            print("bbb")
            return redirect('/channels/' + channel_id + '/' + channel_url + '#membership')

        
def channel_insert_view(request, template_name='channels/channel_ins_form.html'):
    if request.method == 'POST':
          form = ChannelForm(request.POST, request.FILES)
          if form.is_valid():
            form.save()
            return redirect('channels')
    else:
            form = ChannelForm()
    return render(request, template_name, {'form':form})


#def channel_insert_view(request):
#    if request.method == 'POST':
#        user = request.POST['user']
#        title = request.POST['title']
#        link = request.POST['link']
#        description = request.POST['description']
#        start_date = request.POST['start_date']
#        icon = request.POST['icon']
#        banner = request.POST['banner']
#        video = request.POST['video']
#        category = request.POST['category']
#        status = request.POST['status']
#        tag = request.POST['tag']
#        channel = Channel.objects.create(user=user, title=title, link=link, description=description, start_date=start_date, icon=icon, banner=banner, video=video, category=category, status=status, tag=tag)
#        messages.success(request, 'content record is now inserted!')
#        return redirect('creators')
#    else:
#        context = {
#            'vchannel': 'TheoDavis Mercedes',
#            'vuser' : 'peggy'
#        }    
#        return render(request, 'channels/channel_insert.html')
    

def search_channel_content_view(request):
        #userdetail = User_detail.objects.all().order_by('id')
        keywords = request.GET['keywords']
        cid = request.GET['cid']
        querylist = Content.objects.filter(tag__icontains=keywords,channel_id=cid).order_by('-dateupload').values()
        paginator = Paginator(querylist, 3)
        page = request.GET.get('page')
        paged_querylist = paginator.get_page(page)
        context = {
            'listings': paged_querylist,
            'keywords' : keywords
        }    
        return render(request,"contents/search.html",context )  