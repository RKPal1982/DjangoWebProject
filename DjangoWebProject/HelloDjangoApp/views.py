from django.shortcuts import render
from django.http import HttpResponse


#####-----------For Demo 1--------------------------####
#def index(request):
#    return HttpResponse("Hello, Django!")
#####-----------For Demo 1--------------------------####
########################################################



#####-----------For Demo 2--------------------------####
#from datetime import datetime

#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)
#####-----------For Demo 2--------------------------####
########################################################





#####-----------For Demo 3--------------------------####
from django.shortcuts import render   # Added for this step
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


#####-----------For Demo 3--------------------------####
########################################################