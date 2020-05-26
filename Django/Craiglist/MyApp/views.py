from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import urllib.parse
from .models import Search

Base_url = 'https://delhi.craigslist.org/search/bbb?query={}'


def home(request):
    return render(request, 'Base.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    #final_url = urllib.parse.quote(Base_url) + urllib.parse.quote(search) 
    final_url = Base_url.format(urllib.parse.quote(search))
    #print(final_url)
    response = requests.get(final_url)
    data = response.text
    s1 = BeautifulSoup(data,'html.parser')

    results = s1.find_all('li',{'class':'result-row'})
    
    #post_titles = results.find('a',{'class':'result-title hdrlnk'}) 
    #post_images = results.find('a',{'class':'result-image gallery'})
    #print(post_images[0])
    print()
    print(results[0])

    data_for_frontend = {
        'search': search,
    }
    return render(request, 'index.html', data_for_frontend)
