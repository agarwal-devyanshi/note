from rest_framework import viewsets

# import local data
from .serializer import NotesSerializer
from .models import NotesModel
from django.contrib.auth.views import LoginView
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
	template_name = 'note/login.html'
	fields = ['user','title', 'description']
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('note:index')

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('note:index')
#     template_name = 'note/signup.html'
class SignUpView(FormView):
	template_name = 'note/signup.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url=reverse_lazy('note:index')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(SignUpView, self).form_valid(form)



# class CustomLogoutView(LoginView):
# 	template_name = 'note/login.html'
# 	fields = ['user','title', 'description']
# 	redirect_authenticated_user = True

# 	def get_success_url(self):
# 		return reverse_lazy('note:index')


class IndexView(LoginRequiredMixin,generic.ListView):
	queryset = NotesModel.objects.all()
	template_name = 'note/index.html'

	
	# specify serializer to be used
	serializer_class = NotesSerializer

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = context['object_list'].filter(user = self.request.user)
		return context

class DetailView(LoginRequiredMixin,generic.DetailView):
	queryset = NotesModel.objects.all()
	fields = ['title', 'description']
	template_name = 'note/detail.html'

class CreateView(LoginRequiredMixin,generic.CreateView):
	queryset = NotesModel.objects.all()
	fields = ['user','title', 'description']
	success_url=reverse_lazy('note:index')
	template_name = 'note/create.html'

class UpdateView(LoginRequiredMixin,generic.UpdateView):
	queryset = NotesModel.objects.all()
	fields = ['user','title', 'description']
	success_url=reverse_lazy('note:index')
	template_name = 'note/update.html'

class DeleteView(LoginRequiredMixin,generic.DeleteView):
	queryset = NotesModel.objects.all()
	# success_url=reverse_lazy('note:index')
	template_name = 'note/delete.html'



