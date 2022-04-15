from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Add task', max_length=255)

class UpdateForm(forms.Form):
    description = forms.CharField(label='Update task', max_length=255)

class NoteForm(forms.Form):
    text = forms.CharField(label='Add/Remove note', max_length=255)
