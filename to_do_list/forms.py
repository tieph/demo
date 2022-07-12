from django import forms
from .models import ToDo
from django.contrib.admin.widgets import AdminDateWidget

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'status', 'due_date']

    def clean_title(self):
        if self.cleaned_data['title'][0].isalpha():
            split_title = self.cleaned_data['title'].split()
            first_word = split_title[0].capitalize()
            other_words = " ".join(split_title[1:])
            return first_word + " " + other_words
        else:
            return self.cleaned_data['title']