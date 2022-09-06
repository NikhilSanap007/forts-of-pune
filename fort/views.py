from django.shortcuts import render
from .models import fort
#from cart.cart import Cart

# Create your views here.

def index(request):
    return render(request,'index.html')

def forts(request):
    kille = fort.objects.all()
    return render(request,'fort.html', {'kille': kille})

def fort_detail(request, pk):
    killa = fort.objects.get(f_id=pk)
    return render(request,'fort-detail.html', {'killa':killa})

