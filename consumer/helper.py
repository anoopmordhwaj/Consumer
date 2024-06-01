from django.shortcuts import render



def getadata(request):
    import requests
    r = requests.get('https://api.publicapis.org/entries')
    data = r.json()
    params = {"data" : data}
    return render(request, "index.html", params)


