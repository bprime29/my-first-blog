# coding=utf-8
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import MyRegistrationForm
from django.template import RequestContext
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def register_old(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = RegisterForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            user = form.cleaned_data['user']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            envoi = True
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = RegisterForm()  # Nous créons un formulaire vide

    return render(request, "register.html", locals())

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args['form'] = MyRegistrationForm()
    print args
    return render(request, 'register.html', args)