from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.quiz.models import Question, Choice      # inserted this line which import our app's models
# now we can write QuerySets how we did in the database API
def index(request):
    # write a QuerySet to retrieve all the Question objects from our database
    questions = Question.objects.all();
    # package the data in a dictionary to pass to the template
    context = {
        "questions": questions,
    }
    # sends the response to the client aka renders our index.html template with included data
    return render(request, 'quiz/index.html', context)
def show(request, question_id):
    # get the question based on the question_id passed through the request url pattern
    req_question = Question.objects.get(id=question_id)
    # get the choices that belong to the question
    choices = Choice.objects.all().filter(question=req_question)
    # package the data in a dictionary to pass to the template
    context = {
        "question" : req_question,
        "choices" : choices,
    }
    return render(request, 'quiz/index.html', context)
