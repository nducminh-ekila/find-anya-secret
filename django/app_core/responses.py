from rest_framework import status
from rest_framework.response import Response


class APISuccessResponse(Response):
    status_code=status.HTTP_200_OK
    msg=""
    res_data={}

class APIFailedResponse(Response):
    status_code=status.HTTP_400_BAD_REQUEST
    msg=""
    res_data={}
