
from django.urls import path
from books.views import returnlist, landingfunction, contactus, aboutus, getBook,showbook,deleteBook

urlpatterns = [
  
   
    path('books',returnlist,name='books'),
    path('landing',landingfunction,name='landing'),
    path('contactus',contactus,name="contactus"),
    path('aboutus',aboutus,name='aboutus'),
    path('db/book',getBook, name='book.index'),
    path('db/book/show/<int:id>', showbook, name='book.show'),
    path('db/book/delete/<id>', deleteBook, name='book.delete'),

]
