'''
This is where we gather the information we need to send back a proper response.

Django views are Python functions that takes http requests and returns http response, 
like HTML documents.
A web page that uses Django is full of views with different tasks and missions.
Views are usually put in a file called views.py located on your app's folder.
'''

# Take http requests and returns http response 


from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore
from .models import Member

def members(request):
    '''
    template = loader.get_template('myfirst.html')
    # return HttpResponse("Hello World!")
    return HttpResponse(template.render())
    '''
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


