from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def index(request):
    return HttpResponse("Hello, World. I made it !")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def custom_404(request):
    return render(request, '404.html', {}, status=404)

# from django.shortcuts import render_to_response
# from django.http import HttpResponse,HttpResponseRedirect
# from django.template import RequestContext
# from blog.models import blog

# def search_form(request):
#     return render_to_response('search_form.html')

# def search(request):
#     errors = []
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             errors.append('Enter a search term.')
#         elif len(q) > 20:
#             errors.append('Please enter at most 20 characters.')
#         else:
#             books = Book.objects.filter(title__icontains=q)
#             return render_to_response('search_results.html',
#                 {'books': books, 'query': q})
#     return render_to_response('search_form.html',{'errors': errors})