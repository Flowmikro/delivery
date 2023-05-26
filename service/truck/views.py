from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import TruckSerializerList, TruckSerializerUpdate
from .models import TruckModel


class TruckAPIList(ListCreateAPIView):
    queryset = TruckModel.objects.all()
    serializer_class = TruckSerializerList


class TruckAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = TruckModel.objects.all()
    serializer_class = TruckSerializerUpdate
