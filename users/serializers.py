from rest_framework import serializers,validators
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from django.contrib.auth.models import User

class RegisterSerializers(serializers.ModelSerializers):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
  
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={"input_type":"password"}
        )
    password1 = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={"input_type":"password"}
        )
    
    class Meta:
        model=User
        fields = ('username', 'password', 'password1', 'email', 'first_name', 'last_name')
