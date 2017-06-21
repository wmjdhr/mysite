from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name="personal/home.html")

def contact(request):
    return render(request, template_name="personal/basic.html",
                  context={'contact': ['Wanna contact?', 'wmjdhr@sina.com']})
