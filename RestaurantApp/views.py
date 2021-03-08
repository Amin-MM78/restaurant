from django.shortcuts import render
from .models import ReserveTable
from .models import Food
from .models import About
from .models import ContactForm
from django.core.mail import send_mail

def index (request):
    return render(request, 'RestaurantApp/index.html',{})

def ReserveView(request):
	if request.method == "POST":
		name = request.POST['name']
		how_many = request.POST['many']
		task_datetime = request.POST['task-datetime']
		ins = ReserveTable(name= name,how_many=how_many, ReserveDateTime=task_datetime)
		ins.save()

		return render(request, 'RestaurantApp/reservation.html',{'task_datetime':task_datetime})
	else:
		return render(request, 'RestaurantApp/reservation.html')

def MenuView(request):
	query = Food.objects.all()
	context ={
		'object_list':query

	}

	return render(request,'RestaurantApp/menu.html',context)

def ContactView(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		inst = ContactForm(name=name,email=email,subject=subject,message=message)
		inst.save()

		"""send_mail(

			name,
			email,
			subject,
			message,
			['aminmalek5@gmail.com']

			)"""
		#sending email
		return render(request,'RestaurantApp/contact.html',{'name' : name})
	else:
		return render(request,'RestaurantApp/contact.html')


def AboutView(request):
	query = About.objects.all()
	context ={
	'object_list':query

	}
	return render(request,'RestaurantApp/about.html',context)



def GalleryView(request):

	return render(request,'RestaurantApp/gallery.html')



