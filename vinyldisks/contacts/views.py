from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def inquiri(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        email = request.POST['email']
        choice = request.POST['choice']
        theme = request.POST['theme']
        text  = request.POST['text']

        if request.user.is_authenticated:
            #userid = request.user.id
            has_contacted = Contact.object.all().filter(user_id = user_id)

            if has_contacted:
                messages.error(request, 'Sorry, but you have already contacted')
                return redirect('/contuctus')
        contact = Contact.objects.create(
                user_id = user_id,
                first_name = first_name,
                email = email,
                choice = choice,
                theme = theme,
                text = text
        )
        contact.save()
        messages.success(request, 'Your request has been submited')
        return redirect('/contactus')