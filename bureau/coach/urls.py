from django.urls import path
from coach import views
urlpatterns = [
      path('', views.index, name='index'),
      path('about/', views.about, name='about'),
      path('Gall/', views.Gall, name='Gall'),
      path('career/', views.career, name='career'),
      path('computer/', views.computer),
      path('computer/computer/', views.computer, name='computer'),
      path('coach/', views.coach),
      path('coach/coach/', views.coach, name='coach'),
      path('coachi/', views.coachi),
      path('coachi/coachi/', views.coachi, name='coachi'),
      path('teach/', views.teach),
      path('teach/teach/', views.teach, name='teach'),
      path('cont/', views.cont),
      path('cont/cont/', views.cont, name='cont'),
      path('mat/', views.mat),
      path('mat/mat/', views.mat, name='mat'),
      #path('log/', views.log),
      #path('log/log/', views.log, name='log'),
      #path('logout/', views.logout),
      #path('logout/logout/', views.logout, name='logout'),
      #path('sign/', views.sign),
      #path('sign/sign/', views.sign, name='sign'),
      path('sign_up/', views.sign_up, name='sign_up'),
      #path('sign_up/sign_up/', views.sign_up, name='sign_up'),
      #path('userlogin/', views.userlogin, name='userlogin'),
      path('ul/', views.ul, name='ul'),
      #path('ul/ul/', views.ul, name='ul'),
      #path('userlogin/userlogin/', views.userlogin, name='userlogin'),
      path('user_profile/', views.user_profile, name='profile'),
      path('user_logout/', views.user_logout, name='user_logout'),
      path('handlerequest/', views.handlerequest, name='handlerequest')




]