from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, "course/index.html", {'courses': courses})

def detail(request, slug=None):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "course/detail.html", {'course': course})
    