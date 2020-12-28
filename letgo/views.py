from django.http import HttpResponse

from django.shortcuts import render

from letgo.models import imggal
from letgo.models import about
from letgo.models import Contact

from letgo.models import  Ourservice, homedesc


from django.contrib import messages

import sys

from django.utils.datastructures import MultiValueDictKeyError

from django.db.utils import ProgrammingError

# Create your views here.


def index(request):
    Hdesc = homedesc.objects.all()

    Ab = about.objects.all()
    
  
    Ser = Ourservice.objects.all()


    
   

    return render(request,'index.html', {'Ourservice': Ser, 'homedesc': Hdesc, 'about': Ab})
    


    


def aboutus(request):
    img = imggal.objects.all()

    Ab = about.objects.all()
    return render(request,'aboutus.html',{'imggal': img, 'about': Ab})

def contact(request):
    #messages.success(request, 'Welcome to contact')
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        print(name, phone, email, message)
        
        if len(name)<2 or len(phone)<10 or len(email)<4  or len(message)<5:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name = name, phone = phone, email = email, message = message)
            contact.save()
            messages.success(request, "your message have been sucessfully Sent")

    return render(request,'contact.html')

def search(request): 
    query = request.POST.get('query', True)
    if 'query' in request.POST:
        query = request.POST['query']
    else:
        query = False
    #query = request.POST['query']
    #if(len(sys.argv) == 3):
    #if int(len (query) > 200):
    if len('query') > 200|len('query') == '':
        all = []

    else:
        all = imggal.objects.filter(imgtitle__icontains = query)
        params = {'all':all,'query': query}
   
    try:
        query = request.POST['query',False]
    except MultiValueDictKeyError:
        query = False
    return render(request,'search.html',params)

#def imagedisplay(request):
   # resultsdisplay = imggal.add_to_class.objects.all('imggal')
    #return render(request,'aboutus.html',{'imggal':resultsdisplay})


