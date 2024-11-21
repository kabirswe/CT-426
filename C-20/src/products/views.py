from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    page_name = "Products Page"
    page_content = "Welcome to FreshCart Download the app get free food & $30 off on your first order."
    context = {
        "page_name": page_name,
        "page_content": page_content
    }
    return render(request, "products/index.html", context)
