from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Walterini: Nuevo mensaje de contacto",  # Asunto
                "De: {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),  # Cuerpo
                "no-contestar@inbox.mailtrap.io",  # Origen
                ["lpillaga@gmail.com"],  # Destiono
                reply_to=[email]
            )
            try:
                email.send()
                # Todo fue bienr
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no va bien
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
