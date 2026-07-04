from django.http import HttpResponse
# from django.http import Http404 ---> getobject or 404 is shortcut for this
from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.shortcuts import render
from.models import Question


# Create your views here.
# def index(request):
#     return HttpResponse("Hello! You are at the poll index")

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  #--->get the data
    # template = loader.get_template("polls/index.html")
    # output = ", ".join([q.question_text for q in latest_question_list])
    context ={
        "latest_question_list": latest_question_list
    }  #-------------->pack the data
    return render(request, "polls/index.html", context) #----->send it to the template
    #internally django does template(....)-html = temp->return httpresponse(html)
    # return HttpResponse(output)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html",{"question": question})
    question = get_object_or_404(pk=question_id)
    return render(request, "polls/detail.html",{"question": question})




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



