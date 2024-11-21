from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Category
from .forms import CategoryForm

# Create your views here.
def index(request):
    page_name = "Products Page"
    page_content = "Welcome to FreshCart Download the app get free food & $30 off on your first order."
    context = {
        "page_name": page_name,
        "page_content": page_content
    }
    return render(request, "products/index.html", context)

def category_list(request):
    page_name = "Product category list page"
    categories = Category.objects.all()
    context = {
        "page_name": page_name,
        "categories": categories
    }
    return render(request, "products/category_list.html", context)

def category_create(request):
    page_name = "Product category creation page"

    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect("product_category_list")
    context = {
        "page_name": page_name,
        "form": form
    }
    return render(request, "products/category_create.html", context)
