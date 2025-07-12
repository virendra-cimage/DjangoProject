from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .serliazers import *

class lmsSignupUser(APIView):
    def post(self,request):
        userdata = lmsSignupSerliazer(data=request.data)
        if userdata.is_valid():
            lmsUser.objects.create(**userdata.data)
            message = {"message": "User created Successfully"}
            return JsonResponse(message,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class lmsGetUserDetails(APIView):
    def get(self,request):
        result = list(lmsUser.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)

class lmsUpdateEmail(APIView):
    def put(self,request):
        userdata = lmsUpdateEmailSerliazer(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            lmsUser.objects.filter(number=number).update(email=email)
            message = {"message": "email updated successfully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)

class lmsDeleteUser(APIView):
    def delete(self,request,number):
        lmsUser.objects.filter(number=number).delete()
        message = {"message": "user deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)


