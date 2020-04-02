from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html',{})#{}-this allows us to pass stuff from front end to back end.

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email =request.POST['message-email']
		message = request.POST['message']

		#Send email
		send_mail(
			message_name,#subject
			message,#message
			message_email,#from email
			['daniilwork247@gmail.com'],#to email
			fail_silently = False,
			)

		return render(request, 'contact.html',{'message_name': message_name})#python dictionary
	else:
		#return the page.
		return render(request, 'contact.html',{})


# Create your views here.
