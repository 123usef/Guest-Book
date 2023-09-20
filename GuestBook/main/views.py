from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import Comment
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments':comments}
    return render( request, 'main\index.html' , context)


def signin(request):
    if (request.method == 'POST'):
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            comment = request.POST['comment']
            newComment = Comment(name = name ,comment = comment )
            newComment.save()
            return redirect('home')
    else:        
        form = CommentForm()
    context ={
        'form':form,
    }
    return render( request, 'main\signin.html' , context)