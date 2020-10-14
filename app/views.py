from django.shortcuts import render,redirect
import requests

from .forms import Myform
# Create your views here.
def error(request):
    return render(request, 'app/error.html')
    
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=509cf51cb16ac78f31277a78ea7f876f'

    form = Myform()
    city ="Delhi"
    info = "Default City is Delhi,India"

    if request.method== "POST":

        form = Myform(request.POST)
        city = form['name'].value()
        city = city.strip()
        print(city)
        info = None
        if(len(city)==0):
            city = "Delhi"
            info = "Default City is Delhi,India"


    city_weather = requests.get(url.format(city)).json()
    print(city_weather['cod'])
    if(city_weather['cod'] == '404'):
        return redirect('error')



    weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
    print("w",weather)


    context = {'weather' : weather , 'form':form , 'info':info}


    return render(request, 'app/index.html',context)
