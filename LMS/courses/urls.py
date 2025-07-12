from django.urls import path
from . import views
urlpatterns= [
    path("signup/",views.lmsSignupUser.as_view()),
    path("getAllUser/",views.lmsGetUserDetails.as_view()),
    path("updateEmail/",views.lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.lmsDeleteUser.as_view()),
]