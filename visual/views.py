from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.
def get_html(termino):
	html = requests.get('https://www.google.com/search?q='+termino)
	return html.text

def home(request):
	list_elements = []

	if 'termino' in request.GET and request.GET['termino'].strip() != '':
		termino = request.GET['termino'].strip().replace(' ', '+')
		html = get_html(termino=termino)
		entire_document = BeautifulSoup(html, 'html.parser')
		search = entire_document.find_all('div', class_="egMi0")
		
		for i in range(0,5):
			element = BeautifulSoup(f'{search[i]}', 'html.parser')
			title = element.h3.string
			link = element.a['href']

			list_elements.append({
				'title': title,
				'link': link
			})

	return render(request=request, template_name="visual/home.html", context={
		'elementos': list_elements
	})
