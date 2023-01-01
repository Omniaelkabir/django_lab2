from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse ,JsonResponse

from books.models import Book


# Create your views here.
 


def returnlist(request):
    booksinfo= [
		{"id":1, "name":"book1", "description":"book1_description"},
		{"id":2, "name":"book2", "description":"book2_description"},
		{"id":3, "name":"book3", "description":"book3_description"},
    ]
    return HttpResponse(booksinfo)
def landingfunction(request):
    # return HttpResponse("Landing part")
    booksinfo= [
		{"id":1, "name":"book1", "description":"book1_description"},
		{"id":2, "name":"book2", "description":"book2_description"},
		{"id":3, "name":"book3", "description":"book3_description"},
    ]
    return render(request,"homepage.html",context={"books":booksinfo})
def contactus(request):
    name2="Contact Us"
    return render(request,"contactus.html",context={"books":name2})
    # return HttpResponse("Contact Us")
def aboutus(request):
    name1="About Us"
    # return HttpResponse("About Us")
    return render(request,"aboutus.html",context={"books":name1})
def getBook(request):
    book = Book.objects.all()
    return render(request,"book_index.html", context={"book":book})
def showbook(request, id):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book,pk=id)
    return render(request, "showbook.html", context={"book": book})
def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    # return HttpResponse("deleted")
    return redirect("book.index")