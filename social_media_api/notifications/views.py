from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class UserNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        data = [
            {
                'actor': n.actor.username,
                'verb': n.verb,
                'target': str(n.target),
                'timestamp': n.timestamp
            } for n in notifications
        ]
        return Response(data)

    def post(self, request):
        # Mark notifications as read
        Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({'message': 'Notifications marked as read.'})
