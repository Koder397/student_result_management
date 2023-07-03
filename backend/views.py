from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from backend.models import Student


def dashboard(request):
    return render(request, "backend/dashboard.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('hello')
            return redirect('dashboard')
        else:
            messages.error(request, "Please enter valid login details")
            return render(request, "backend/login.html")
    return render(request, "backend/login.html")


def staff_logout(request):
    logout(request)
    return redirect('staff_login')


class TaskList(ListView):
    model = Student

    template_name = "backend/tables/table.html"


class TaskCreate(CreateView):
    model = Student

    template_name = "backend/tables/create.html"

    fields = "__all__"

    success_url = reverse_lazy('task_list')


class TaskUpdate(UpdateView):
    model = Student

    template_name = "backend/tables/update.html"

    fields = "__all__"

    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TaskDelete(DeleteView):
    model = Student

    template_name = "backend/tables/delete.html"

    success_url = reverse_lazy('task_list')
