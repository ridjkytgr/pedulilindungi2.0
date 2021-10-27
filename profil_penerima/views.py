from django.http import response
from django.http.response import Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from biodata.models import Peserta
from django.core import serializers
from .forms import *

from profil_penerima.models import Message

@login_required(login_url='/auth/login/')
def index(request):
    return HttpResponseRedirect('/profil-penerima/user/' + request.user.username)

def logout_account(request):
    auth_logout(request)
    return HttpResponseRedirect('/auth/login')

def logout_modal(request):
    return render(request, 'logout-modal.html')
    
@login_required(login_url='/auth/login/')
def view_profile(request, usn):

    if request.user.username != usn:
        return HttpResponseForbidden("The Username does not match with yours")

    elif request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseRedirect('/profil-penyedia')
    
    user = User.objects.get(username = request.user.username).profile
    penerima = Peserta.objects.get(superUser = request.user)

    return render(request, 'profile.html', {'user':user, 'penerima':penerima})

@login_required(login_url='/auth/login/')
def get_message(request):
    messageObjs = Message.objects.filter(creator = request.user)

    if messageObjs:
        data = serializers.serialize('json', messageObjs)
        return HttpResponse(data, content_type="application/json")

    response = {
        'id' : -1
    }
    return JsonResponse(response)

@login_required(login_url='/auth/login/')
def create_message(request):
    form = MessageForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        # save the form data to model
        tempMsgObj = form.save(commit=False)
        tempMsgObj.creator = User.objects.get(username = request.user.username)
        tempMsgObj.save()

        # when saved json dump
        response = {
            'url' : '/profil-penerima'
        }
        return JsonResponse(response)
    
    return render(request, 'add-message-modal.html', {'form': form})

@login_required(login_url='/auth/login/')
def delete_message(request, id):
    try:
        note = Message.objects.get(id = id)

        if(request.method == 'POST'):
            note.delete()
            return JsonResponse({'url':'/profil-penerima'})
        
    except Message.DoesNotExist:
        return Http404
    
    return render(request, 'delete-message-modal.html', {'message':note})
