from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.contrib import messages
# Create your views here.
def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		subject = request.POST['subject']
		data = Contact.objects.create(
			name = name,
			email = email,
			message = message,
			subject = subject
			)
		data.save()

		email = EmailMessage(
		    'Contact message from your store',
		    f'Hello admin {name} is trying to contact you. His email is {email}.He wants to talk about {subject}',
		    'aceraayush@gmail.com',
		    ['aceraayush@gmail.com']
		)
		email.send()
		messages.success(request,'Your message is sent')
	return render(request,'contact-us.html')