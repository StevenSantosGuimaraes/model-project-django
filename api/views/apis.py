from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import ClienteSerializer
from crm.models import Cliente


@api_view(['GET'])
def listar_clientes_api(request, id=None):
    if request.user.is_authenticated:
        if id is not None:
            try:
                registro_cliente = Cliente.objects.get(pk=id)
                serializer = ClienteSerializer(registro_cliente)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Cliente.DoesNotExist:
                return Response({"erro": "Cliente não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"erro": "Não autorizado!"}, status=status.HTTP_403_FORBIDDEN)
