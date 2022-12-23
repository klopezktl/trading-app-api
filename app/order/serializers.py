"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import (
    Order,
)

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for orders."""

    class Meta:
        model = Order
        fields = [
            'id', 'stock', 'quantity', 'price'
        ]
        read_only_fields = ['id']
class OrderDetailSerializer(OrderSerializer):
    """Serializer for order detail view."""

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields

class OrderTotalInvestmentSerializer(serializers.ModelSerializer):
    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ['total_investment']

