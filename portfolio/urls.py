from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
        path('', views.index, name='index'),
        path('x', views.xfiles, name='x'),
        path('blog', views.blog, name='blog'),
        path('booklib', views.bookLib, name='books'),
        path('cryptoDash',views.Cdashboard, name='cdashboard'),
        path('ecom', views.ecom,name='ecom'),
        path('scraper', views.scraper, name='scraper'),
        path('vs',views.videoS,name='vs'),
]+ + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
