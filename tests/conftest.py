import pytest
from datetime import date
from src.automobile_type import AutomobileType

@pytest.fixture
def data_full_dict():
    data = {
        "manufacturer": "BMW",
        "series_name": "M4",
        "type_": AutomobileType.convertible,
        "is_electric": False,
        "manufactured_date": "2023-01-01",
        "base_msrp_usd": 93_300,
        "vin": "1234567890",
        "number_of_doors": 2,
        "registration_country": "France",
        "license_plate": "AAA-BBB",
    }
    return data


@pytest.fixture
def data_expected_serialization_full():
    data_expected_serialization = {
        'manufacturer': 'BMW',
        'series_name': 'M4',
        'type_': AutomobileType.convertible,
        'is_electric': False,
        'manufactured_date': date(2023,1,1),
        'base_msrp_usd': 93_300,
        'vin': '1234567890',
        'number_of_doors': 2,
        'registration_country': 'France',
        'license_plate': 'AAA-BBB',
    }
    return data_expected_serialization


@pytest.fixture
def data_optional_json():
    data_json = '''
    {
        "manufacturer": "BMW",
        "series_name": "M4",
        "type_": "Convertible",
        "manufactured_date": "2023-01-01",
        "base_msrp_usd": 93300,
        "vin": "1234567890"
    }
    '''
    return data_json


@pytest.fixture
def data_expected_serialization_optional_json():
    data_json_expected_serialization = {
        'manufacturer': 'BMW',
        'series_name': 'M4',
        'type_': AutomobileType.convertible,
        'is_electric': False,
        'manufactured_date': date(2023, 1, 1),
        'base_msrp_usd': 93_300,
        'vin': '1234567890',
        'number_of_doors': 4,
        'registration_country': None,
        'license_plate': None,
    }
    return data_json_expected_serialization