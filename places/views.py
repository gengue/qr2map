import math
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from .models import Place, PlaceOfInterest


class Point():
    """
    Esta clase se usa para hacer la busqueda geografica
    """
    lat = 0
    lng = 0

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def rad(self, x):
        return x * math.pi / 180
    # fomula de haversine
    def getDistance(self, p1, p2):
        R = 6378137 #radio de la tierra en metros
        dLat = self.rad(p2.lat - p1.lat)
        dLong = self.rad(p2.lng - p1.lng)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(self.rad(p1.lat)) * math.cos(self.rad(p2.lat)) * math.sin(dLong / 2) * math.sin(dLong / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        return d # valor en metros

class Search(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        place = Place.objects.get(pk=self.kwargs['pk'])
        ctx['place'] = place
        ctx['places_of_interest'] = self.search_places_of_interest(place.location, place.coverage)
        ctx['places_of_interest_json'] = serializers.serialize("json", ctx['places_of_interest'])
        ctx['place_json'] = serializers.serialize("json", [place])
        return render(request, self.template_name, ctx)

    def search_places_of_interest(self, location, coverage):
        lat = location.split(",")[0]
        lng = location.split(",")[1]

        point = Point(lat=float(lat), lng=float(lng))
        all_places = PlaceOfInterest.objects.all()
        result = []

        for place in all_places:
            l = place.location.split(",")
            place_point = Point(lat=float(l[0]),lng=float(l[1]))
            distance = point.getDistance(point, place_point)

            if distance < float(coverage):
                result.append(place)

        return result



