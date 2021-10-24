from django.urls import path

from . import views 
from .views import CustomLoginView, SignUpView
from django.contrib.auth.views import LogoutView

app_name = 'note'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'note:login'), name='logout'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/',SignUpView.as_view(), name='signup'),
    # path('register/',RegisterPage.as_view(), name='register'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name = 'delete'),
]


