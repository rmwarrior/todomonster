from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    # users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    # user = UserModelSerializer()
    # project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
