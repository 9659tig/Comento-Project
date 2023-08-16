from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm

def signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(req, 'accounts/signup.html', {'form': form})
