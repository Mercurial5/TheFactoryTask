from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import services, serializers


class UserViewSet(ModelViewSet):
    user_services: services.UserServicesInterface = services.UserService()

    def get_queryset(self):
        return self.user_services.get_users()

    def get_permissions(self):
        if self.action == 'list':
            return (IsAdminUser(),)

        return ()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateUserSerializer
        if self.action == 'list':
            return serializers.ListUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = self.user_services.create_user(serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
