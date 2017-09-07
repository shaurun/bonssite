from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.template.context_processors import csrf

from django.contrib import auth
from bonssite.models import Section, Article

sections = Section.objects.all();

def home(request):
    context = {
        'sections': sections,
        'user': auth.get_user(request)
    }
    return render(request, "bonssite/home.html", context);

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id);
    context = {
        'sections': sections,
        'article' : article,
        'user': auth.get_user(request)
    }
    return render(request, "bonssite/article.html", context);


def login(request):
    args = {};
    args.update(csrf(request));
    if (request.POST):
        username = request.POST.get('username', '');
        password = request.POST.get('password', '');
        args['username'] = username;
        args['password'] = password;
        if (username == '' or password == ''):
            args['login_error'] = "Заполните имя пользователя и пароль";
            return render(request, "bonssite/home.html", args);
        else:
            if (request.POST.get('action') == "Регистрация"):
                if (User.objects.filter(username=username).exists()):
                    args['login_error'] = "Пользователь с таким именем уже существует.";
                    return render(request, "bonssite/home.html", args);
                user = User.objects.create_user(username=username, password=password);
            elif (request.POST.get('action') == "Вход"):
                user = auth.authenticate(username=username, password=password);

            if (user is not None):
                auth.login(request, user);
                return redirect("/");
            else:
                args['login_error'] = "Пользователь не найден.";
                return render(request, "bonssite/home.html", args);

def logout(request):
    auth.logout(request);
    return redirect("/");

def register(request):
    args = {};
    args.update(csrf(request));
    args['form'] = UserCreationForm();
    if (request.POST):
        new_user_form = UserCreationForm(request.POST);
        if (new_user_form.is_valid()):
            new_user_form.save();
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2']);
            auth.login(request, new_user);
            return redirect("/");
        else:
            args['form'] = new_user_form;
    return render(request, "bonssite/register.html", args);


def newspaper(request):
    sections = Section.objects.all();
    context = {
        'sections': sections,
        'user': auth.get_user(request)
    }
    return render(request, "bonssite/newspaper.html", context);