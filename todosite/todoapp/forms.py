from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Add task', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))

class UpdateForm(forms.Form):
    description = forms.CharField(label='Action', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))

class NoteForm(forms.Form):
    text = forms.CharField(label='Action', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))

class CommentForm(forms.Form):
    content = forms.CharField(label='', max_length=255, widget=forms.Textarea(attrs={'rows': '10', 'cols': '40'}))

class TagForm(forms.Form):
    name = forms.CharField(label='Tag', max_length=30, widget=forms.TextInput(attrs={'size': '30'}))
