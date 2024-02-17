from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

# def home(request):
# 	return HttpResponse('<h1>Blog Home</h1>')
# posts = [
#  	{
# 	 	'author': 'Vaga',
# 	 	'title': 'blog post',
# 	 	'content': 'first post content',
# 	 	'date_posted': 'Aug 25, 2019'
# 	},
# 	{
# 		'author': 'jane',
# 	 	'title': 'blog post 2',
# 	 	'content': '2nd post content',
# 	 	'date_posted': 'Aug 28, 2019'
# 	}
#  ]



def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

