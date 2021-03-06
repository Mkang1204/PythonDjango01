"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import * 
from . import views 
from django.conf.urls.static import static
from django.conf import settings


#urlpatterns = patterns('books.views', (r'^search_form/$', 'search_form'), (r'^search/$', 'search'), )

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'tutorial.views.custom_404'
    # path('admin/', admin.site.urls),
    # path('blog',include('blog.urls')),
    # path('', views.index, name='index',)



# from django.contrib import admin
# admin.autodiscover()

# urlpatterns += patterns('mysite.views',
#       (r'^admin/', include(admin.site.urls)),
# )
