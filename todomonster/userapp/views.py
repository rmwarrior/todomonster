from rest_framework import mixins, viewsets
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(mixins.ListModelMixin,  # получаем список пользователей
                       mixins.RetrieveModelMixin,  # получаем конкретного пользователя
                       mixins.UpdateModelMixin,  # редактирование пользователей
                       viewsets.GenericViewSet):  # завершающий GenericViewSet, который даёт нам APIView
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
