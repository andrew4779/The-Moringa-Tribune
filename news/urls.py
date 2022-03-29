from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[

   path('',views.news_today, name='newsToday'),
   path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
   path('',views.search_results, name='search_results'),
   path('',views.article,name ='article'),
   path('', views.new_article, name='new-article')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)