from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, GenerateRoomForm
from .models import Record, Room, Message
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

def home(req):
    records = Record.objects.all()
    #Check to see if logging in
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        #Authenticate 
        user = authenticate(req, username=username, password=password)
       
        if user is not None:
            login(req, user)
            messages.success(req, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(req, "There was an error logging in, please try again..")
            return redirect('home')
    else: 
        return render(req, 'home.html', {'records':records})


def logout_user(req):
    logout(req)
    messages.success(req, "You Have Been Logged Out...")
    return redirect('home')


def register_user(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "You Have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(req, 'register.html', {'form':form})
    return render(req, 'register.html', {'form':form})

def customer_record(req, pk):
    if req.user.is_authenticated:
        #Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(req, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(req, "You Do Not Have Access To This Page...")
        return redirect('home')
    
def delete_record(req, pk):
    if req.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(req, "Record Deleted...")
        return redirect('home')
    else:
        messages.success(req, "You Must Be Logged In To Do That..")
        return redirect('home')

def add_record(req):
    form = AddRecordForm(req.POST or None)
    if req.user.is_authenticated:
        if req.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(req, "Record Added...")
                return redirect('home')
        return render(req, 'add_record.html', {'form':form})
    else:
        messages.success(req, "You Do Not Have Access To This Page...")
        return redirect('home')

def update_record(req, pk):
    if req.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(req.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(req, "Record Has Been Updated...")
            return redirect('home')
        return render(req, 'update_record.html', {'form':form})
    else:
        messages.success(req, "You Do Not Have Access To This Page...")
        return redirect('home')

def generate_room(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = GenerateRoomForm(req.POST)
            if form.is_valid():
                form.save()
                room = form.cleaned_data['room']
                user = form.cleaned_data['user']
                messages.success(req, "You Have Successfully Generated A New Chat Room!!")
                return redirect('room')
        else:
            form = GenerateRoomForm()
        return render(req, 'generate_room.html', {'form':form})
    else:
        messages.success(req, "You Do Not Have Access To This Page...")
        return redirect('home')

 
def room(req, room):
    username = req.GET.get('user')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        new_room = Room.objects.create(name=room)
        new_room.save()
        room_details = new_room

    return render(req, 'room.html', {
        'user': username,
        'room': room,
        'room_details': room_details
    })
# def checkview(req):
#     room = req.POST['room']
#     user = req.POST['user']

    
def send(req):
    message = req.POST['message']
    username = req.POST['username']
    room_id = req.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id, created_at=timezone.now())
    new_message.save()
    return HttpResponse("Message sent successfully!")

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


