from django.shortcuts import render
from .models import ReserveTable
from .models import Food
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


