from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.core.mail import send_mail
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # subject = "Contact Form Submission"
            # message = f"Name: {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}\nEmail: {form.cleaned_data['email_address']}\nMessage: {form.cleaned_data['message']}"
            pass
            # return redirect("homepage")  # Assuming 'home' is the name of your homepage URL
    else:
        form = ExampleForm()

    return render(request, "home.html", {'form': form})


# views.py
from django.shortcuts import render
from .models import MyModel

def my_view(request):
    my_objects = MyModel.objects.all()
    return render(request, 'second.html', {'my_objects': my_objects})
