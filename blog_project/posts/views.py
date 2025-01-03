from django.shortcuts import render,redirect
from . import forms
from posts.models import Post

# Create your views here.
def add_post(request):
     if request.method=='POST':
        post_form=forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
        return redirect('add_post')
     else:
         post_form=forms.PostForm()
         return render(request,'add_post.html',{'form':post_form})
    
    
def home(request):
    data=Post.objects.all()
    print(data)
    return render(request, 'home.html')