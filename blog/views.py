from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm
# Create your views here.
def index(arg):
    return HttpResponse("<p>Hello DapJak</p>")

def first_entry(request):
    return render(request, 'blog/hello.html')

def get_name(request):
    if request.method == "POST":
        f = NameForm(request.POST)
        if f.is_valid():
            name=f.save()
            return redirect('blog:get_name')
    else:
        f = NameForm()

    return render(request, 'blog/get_name.html', {'form': f})
