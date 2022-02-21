from asyncio.format_helpers import extract_stack
from re import template
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import AddPostForm


from .models import Post, User
from django.views.generic import CreateView, DetailView, ListView


""" def index(request):
    return render(request, "network/index.html") """


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

class NetworkHome(ListView):
    model = Post
    template_name = "network/index.html"
    # указать переменную 'posts', для того чтобы именно ее использовать в шаблоне index
    # а не object_list(стандартная переменная для отображения контекста в шаблоне) 
    context_object_name = 'posts'

    # ф-ция для передачи динамического и статического контекста
    def get_context_data(self, *, object_list=None, **kwargs):
        # берем контекст базового класса (context_object_name = 'posts')
        context=super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context


class ShowPost(DetailView):
    model = Post
    template_name = 'network/post.html'
    pk_url_kwarg = 'post_pk' # указать параметр маршрута 'post_pk'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = "network/add_post.html"
    success_url = reverse_lazy('index')
