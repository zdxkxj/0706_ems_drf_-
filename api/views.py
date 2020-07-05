from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

from api.models import User, Employee
from api.serializers import UserModelSerializer,EmployeeModelSerializer
from utils.response import APIResponse

class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        request_data=request.data
        print(request_data)
        serialzer=UserModelSerializer(data=request_data)
        serialzer.is_valid(raise_exception=True)
        user_obj=serialzer.save()

        return APIResponse(200,True,results=UserModelSerializer(user_obj).data)

    def get(self, request, *args, **kwargs):
        username=request.query_params.get('username')
        password=request.query_params.get('password')
        user=User.objects.filter(username=username,password=password).first()
        print(username,type(username))
        print(password)
        print(user,type(user))

        if user:
            data=UserModelSerializer(user).data
            return APIResponse(200,True,results=data)

        return APIResponse(400,False)


class EmployeeView(ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericAPIView,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'

    def get(self,request, *args, **kwargs):
        emp_id=kwargs.get('id')
        if emp_id:
            user_list=self.retrieve(request, *args, **kwargs)
        else:
            user_list=self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=user_list.data)

    def post(self,request, *args, **kwargs):
        # data=request.data
        # print(data)
        # user_list=self.list(request, *args, **kwargs)
        user_obj=self.create(request, *args, **kwargs)
        return APIResponse(200,True,results=user_obj.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(200, True)

    def patch(self, request, *args, **kwargs):
        user_obj=self.partial_update(request, *args, **kwargs)
        return APIResponse(200, True, results=user_obj.data)




