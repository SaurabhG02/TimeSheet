from django.shortcuts import render
from .forms import TimeSheetForm
from django.views import generic

# Create your views here.
def home(request):
    print(request.method)
    print(request.POST)
    if request.method == "GET":
        form = TimeSheetForm()
        return render(request, 'home.html', {'form':form})
    else:
        form = TimeSheetForm(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'form':form})
        else:
            # print(form.errors)
            return render(request, 'home.html', {'form':form})
