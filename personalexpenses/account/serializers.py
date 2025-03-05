from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")  # Apenas leitura, pega do usuário autenticado

    class Meta:
        model = Account
        fields = ('id', 'name', 'balance', 'user_id')  # user_id não é um campo gravável
        read_only_fields = ('user_id',)  # Garante que não seja enviado na requisição

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # Passa o objeto User
        return super().create(validated_data)
