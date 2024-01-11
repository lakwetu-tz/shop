from django.shortcuts import render
from product.models import *

# Create your views here.
def home(request):
    # categories = Category.objects.all().filter(top)
    return render(request, 'core/index.html')


def webadmin(request):
    return render(request, 'webadmin/index.html')
