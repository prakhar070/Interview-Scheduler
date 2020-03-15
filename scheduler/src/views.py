from django.forms import ValidationError
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import Interview, Candidate
from .forms import InterviewForm
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#view corresponding to the URL Pattern /scheduler/home
class IndexView(LoginRequiredMixin,ListView):
	template_name = 'main/index.html'
	model = Interview

	#function to fetch the queryset
	def get_queryset(self):
		queryset = Interview.objects.filter(created_by=self.request.user)
		return queryset

#view corresponding to the URL Pattern /scheduler/create
class CreateInterview(LoginRequiredMixin, CreateView):
    #python method corresponding to a get request
    def get(self, request, *args, **kwargs):
        context = {'form': InterviewForm()}
        return render(request, 'main/create.html', context)

    #python method corresponding to a post request
    def post(self, request, *args, **kwargs):
        form = InterviewForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The form is valid.')
            interview = Interview()
            interview.start = request.POST.get('start')
            interview.end = request.POST.get('end')
            interview.created_by = request.user
            interview.save()
            candidates_set = Candidate.objects.filter(id__in = request.POST.getlist('candidates'))
            for candidate in candidates_set:
            	print("candidates are :",candidate)
            	interview.candidates.add(candidate)
            interview.save()
            return redirect(to = reverse('home'))
        else:
            messages.error(request, 'The form is invalid.')
            return render(request, 'main/create.html', {'form': form})

#view corresponding to the URL Pattern /scheduler/edit/<int:id>/
class EditInterview(LoginRequiredMixin, CreateView):
    #python method corresponding to a get request
    def get(self, request, *args, **kwargs):
        interview = Interview.objects.get(id=self.kwargs['interview_id'])
        context = {'form': InterviewForm(initial={'start':interview.start,'end':interview.end,'candidates':interview.candidates.all()})}
        return render(request, 'main/edit.html', context)
   #python method corresponding to a post request
    def post(self, request, *args, **kwargs):
        form = InterviewForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The form is valid.')
            interview = Interview.objects.get(id=self.kwargs['interview_id'])
            interview.start = request.POST.get('start')
            print("start val is ", interview.start)

            interview.end = request.POST.get('end')
            print("start val is ", interview.end)
            interview.created_by = request.user
            interview.save()
            interview.candidates.set(request.POST.getlist('candidates'))
            return redirect(to = reverse('home'))
        else:
            messages.error(request, 'The form is invalid.')
            return render(request, 'main/edit.html', {'form': form})


