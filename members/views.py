from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import loginForm

class Login(View):
    form = loginForm
    template = 'login.html'

    def get(self, request):
        return render(request, self.template, {'loginForm': self.form()})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/artists/create')
        else:
            messages.success(request, 'Wrong username or password, Please try again.')
            return redirect('/login_page')