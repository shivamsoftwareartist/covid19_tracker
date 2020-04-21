from django.shortcuts import render
from covid import  Covid


def index(request):
    covid = Covid()
    data = covid.get_data()[:2]
    countries = covid.list_countries()[:5]
    print(countries)
    print(data)
    list = []

    for a in data:
        c_data = a['country']
        list.append(c_data)
    # print(list)
    return render(request, 'index.html',{'data':data,
                                        'countries':countries})