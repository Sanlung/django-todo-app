from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Note
from .forms import TaskForm, UpdateForm, NoteForm

# Create your views here.
class TaskListView(View):
    """Handles homepage"""
    def get(self, request):
        """Display the todolist.html page with list of tasks"""
        pending_tasks = Task.objects.filter(completed=False).order_by('-id')
        completed_tasks = Task.objects.filter(completed=True).order_by('-id')
        form = TaskForm()

        return render(
            request=request,
            template_name='todolist.html',
            context={
                'pending_tasks': pending_tasks,
                'completed_tasks': completed_tasks,
                'task_form': form,
                }
            )

    def post(self, request):
        """Take form data and create a new task in the todo list"""
        form = TaskForm(request.POST)
        if form.is_valid():
            task_description = form.cleaned_data['description']
            Task.objects.create(description=task_description)

        # Redirect to the todo homepage
        return redirect('todo_list')

class TaskDetailView(View):
    """Handles the details page"""
    def get(self, request, task_id):
        """Display the detail.html page with form to update the task"""
        task = Task.objects.get(id=task_id)
        form = UpdateForm(initial={'description': task.description})

        return render(
            request=request,
            template_name='detail.html',
            context={
                'update_form': form,
                'id': task_id,
                },
        )

    def post(self, request, task_id):
        """Take form data and update, delete or mark complete the specific task"""
        task = Task.objects.filter(id=task_id)
        if 'update' in request.POST:
            form = UpdateForm(request.POST)
            if form.is_valid():
                task_description = form.cleaned_data['description']
                task.update(description=task_description)
        elif 'complete' in request.POST:
            task.update(completed=True)
        elif 'delete' in request.POST:
            task.delete()

        # Redirect to the todo homepage
        return redirect('todo_list')

class NotesView(View):
    """Handles the notes page"""
    def get(self, request):
        """Display the notes.html page with list of notes"""
        notes = Note.objects.all().order_by('id')
        form = NoteForm()

        return render(
            request=request,
            template_name='notes.html',
            context={
                'note_list': notes,
                'note_form': form,
            },
        )

    def post(self, request):
        """Take form data and create or delete a note in the notes list"""
        form = NoteForm(request.POST)
        if form.is_valid():
            note_text = form.cleaned_data['text']
            if 'create' in request.POST:
                Note.objects.create(text=note_text)
            elif 'delete' in request.POST:
                Note.objects.filter(text=note_text).delete()

        # Redirect to the todo homepage
        return redirect('notes')
