from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views import View
from . import models

# Create your views here.
class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        context = {'resumes': models.Resume.objects.all()}
        return render(request, "resume/resume_list.html", context=context)

class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden
        description = request.POST['description']
        new_resume = models.Resume(author=request.user, description=description)
        new_resume.save()
        return redirect('/home')
