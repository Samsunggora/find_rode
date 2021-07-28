from django.contrib import admin
from django.urls import path

from find_route.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', current_datetime),
    path('about/', return_about),
    path('home/', return_home),

]
