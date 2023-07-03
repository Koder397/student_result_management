from django.urls import path

from .views import login, logout, logout_view

urlpatterns = [
    path('', login, name="login"),
    path('logout_view/', logout_view, name='logout_view')
    # path('result', result, name="result")
]