from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')  # Renders the home page with a "Send Email" button

def send_email(request):
    if request.method == 'POST':
        send_mail(
            'Welcome Party - reg.',
            'Greetings!!! Welcome to the Department of Information Technology.',
            settings.EMAIL_HOST_USER,
            ['22uit054@kamarajengg.edu.in'],
            fail_silently=False,
        )
        return render(request, 'sendMail.html', {'message': 'Email has been sent successfully!'})
    return redirect('home')  # Redirect to home if the request method isn't POST
