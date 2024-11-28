# urls.py
from django.urls import path
from authentication import views, view_api
from .forms import login

urlpatterns = [
        path('',views.login.as_view(authentication_form=login), name='login'),
        path('home/',views.HomeView.as_view(), name='home'),
        # path('upload/', view_api.UploadFile.as_view(), name='home_api'),
]


urlpatterns.append(path('auth/register/', view_api.RegisterCreateView.as_view()))
urlpatterns.append(path('auth/login/', view_api.LoginAPIView.as_view()))
urlpatterns.append(path('upload/', view_api.UploadFile.as_view(), name='home_api'))
# urlpatterns.append(path('auth/profile/', views.ProfileCreateAPIView.as_view()))