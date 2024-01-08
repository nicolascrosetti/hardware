from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Listing, Category, Message, User

def index(request):
    return render(request, "hardware/index.html", {
        "listings": Listing.objects.all(),
    })
def category(request, category_name):
    category = Category.objects.get(categoryName = category_name)
    listings = category.listings.all()
    return render(request, "hardware/index.html", {
        "listings": listings,
    })

@login_required(login_url='/login')
def search(request):
    if request.method == "POST":
        query = request.POST['query']
        url = reverse("search_query", kwargs={ 'query': query })
        return HttpResponseRedirect(url)

def search_query(request, query):
    listings = Listing.objects.filter(title__icontains=query)
    if len(listings) >= 1:
        return render(request, "hardware/index.html", {
            "listings": listings,
        })
    else:
        return render(request, "hardware/index.html", {
            "listings": listings,
            "message": "No hay productos que coincidan con su busqueda."
        })

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        message_content = request.POST["message"] 

        # Verifica que el mail sea valido
        try:
            validate_email(mail)
        except ValidationError:
            return render(request, "hardware/contact.html", {
                "message": "El email no es valido.",
                "error": True
            })

        message = Message(name=name, mail=mail, message=message_content)
        message.save()  
        return render(request, "hardware/contact.html", {
                "message": "Mensaje enviado exitosamente!"
        })
    
    return render(request, "hardware/contact.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Verifica que se haya logueado correctamente
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hardware/login.html", {
                "message": "Nombre de usuario y/o contraseña incorrecto."
            })
    else:
        return render(request, "hardware/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Verifica que las contraseñas coincidan
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hardware/signup.html", {
                "message": "Las contraseñas no coinciden."
            })
        # Verifica que el mail sea valido
        try:
            validate_email(email)
        except ValidationError:
            return render(request, "hardware/signup.html", {
                "message": "El email no es valido."
            })
        # Crea nuevo usuario
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hardware/signup.html", {
                "message": "El nombre de usuario ya existe."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hardware/signup.html")

