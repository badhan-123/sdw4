from django.shortcuts import render
from . forms import contactForm,PasswordValidationProject
def home(request):
    return render(request,'home.html')

def about(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password= request.POST.get('pass')
        select=request.POST.get('select')
        return render(request, 'about.html',{'email':email, 'pass':password,'select':select})
    else:
        return render(request, 'about.html',{'email':email, 'pass':password,'select':select})

def submit_form(request):
    print(request.POST)
    return render(request, 'form.html')

def DjangoForm(request):
     if request.method=='POST':
         form=contactForm(request.POST,request.FILES)
         if form.is_valid():
             file=form.cleaned_data['file']
             with open('./formapp/upload/' + file.name, 'wb+')as dest:
                 for chunk in file.chunks():
                     dest.write(chunk)
             print(form.cleaned_data)
         return render(request, 'djangoform.html',{'form':form})
     else:
         form=contactForm()
         return render(request, 'djangoform.html',{'form':form})
   
def PasswordValidation(request):
    if request.method=='POST':
        form=PasswordValidationProject(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'djangoform.html',{'form':form})
    else:
         form=PasswordValidationProject()
         return render(request, 'djangoform.html',{'form':form})
   