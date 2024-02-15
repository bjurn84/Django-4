from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponseRedirect

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})