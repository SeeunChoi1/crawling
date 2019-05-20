from django.shortcuts import render
from time import sleep
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    if request.method == 'POST':
        #get input from home.html
        word = request.POST.get('word')
        
        #define url to crawl
        URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
        fullURL = URL + word
        #reqests 실행 후 text content 추출
        html = requests.get(fullURL).text
        print(html)
        #BeautifulSoup 
        soup = BeautifulSoup(html, 'html.parser')

        news_title = soup.find_all(class_='_sp_each_title')
        title_array = []

        for title in news_title:
            title_array.append( { 'url': title.get('href') , 'title': title.get('title') } )

        return render(request, 'result.html', {'title_array':title_array })

    else:
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')