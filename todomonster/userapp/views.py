from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import User


class UserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
