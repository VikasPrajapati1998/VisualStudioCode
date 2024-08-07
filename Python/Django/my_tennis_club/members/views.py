'''
This is where we gather the information we need to send back a proper response.

Django views are Python functions that takes http requests and returns http response, 
like HTML documents.
A web page that uses Django is full of views with different tasks and missions.
Views are usually put in a file called views.py located on your app's folder.
'''

# Take http requests and returns http response 


from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


