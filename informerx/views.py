from django.shortcuts import render

# Create your views here.
def health(request):
    return HttpResponse(PageView.objects.count())
