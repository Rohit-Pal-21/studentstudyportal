from django.urls import URLPattern, path
from . import views

urlpatterns =[ 
    path('https://studentstudyportal.azurewebsites.net',views.home,name="home"),
    path('https://studentstudyportal.azurewebsites.net/notes',views.notes,name="notes"),
    path('https://studentstudyportal.azurewebsites.net/delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('https://studentstudyportal.azurewebsites.netnotes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
    path('https://studentstudyportal.azurewebsites.net/homework',views.homework,name="homework"),
    path('https://studentstudyportal.azurewebsites.net/update_homework/<int:pk>',views.update_homework,name="update-homework"),
    path('https://studentstudyportal.azurewebsites.net/delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('https://studentstudyportal.azurewebsites.net/youtube',views.youtube,name="youtube"),
    path('https://studentstudyportal.azurewebsites.net/todo',views.todo,name="todo"),
    path('https://studentstudyportal.azurewebsites.net/update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('https://studentstudyportal.azurewebsites.net/delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),
    path('https://studentstudyportal.azurewebsites.net/books',views.books,name="books"),
    path('https://studentstudyportal.azurewebsites.net/books',views.books,name="books"),
    path('https://studentstudyportal.azurewebsites.net/dictionary',views.dictionary,name="dictionary"),
    path('https://studentstudyportal.azurewebsites.net/wiki',views.wiki,name="wiki"),
    path('https://studentstudyportal.azurewebsites.net/conversion',views.conversion,name="conversion")





    
    ]
