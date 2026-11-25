from django.test import TestCase

from django.test import TestCase
from model_bakery import baker

from rest_framework.test import APIClient

from airtickets.models import Aeroport


class AeroportViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_get_list(self):
        aeroport = baker.make("Aeroport")

        r = self.client.get('/api/aeroports/')
        data = r.json()

        assert aeroport.name == data[0]['name']
        assert aeroport.id == data[0]['id']
        assert len(data) == 1

    def test_create_aeroport(self):
        r = self.client.post('/api/aeroports/', {
            'name': 'Аэропорт',
            'city': 'Рига',
            'country': 'Латвия',
            'iata_code': 'RIX',
        })

        new_aeroport_id = r.json()['id']

        aeroport = Aeroport.objects.filter(id=new_aeroport_id).first()

        assert len(Aeroport.objects.all()) == 1
        assert aeroport.name == 'Аэропорт'
        assert aeroport.city == 'Рига'
        assert aeroport.country == 'Латвия'
        assert aeroport.iata_code == 'RIX'

    def test_delete_aeroport(self):
        aeroport = baker.make("Aeroport", _quantity=10)

        r = self.client.get('/api/aeroports/')
        data = r.json()

        assert len(data) == 10

        aeroport_id_to_delete = aeroport[3].id

        self.client.delete(f'/api/aeroports/{aeroport_id_to_delete}/')

        r = self.client.get('/api/aeroports/')
        data = r.json()

        assert len(data) == 9
        assert aeroport_id_to_delete not in [i['id'] for i in data]

    def test_update_aeroport(self):
        aeroport = baker.make("Aeroport")

        r = self.client.get(f'/api/aeroports/{aeroport.id}/')
        data = r.json()

        assert data['name'] == aeroport.name

        r = self.client.put(f'/api/aeroports/{aeroport.id}/', {
         'name': 'Новый аэропорт',
         'city': 'Москва',
         'country': 'Россия',
         'iata_code': 'SVO',
        }, content_type='application/json')
        assert r.status_code == 200

        r = self.client.get(f'/api/aeroports/{aeroport.id}/')
        data = r.json()

        assert data['name'] == 'Новый аэропорт'
        assert data['city'] == 'Москва'
        assert data['country'] == 'Россия'
        assert data['iata_code'] == 'SVO'

        aeroport.refresh_from_db()

        assert aeroport.name == 'Новый аэропорт'
