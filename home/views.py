from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gullar
from .serializers import GullarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class GullarAPIView(APIView):
    def get(self, request, pk=None):
        search = request.GET.get('search')
        gullar = Gullar.objects.all()

        if search:
            gullar = gullar.filter(nomi__icontains=search)

        paginator = PageNumberPagination()
        paginated_qs = paginator.paginate_queryset(gullar, request) 
        serializer = GullarSerializer(paginated_qs, many=True)

        data = {
            'gullar': serializer.data,
            'count': gullar.count(),
            'status': status.HTTP_200_OK
        }
        return paginator.get_paginated_response(data)

    def post(self, request):
        serializer = GullarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GullarDetailApi(APIView):
    def put(self, request, pk):
        gullar = get_object_or_404(Gullar, pk=pk)
        serializer = GullarSerializer(gullar, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "O'zgartirildi", 'data': serializer.data})
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        gullar = get_object_or_404(Gullar, pk=pk)
        serializer = GullarSerializer(gullar, data=request.data, partial=True)    
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Qisman o'zgartirildi", 'data': serializer.data})
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gullar = get_object_or_404(Gullar, pk=pk)
        gullar.delete()
        return Response({'message': "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)
