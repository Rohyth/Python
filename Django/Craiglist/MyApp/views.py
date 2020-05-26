from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import urllib.parse
from . import models

Base_url = 'https://delhi.craigslist.org/search/bbb?query={}'


def home(request):
    return render(request, 'Base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    final_url = Base_url.format(urllib.parse.quote(search))

    response = requests.get(final_url)
    data = response.text
    s1 = BeautifulSoup(data, 'html.parser')

    results = s1.find_all('li', {'class': 'result-row'})

    final_list = []
    for post in results:
        post_title = post.find(class_='result-title').text
        post_url = post.find(class_='result-title').href

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        print(post_title, post_url, post_price)

    data_for_frontend = {
        'search': search,
    }

    return render(request, 'index.html', data_for_frontend)
