from django.urls import path
from fnfwebapp import views

app_name = "fnfwebapp"

urlpatterns = [
    path('', views.home, name= 'home' ),
    path('signup/', views.signup, name= 'signup' ),
    path('login/', views.login, name= 'login' ),
    path('addCart/', views.addToCart, name= 'addToCart' ),
    path('order/', views.orderSummary, name= 'orderSummary' ),
    path('search/', views.searchFood, name= 'searchFood' ),
    path('findFood/', views.findFood, name= 'findFood' ),
  
    
    # path('book', views.book, name= 'book' ),
    # # path('clients', views.clients, name= 'clients' ),
    # path('foodnfries', views.fnfhome, name= 'foodnfries' ),
    
]
