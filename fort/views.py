from django.shortcuts import render, redirect
from .models import fort, Contact_form
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

def contact_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact_form(name=name, email=email, message=message)
        contact.save()
    return redirect('/')