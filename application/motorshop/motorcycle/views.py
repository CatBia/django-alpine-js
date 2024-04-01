from django.shortcuts import render
from motorcycle.models import Brands, Motorcycles

# Create your views here.

def brands_list(request):
    all_brands = list(Brands.objects.all().values('brand_name', 'brand_desc', 'brand_logo'))
    return render(request, 'brands.html', {'brands': all_brands})
