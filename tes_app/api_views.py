from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produk
from .serializers import ProdukSerializer

@api_view(['PUT'])
def update_produk_api(request, pk):
    produk = Produk.objects.get(id_produk=pk)
    serializer = ProdukSerializer(instance=produk, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_produk_api(request, pk):
    produk = Produk.objects.get(id_produk=pk)
    produk.delete()
    return Response({'message': 'Produk deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def insert_produk_api(request):
    serializer = ProdukSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def produk_api(request):
    produk = Produk.objects.all()
    serializer = ProdukSerializer(produk, many=True)
    return Response(serializer.data)


