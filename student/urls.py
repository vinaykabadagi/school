from django.urls import path
from student import views
from .views import  SearchResultsView,HomePageView,remove,update

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', views.HomePageView, name='home'),
    path('search/update/<item_id>', views.update, name='update'),
    path('search/del/<item_id>', views.remove, name='del'),
]