from django.http import HttpResponse
from .models import CourseNumber
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import CourseSerializer
from rest_framework.exceptions import ValidationError

@api_view(['POST'])
def course_view(request):

    data = request.data
    serializer = CourseSerializer(data=data)
    num = data['number']
    # return Response(num)
    try:
        check = CourseNumber.objects.get(number=int(num))
        if check.number == num:
            return Response({'Course_id': str(num)})
        #
    except Exception as e:
            return Response({'Course_id': 'null'})
