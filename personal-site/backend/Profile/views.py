from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def personal_info(request):
    data = {
        "name": "Ahmed Kashima",
        "bio": "Computer Science student and passionate developer.",
        "email": "ahmed.email@example.com",
        "social": {
            "github": "https://github.com/ahmedkashima",
            "linkedin": "https://linkedin.com/in/ahmedkashima"
        },
        "pictures": [
            "https://yourdomain.com/static/images/pic1.jpg",
            "https://yourdomain.com/static/images/pic2.jpg"
        ]
    }
    return Response(data)
