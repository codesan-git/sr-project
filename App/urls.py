from django.urls import path
from .views import article_form, delete_article, home, article_details, update_article, delete_article
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('', home, name = 'article_list'),
    path('add/', article_form, name= 'article_form'),
    path('App/<slug:slug>/', article_details, name = 'article_details'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    path('delete/<slug:slug>/', delete_article, name='delete_article'),

    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]