from django.urls import include, path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('news/', include('news_blog.urls')),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:issue_id>/vote/', views.vote, name='vote'),
]
