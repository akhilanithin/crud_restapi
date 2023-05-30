
from django.contrib import admin  
from django.urls import path  
from . import views  


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('',views.home,name='home'),
    path('emp', views.emp,name='details'),  #list all notes
    path('show',views.show,name='show'),  # Create a new Note
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),  # Update Note with data provided in request
    path('delete/<int:id>', views.destroy,name='delete'), #  Delete single Note with primary key id
]


