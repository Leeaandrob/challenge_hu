# coding: utf-8
import urllib2
import datetime

from django.core.management.base import BaseCommand

from search_engine.models import Establishment, AvailabilityEstablishment


class Command(BaseCommand):

    def _open_and_read_hotel_file(self):
        dados = urllib2.urlopen('https://raw.githubusercontent.com/HotelUrbano/desafiohu1/master/artefatos/hoteis.txt')
        return dados.read().split('\n')

    def _open_and_read_available_file(self):
        dados = urllib2.urlopen('https://raw.githubusercontent.com/HotelUrbano/desafiohu1/master/artefatos/disp.txt')
        return dados.read().split('\n')

    def populate_hotels_data(self):
        hotels = self._open_and_read_hotel_file()
        hotels = [Establishment(**dict(
            city=info.strip().split(
                ',')[1],
            name=info.strip().split(',')[2],
            index=info.strip().split(',')[0]
        ))
            for info in hotels]

        Establishment.objects.bulk_create(hotels)

    def populate_available_hotel(self):
        availables = self._open_and_read_available_file()
        availables = [AvailabilityEstablishment(
            **dict(
                establishment=Establishment.objects.get(
                    index=available.strip().split(
                        ',')[0]),
                available=available.strip().split(',')[2],
                date=datetime.datetime.strptime(available.strip().split(
                    ',')[1],
                    '%d/%m/%Y').date(),
            )) for available in availables if len(available) > 1]
        AvailabilityEstablishment.objects.bulk_create(availables)

    def handle(self, *args, **options):
        self.populate_hotels_data()
        self.populate_available_hotel()

