from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Vacancy

# Create your views here.
class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancies': Vacancy.objects.all()}
        return render(request, "vacancy/vacancy_list.html", context=context)

class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponse(status=403)
        if not request.user.is_authenticated:
            return HttpResponse(status=403)
        description = request.POST['description']
        new_vacancy = Vacancy(author=request.user, description=description)
        new_vacancy.save()
        return redirect('/home')