from django import forms
from .models import Candidate, Interview
from django.forms import ValidationError

#python file for django forms
class InterviewForm(forms.Form):
   
   	#fields for starttime, endtime and candidates present in an interview
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    candidates = forms.ModelMultipleChoiceField(queryset=Candidate.objects.all(),widget=forms.CheckboxSelectMultiple)
    def clean(self):
        super(InterviewForm, self).clean()
        # This method will set the `cleaned_data` attribute
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        candidates = self.cleaned_data.get('candidates')
        interviews = Interview.objects.all()
        if start>=end:
        	msg = 'start time of the interview must be less then the end time'
        	self.add_error('start', msg)
        elif len(candidates)<2:
        	msg = 'minimum number of participants must be 2'
        	self.add_error('candidates', msg)
        else:
	        for candidate in candidates:
	        	for interview in interviews:
	        		if candidate in interview.candidates.all():
	        			low = interview.start
	        			high = interview.end
	        			if low>=start and low<=end:
	        				msg = "{} is busy in another interview ".format(candidate.name)
	        				self.add_error('candidates', msg)
	        			elif start>=low and start<=high:
	        				msg = "{} is busy in another interview ".format(candidate.name)
	        				self.add_error('candidates', msg)

        
