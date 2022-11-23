from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'susmitha'}
    return render(request,'jinja.html',d)