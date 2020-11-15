from django import forms
from .models import Question, Choice

class PollAddForm(forms.ModelForm):

    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice3 = forms.CharField(label='Choice 3', max_length=100, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    

    class Meta:
        model = Question
        fields = ['question_text', 'choice1', 'choice2', 'choice3','pub_date']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }

class EditPollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', ]
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }

class ChoiceAddForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', })
        }