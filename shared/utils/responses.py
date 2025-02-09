from rest_framework.response import Response

class SuccessResponse:
    @staticmethod
    def format(message="Success", data=None, status_code=200):
        return Response({
            "type": "success",
            "errors": [],
            "detail": message,
            "data": data
        }, status=status_code)
