from rest_framework import serializers
from .models import AccountTransaction

class AccountTransactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    
    class Meta:
        model = AccountTransaction
        fields = (
            'id',
            'user',
            'account',
            'amount',
            'account_type',
            'category',
            'date',
            'description',
        )
        read_only_fields = ('user',)
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            
            account = validated_data.get('account')
            if account and account.user != request.user:
                raise serializers.ValidationError({"account": "You dont't have access to use this account."})
            
        return super().create(validated_data)