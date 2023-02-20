"""
url configurations for app 'authentication'
for Signup API,
SignupView function is called
for login API,
LoginView function is called
for Book API,
created a default router object and register the viewset class with it
Through this API URLs are determined automatically by the router
The '' url request takes to add_books function in views to fill details
The 'show' url requests show_books function to display data
The 'retrieve' url requests retrieve_books function to retrieve the data
The 'update' url requests delete_books function to update the data
The 'delete' url requests delete_books function to delete the data
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('Signup', views.SignupView, basename='signup')
router.register('login', views.LoginView, basename='login')
router.register('Book', views.BookViewSet, basename='Books')
urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
