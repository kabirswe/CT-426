from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

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
    paginator = Paginator(categories, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_name": page_name,
        "page_obj": page_obj
    }
    return render(request, "products/category_list.html", context)

def category_detail(request, category_id):
    page_name = "Product category detail page"
    category = Category.objects.get(id=category_id)
    print("=======================================")
    print(category)
    print("=======================================")
    context = {
        "page_name": page_name,
        "category": category
    }
    return render(request, "products/category_detail.html", context)

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

def category_update(request, category_id):
    page_name = "Product category update page"
    category = Category.objects.get(id=category_id)

    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("product_category_list")
    context = {
        "page_name": page_name,
        "form": form
    }
    return render(request, "products/category_create.html", context)

def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect("product_category_list")
