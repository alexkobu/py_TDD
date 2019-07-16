from django.shortcuts import render

#home_page = None

def home_page(request):
    #return HttpResponse('<html><title>To-do lists</title></html>')
    return render(request, 'hoem.html')