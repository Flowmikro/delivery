from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from geopy.distance import geodesic as GD

from .serializers import CargoSerializerList, CargoSerializerUpdate
from .models import CargoModel
from truck.models import TruckModel


class CargoAPIList(ListCreateAPIView):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializerList

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Получаем все грузы, которые еще не были забраны и у которых есть координаты
        unpicked_cargos = queryset.filter(pick_up=True).exclude(lat_pick_up=True)

        # Получаем все грузовики, у которых есть координаты
        trucks = TruckModel.objects.exclude(lat=None).exclude(lng=None)

        result = []

        for cargo in unpicked_cargos:
            cargo_location = (cargo.lat_pick_up, cargo.lng_pick_up)
            nearby_trucks_count = 0

            for truck in trucks:
                truck_location = (truck.lat, truck.lng)
                distance = GD(cargo_location, truck_location).miles

                if distance <= 450:
                    nearby_trucks_count += 1

            result.append({
                'cargo': CargoSerializerList(cargo).data,
                'nearby_trucks_count': nearby_trucks_count
            })

        return Response(result)


class CargoAPIDetail(APIView):
    def get(self, request, pk):
        try:
            # Получаем информацию о грузе по его id
            cargo = CargoModel.objects.get(id=pk)
        except CargoModel.DoesNotExist:
            return Response(f'Груз с id {pk} не найден.')

        # Получаем координаты места забора груза
        lat_pick_up = cargo.lat_pick_up
        lng_pick_up = cargo.lng_pick_up

        if lat_pick_up is None or lng_pick_up is None:
            return Response(f'Недостаточно информации о месте забора груза (lat_pick_up={lat_pick_up}, lng_pick_up={lng_pick_up}).')

        # Получаем все грузовики, у которых есть координаты
        trucks = TruckModel.objects.exclude(lat=None).exclude(lng=None)

        # Создаём список машин с расстоянием до выбранного груза
        truck_list = []

        for truck in trucks:
            # Рассчитываем расстояние (в милях) между местами забора груза и текущим грузовиком
            lat = truck.lat
            lng = truck.lng

            if lat is None or lng is None:
                continue

            distance = GD((lat_pick_up, lng_pick_up), (lat, lng)).miles

            if distance <= 450:
                truck_list.append({
                    'distance': distance,
                })

        # Сериализуем груз и добавляем список машин
        serializer = CargoSerializerList(cargo)
        data = serializer.data
        data['trucks'] = truck_list

        return Response(data)


class CargoAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializerUpdate


