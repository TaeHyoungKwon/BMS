from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from book.models import Book
from book.serializers import BookSerializer


@csrf_exempt
def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
