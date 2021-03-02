from django.shortcuts import render

def index (request):
    return render(request, 'RestaurantApp/index.html',{})

def ReserveView(request):
    if request.method == "POST":
	    name = request.POST['name']
	    how_many = request.POST['many']
	    task_datetime = request.POST['task-datetime']
			if form.is_valid():
				form.save()
	    return render(request , 'RestaurantApp/reservation.html',{'task-datetime': task_datetime})
    else:
	    return render(request, 'RestaurantApp/reservation.html',{})
 