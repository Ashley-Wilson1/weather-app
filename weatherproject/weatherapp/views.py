from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
   
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'sheffield'
    
    url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=696cd71a9679e055fc8039459ade9cbc'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyBip8jkFF9W9AMezbWmGfeqh14dw7sGEAs'
    SEARCH_ENGINE_ID = 'b594445ec513343d1'

    
    try:
        query = city + " 1920x1080"
        page = 1
        start = (page - 1) * 10 + 1
        searchType = 'image'
        city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

        data = requests.get(city_url).json()
        count = 1
        search_items = data.get("items")
        image_url = search_items[1]['link']
        data = requests.get(url,PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today
        print(city_url)
        print(image_url)
        
        return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})    
    except:
        exception_occurred = True
        messages.error(request,'entered data is not availible to API')
        day = datetime.date.today

        return render(request,'index.html',{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'sheffield' , 'exception_occurred':exception_occurred })
