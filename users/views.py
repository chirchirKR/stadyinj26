from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from posts.models import Post,Announcement
from django.http import JsonResponse
# Create your views here.

def Dashboard(request):
    tmp = "users/dashboard.html"
    posts = Post.objects.order_by('-posted_at')
    announs = Announcement.objects.order_by('-edited_at')
    ans = list()
    for a in announs:
        if a.read_by.filter(id=request.user.id):
            ans.append(a.id)
    numOfAns = announs.count()        

    return render(request, tmp, {"posts": posts, "num_of_announcements": numOfAns, "unread": numOfAns - len(ans), "length_": len(ans)})
    
def AnnouncementView(request):
    tmp = 'users/announcement.html'
    announs = Announcement.objects.order_by('-edited_at')
    ans = list()
    for a in announs:
        if a.read_by.filter(id=request.user.id):
            ans.append(a.id)
    numOfAns = announs.count()        
    #announcement = Announcement.objects.read_by.filter(id=request.user.id)
    #is_read = announs.read_by.filter(id=request.user.id).exists()
    return render(request, tmp, {"notifs": announs, "read_notifs": ans, "num_of_announcements": numOfAns, "unread": numOfAns - len(ans), "length_": len(ans)})
    
def SignUp(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    tmp = 'register/signup.html'
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
            
    else:
        form = UserCreationForm()
        
    return render(request, tmp, {'form': form})
        
def ReadNotif(request, notifid):
    if request.method == "POST":
        announce = Announcement.objects.get(id=notifid)
        announce.read_by.add(request.user)
        announce.save()
        
        return JsonResponse({"status": "read"})