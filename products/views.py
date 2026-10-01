from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product
from .serializers import ProductSerializer
from .authentication import BearerAuthentication


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]