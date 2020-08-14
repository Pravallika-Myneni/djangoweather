from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode=request.POST['zipcode']
        #return render(request,'home.html',{'zipcode': zipcode})
        api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=7E923556-A184-462F-92C5-8A1892197430")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api=" "
        if api[0]['Category']['Name']=='Good':
            category_color="good"
        elif api[0]['Category']['Name']=="Moderate":
            category_color="mod"
        elif api[0]['Category']['Name']=='Unhealthy for Sensitive Groups':
            category_color="usg"
        elif api[0]['Category']['Name']=='Unhealthy':
            category_color="unh"
        elif api[0]['Category']['Name']=='Very Unhealthy':
            category_color="vuh"
        elif api[0]['Category']['Name']=='Hazardous':
            category_color="haz"
        return render(request,'home.html',{'api': api,'category_color' : category_color})
    else:
        api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=7E923556-A184-462F-92C5-8A1892197430")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api=" "
        if api[0]['Category']['Name']=='Good':
            category_color="good"
        elif api[0]['Category']['Name']=="Moderate":
            category_color="mod"
        elif api[0]['Category']['Name']=='Unhealthy for Sensitive Groups':
            category_color="usg"
        elif api[0]['Category']['Name']=='Unhealthy':
            category_color="unh"
        elif api[0]['Category']['Name']=='Very Unhealthy':
            category_color="vuh"
        elif api[0]['Category']['Name']=='Hazardous':
            category_color="haz"
        return render(request,'home.html',{'api': api,'category_color' : category_color})

def about(request):
    return render(request,'about.html',{})
