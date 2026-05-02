from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def lookup_by_email(self, request):
        """Look up a user by email address for sending money."""
        email = request.query_params.get('email', '').strip()
        
        if not email:
            return Response(
                {'error': 'Email parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(email=email)
            return Response({
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'is_verified': user.is_verified,
                'message': 'User found'
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {'error': f'No user found with email: {email}'},
                status=status.HTTP_404_NOT_FOUND
            )
