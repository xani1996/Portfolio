from django.shortcuts import render, redirect
from .models import Home, About, Profile, Category, Skills, Portfolio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def index(request):
    # Home
    home = Home.objects.latest('updated')
    # # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'from portfolio'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'rashidixaniar@gmil.com', ['rashidixaniar@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Somethings wrong')
            return HttpResponse('your Email sens successfully')
    form = ContactForm
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'form': form
    }
    return render(request, 'index.html', context)
