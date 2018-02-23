from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! this is forst page form Django")