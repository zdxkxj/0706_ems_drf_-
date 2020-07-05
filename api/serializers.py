from rest_framework import exceptions, serializers
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'username':{
                'required':True,
                'min_length':2,
                'error_messages':{
                    'required':'用户名必填',
                    'min_length':'长度至少为2'
                }
            },
            'real_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '真实姓名必填',
                    'min_length': '长度至少为2'
                }
            },
            'password': {
                'required': True,
                'min_length': 6,
                'error_messages': {
                    'required': '密码必填',
                    'min_length': '长度至少为6'
                }
            },
        }

    def validate(self,attrs):
        username=attrs.get('username')
        password=attrs.get('password')
        re_pwd=attrs.pop('re_pwd')
        print(attrs)
        print(password)
        print(re_pwd)
        user=User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError('用户名已存在')
        if password !=re_pwd:
            raise exceptions.ValidationError('密码不一致')
        return attrs

class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model=Employee
        # fields='__all__'
        fields=('id','emp_name','age','salary','age_name','img')

        extra_kwargs={
            'emp_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '员工名必填',
                    'min_length': '长度至少为2'
                }
            },
        }
