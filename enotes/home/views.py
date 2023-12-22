from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from authh.models import *
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    user = request.user
    try:
        signup = Signup.objects.get(user=user)
        totalnotes = Notes.objects.filter(signup=signup).count()
    except Signup.DoesNotExist:
        # Handle the case where Signup does not exist for the user
        signup = None
        totalnotes = 0

    notes = Notes.objects.filter(publish=True)

    return render(request, 'dashboard.html', locals())

def addNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    error = ""
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']
        
        try:
            Notes.objects.create(signup=signup, Title=title, Content=content)
            print()
            error = "no"
        except:
            error = "yes"
    return render(request, 'addNotes.html', locals())

def viewNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    notes = Notes.objects.filter(signup=signup)
    return render(request, 'viewNotes.html', locals())

def editNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        notes.Title = title
        notes.Content = content

        try:
            notes.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotes.html', locals())

def deleteNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewNotes')


def publish_note(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    note = get_object_or_404(Notes, id=pid)
    note.publish = True
    note.save()

    return redirect('viewNotes')

def unpublish_note(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    note = get_object_or_404(Notes, id=pid)
    note.publish = False
    note.save()

    return redirect('viewNotes')





 