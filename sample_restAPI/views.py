from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user(request):
    user = [ 
        {'name': 'Roshla', 'age': 42},
        {'name': 'John', 'age': 30},
        {'name': 'Alice', 'age': 28},
        ]
    return Response(user)

