from django.core.mail import EmailMessage
from django.conf import settings

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form =  ContactForm(data=request.POST)
        if contact_form.is_valid():
            form_name = request.POST.get('name', '')
            form_email = request.POST.get('email', '')
            form_content = request.POST.get('content', '')
            #si el formulario se envio correctamente se envia un ok

            # Envio de correo con los datos del formulario
            subject = 'Mensaje recibido'
            message = 'De {} <{}> envió el siguiente mensaje:\n\t"{}."'.format(form_name, form_email, form_content)
            email_from = form_email
            recipient_list = [settings.EMAIL_HOST_USER,]
            correo = EmailMessage( subject, message, email_from, recipient_list, reply_to=[form_email])
            
            try:
                correo.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?error')

    return render(request, "contact/contact.html", {'form': contact_form})
