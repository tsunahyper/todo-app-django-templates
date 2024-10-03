from django.shortcuts import render,redirect
from .models import Todo
import logging
logger = logging.getLogger(__name__)

from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy # To redirect the user to another page

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # A plugin that restrict users from accessing any other functionality or pages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # A plugin that login the user directly upon creation successfully

# Using Viewsets as a way for doing CRUD operations via API requests.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView

# Register View
class Register(FormView):
    template_name = 'api/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True # if user is already logged in, redirect him to the home page
    success_url = reverse_lazy('todo') # redirect to todo list after login

    # Once form is submitted and valid, user will be logged in
    def form_valid(self, form):
        logger.info("Form valid, user is being created")
        user = form.save()
        if user is not None:
            login(self.request, user) # login the user directly upon creation successfully
        return super(Register,self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo')
        return super(Register,self).get(request, *args, **kwargs)

# Login View
class CustomLogin(LoginView):
    template_name = 'api/login.html'
    fields = '__all__' # portray all fields for the forms
    redirect_authenticated_user = True # if user is already logged in, redirect him to the home page

    def get_success_url(self):
        return reverse_lazy('todo') # redirect to todo list after login

# Get Todo List
class ListTodo(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todo' # to replace the context object name in html from object_list to any name by user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = (str(self.request.user)).upper() # pass the user to html templates to be rendered
        context['todo'] = context['todo'].filter(user=self.request.user) # filter out the context data only for the current user
        context['count'] = context['todo'].filter(complete=False).count() 

        search_input = self.request.GET.get('search-area')
        if search_input:
            context['todo'] = context['todo'].filter(title__icontains=search_input)

        context['search_input'] = search_input # pass the search input to html templates to be rendered
        return context

# View Todo List
class DetailTodo(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'detail' # to replace the context object name in html from object_list to any name by user
    template_name = 'api/todo_detail.html' # to replace the templates file name in templates folder 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all todos for the specific user and primary key (pk)
        fetch_all = Todo.objects.filter(user=self.request.user, pk=self.kwargs['pk'])
        # print(fetch_all)
        for i in fetch_all:
            print(i.complete)
        context['title'] = (str(([_.title for _ in fetch_all])[0])).upper()  # Passing the QuerySet to the template
        context['description'] = str(([_.description for _ in fetch_all if _])[0])# Passing the QuerySet to the template
        context['complete'] = (str(([_.complete for _ in fetch_all])[0])).upper()  # Passing the QuerySet to the template
        
        return context


# Create Todo List
class CreateTask(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title','description','complete'] # portray all fields for the forms
    success_url = reverse_lazy('todo') # to redirect the user to another page after creating a new task, 'todo' naming convention comes from the urls context name

    # create a secluded forms for current user to create a new task under their own user
    def form_valid(self, form: BaseModelForm) -> HttpResponse: 
        # assign the currently logged-in user to the 'user' field of the form instance.
        form.instance.user = self.request.user  
        # call the superclass's form_valid method to proceed with the standard processing (such as saving the form and redirecting to a success URL).
        return super(CreateTask, self).form_valid(form)

# Update Todo List
class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__' # portray all fields for the forms
    success_url = reverse_lazy('todo') # to redirect the user to another page after creating a new task, 'todo' naming convention comes from the urls context name


# Delete Todo List
class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo' # to replace the context object name in html from object_list to any name by user
    template_name = 'api/todo_confirm_delete.html' # to replace the templates file name in templates folder 
    success_url = reverse_lazy('todo') # to redirect the user to another page after creating a new task, 'todo' naming convention comes from the urls context name