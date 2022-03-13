from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import User,Cour,ArchiveUser,ArchiveCour

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('__all__')
        extra_kwargs = {
            'id': {
                'validators': [UnicodeUsernameValidator()],
            }
        }



class CourSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field = 'id')

    class Meta:

        model = Cour
        fields = ('__all__')


class ArchiveCourSerializer(serializers.ModelSerializer):

    cour = serializers.SlugRelatedField(queryset = Cour.objects.all(),slug_field = 'id', error_messages={
        'does_not_exist': 'Foo error field={value} does not exist.',
    })

    class Meta:

        model = ArchiveCour
        fields = ('__all__')
     


class ArchiveUserSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field = 'id', error_messages={
        'does_not_exist': 'Foo error field={value} does not exist.',
    })

    class Meta:

        model = ArchiveUser
        fields = ('__all__')

    