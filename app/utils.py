from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            'status': 'error',
            'code': response.status_code,
            'errors': response.data
        }, status=response.status_code)

    return Response({
        'status': 'error',
        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
        'errors': 'An unexpected error occurred. Please try again later.',
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
