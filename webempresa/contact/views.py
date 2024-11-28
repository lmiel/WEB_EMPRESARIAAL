from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            
            email = EmailMessage(
                'La Caffetiera: Nuevo mensaje de contacto',
                'Mensaje enviado de {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                email,
                ['8b296439d55f89@inbox.mailtrap.io'],
            )
            
            try:
                email.send()  
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
            
        
        
    return render(request, "contact/contact.html", {'form':contact_form})