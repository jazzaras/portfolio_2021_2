from django.http import HttpResponse
from django.shortcuts import render
import operator
import smtplib
import os
from twilio.rest import Client

account_sid = 'ACd99ba11144b289bc7fa12e3bda8b7e4f'
auth_token  = 'b476929dc6662e901c4beb928f6f34ea'

client = Client(account_sid, auth_token)


def contact(request):
	return render(request, 'contact.html')

def thanks(request):
	email = request.GET['email']
	name = request.GET['name']
	message = request.GET['message']
	
	from_whatsapp_number = 'whatsapp:+14155238886'
	to_whatsapp_number = 'whatsapp:+966536546711'
	client.messages.create(
		body=f'FROM : {email} \n NAME : {name} \n MESSAGE : (\n {message}\n)',
		from_=from_whatsapp_number,
		to=to_whatsapp_number)

	return render(request, 'thx.html')