from django.http import *

def main(request):
    return HttpResponse("<h1>Main Home page for user</h1>""This is the main page. This is where we would have our news transmission")
