from django.shortcuts import render, HttpResponse, redirect
import string
import random

# Create your views here.

def index(request):

    my_string = {
        'string':''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(14))
    }

    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1

    return render(request, 'first_app/index.html', my_string)
    #this connects views to your html/template file.
