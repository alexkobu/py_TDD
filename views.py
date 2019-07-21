from django.shortcuts import render
from django.http import HttpResponse

#home_page = None

def home_page(request):
    # if request.method == 'POST':
        # return HttpResponse(request.POST['item_text'])
    #return HttpResponse('<html><title>To-do lists</title></html>')
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })