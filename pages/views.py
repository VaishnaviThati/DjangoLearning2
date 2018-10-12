from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, "home.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")

def about_view(request, *args, **kwargs):
    my_context = {

                    "my_text" : "This is about ",
                    "this_is_true" : True,
                    "my_num" : 123,
                    "my_list" : [1234,2432,3765,"Abc"] ,
                    "my_context" : "<h1>Hello World</h1>"

                 }
    #return render(request, "about.html", {})
    return render(request, "about.html", my_context)
