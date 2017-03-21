from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    form=ContactForm()

    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            message=request.POST.get('message', '')

	    Contact.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'], message=form.cleaned_data['message'])
            
        return redirect('index')
    else:
        #form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def showdata(request):
    all_contact = Contact.objects.all()
    return render(request, 'showdata.html', {'all_contact': all_contact})
