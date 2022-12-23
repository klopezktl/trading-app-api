"""
Views for the recipe APIs
"""

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from core.models import (
    Order
)
from order import serializers

class OrderViewSet(viewsets.ModelViewSet):
    """View for manage order APIs."""
    serializer_class = serializers.OrderDetailSerializer
    queryset = Order.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        get_total = self.request.query_params.get('get_total')

        total_sum = 0
        if get_total:
            self.action = 'get_total'
            return self.queryset \
            .annotate(total_investment=Sum('price', field="price * quantity")) \
            .filter(
                user=self.request.user
            ) \
            .order_by('-id') \
            .values("stock", "price", "quantity", "total_investment") \
            .distinct()

        return self.queryset.filter(
                user=self.request.user
            ).annotate(total=Sum('price', field="price * quantity")
                       ).order_by('-id').distinct()

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.OrderSerializer
        # elif self.action == 'get_total':
        #     return serializers.OrderTotalInvestmentSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new order."""
        serializer.save(user=self.request.user)
