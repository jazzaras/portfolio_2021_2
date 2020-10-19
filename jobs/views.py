from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'jobs/home.html')


def aboutme(request):
	return render(request, 'aboutme/aboutme.html')

def resume(request):
	return render(request, 'resume/resume.html')