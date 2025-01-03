from django.shortcuts import render
from app_7.forms import StudentForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save(commit=False)
            print(form.cleaned_data)
        return render(request, 'home.html',{'form':form})
    else:
         form=StudentForm()
         return render(request, 'home.html',{'form':form})
