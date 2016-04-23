# coding: utf-8
from django.test import TestCase

from mock import patch

from core.management.commands.bootstrap import Command


class CommandTest(TestCase):
    def setUp(self):
        self.command = Command()

    @patch('core.management.commands.bootstrap.urllib2')
    def test_open_and_read_hotel_file(self, _urllib):
        self.command._open_and_read_hotel_file()

        _urllib.urlopen.assert_called_once_with('https://raw.githubusercontent.com/HotelUrbano/desafiohu1/master/artefatos/hoteis.txt')

    @patch('core.management.commands.bootstrap.urllib2')
    def test_open_and_read_available_file(self, _urllib):
        self.command._open_and_read_available_file()

        _urllib.urlopen.assert_called_once_with('https://raw.githubusercontent.com/HotelUrbano/desafiohu1/master/artefatos/disp.txt')

    @patch('core.management.commands.bootstrap.Command._open_and_read_hotel_file')
    @patch('core.management.commands.bootstrap.Establishment')
    def test_populate_hotels_data(self, _establishment, _hotel):
        self.command.populate_hotels_data()

        _hotel.assert_called_once_with()
        _establishment.objects.bulk_create.assert_called_once_with([])

    @patch('core.management.commands.bootstrap.Command._open_and_read_available_file')
    @patch('core.management.commands.bootstrap.AvailabilityEstablishment')
    def test_populate_available_hotel(self, _available, _available_file):
        self.command.populate_available_hotel()

        _available_file.assert_called_once_with()
        _available.objects.bulk_create.assert_called_once_with([])

    @patch('core.management.commands.bootstrap.Command.populate_hotels_data')
    @patch('core.management.commands.bootstrap.Command.populate_available_hotel')
    def test_handle(self, _populate_hotel, _available_hotel):
        self.command.handle()

        _populate_hotel.assert_called_once_with()
        _available_hotel.assert_called_once_with()
