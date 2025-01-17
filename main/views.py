from django.core.checks import messages
from django.shortcuts import redirect, render

from main.models import Questions, Discussion
from .forms import NewQuestion, NewResponse, NewReply
from django.http import response, JsonResponse
from django.core import serializers
from django.http.response import HttpResponse
from account.models import Profile


def home(request):
    questions = Questions.objects.all().order_by("-created_at")
    context = {'questions' : questions}

    if request.user.is_authenticated : 
        context["user"] = request.user
        form = NewQuestion(request.POST or None)

        # post form with ajax
        if request.is_ajax() : 
            person = Profile.objects.get(user=request.user)
            form = NewQuestion(request.POST or None)
            if form.is_valid():
                questions = form.save(commit=False)
                questions.author = person
                questions.save()
                return JsonResponse({
                    'msg': 'Success'
                })

        context['form'] = form

        # rendering homepage based on user's role
        person = Profile.objects.get(user=request.user)
        if person.role == 'penerima' :
            return render(request, 'main/home_penerima.html', context)
        elif person.role == 'penyedia' :
            return render(request, 'main/home_penyedia.html', context)
        
    return render(request, 'main/home.html', context)
    

def see_question(request, id) : 
    response_form = NewResponse(request.POST or None)
    reply_form = NewReply(request.POST or None)
    question = Questions.objects.get(id=id)

    # post response
    if request.method == "POST" : 
        try : 
            response_form = NewResponse(request.POST or None)
            person = Profile.objects.get(user=request.user)
            if response_form.is_valid():
                responses = response_form.save(commit=False)
                responses.author = person
                responses.forum = Questions(id=id)
                responses.save()
                return response.HttpResponseRedirect('')
            else : 
                print("error")

            
        except Exception as e:
            print(e)
    

    context = {
        "question" : question,
        "response_form" : response_form,
        "reply_form" : reply_form
    }
    return render(request, "main/detail_question.html", context)


def reply(request) : 

    # post reply
    if request.method == "POST" : 
        try : 
            reply_form = NewReply(request.POST or None)
            if reply_form.is_valid():
                person = Profile.objects.get(user=request.user)
                question_id = request.POST.get("question")
                parent_id = request.POST.get("parent")
                reply = reply_form.save(commit=False)
                reply.author = person
                reply.forum = Questions(id=question_id)
                reply.parent = Discussion(id=parent_id)
                reply.save()
                return response.HttpResponseRedirect('question/' + str(question_id))
            else : 
                print("error")

            
        except Exception as e:
            print(e)
        
    
    return redirect('home')

def json(request) : 
    questions =  Questions.objects.all()
    response = {'questions':questions}
    render(request, 'main/question.json', response)

    data = serializers.serialize('json', Questions.objects.all())
    return HttpResponse(data, content_type="application/json")




