from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#This index function displays the latest 5 poll questions, seperated by commas, and in order of publication date

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#Better way to handle the index request,
#This loads the template called 'polls/index.html' and sends it the *context* and *request* in an HTTPRequest
#context is a dictionary that maps variable names to Python objects

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
#Even better way to handle the above
#render() takes the request object as first argument,
#template name as second argument,
#and dictionary as third OPTIONAL argument
#returns an HttpResponse object of the template rendered with the given context

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
#pub_date__lte - lte means "less than or equal to"
                                     
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

#We're using two generic views - ListView and DetailView
#These do what they're named, they display a list of objects and display a detail page for a type of object
#Each view needs to know what model it will be acting on with the model attribute
#DetailView generic view expects the primary key captured in the URL to be called "pk", so we changed "question_id" to "pk"

#By default, the DetailView view uses a template called <app name>/<model name>_detail.html
#For example, "polls/question_detail.html"
#template_name attribute tells Django to use a specific template name instead of the default
#We have to specify the template_name for the results list view
#Same goes for ListView, we renamed that template_name to "polls/index.html"
#We are working with a couple variables, "question" and "latest_question_list"
#ListView wants to autocreate a context variable as "question_list"
#We don't want that, so we override it with the context_object_name attribute = "latest_question_list"


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})
#Try catch for if a question (question's primary key) does not exist, raises 404 error

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
#Better way to handle detail function
#get_object_or_404() takes Django model as first argument, and an arbitrary number of keyword arguments
#passes to the get() function of the model's manager
#raises Http404 if object does not exist
#there is also a get_list_or_404(), works the same but raises 404 if a list is empty

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HTTPResonseRedirect after successfully dealing with POST data
        #This prevents data from being posted twice if the user hits the back button
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
#request.POST is a dictionary-like object that lets you access data by key name
#request.POST['choice'] returns ID of seleced choice as a string
#request.POST values are always strings
#HttpResponseRedirect takes a single argument: a URL to redirect the user to
#Always use HTTPResponseRedirect after successfully dealing with POST data
#the reverse() function is given the name of the view that we want to pass control to and the variable portion of the
#URL pattern that points to that view
#In this case, it will use the URLconf from polls/urls.py
#The reverse() call will return a string like "/polls/3/results" where '3' is the value of the question.id
#This URL will then call the 'results' view to display the final page

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
