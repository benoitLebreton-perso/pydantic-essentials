import pytest
from src.automobile import Automobile
from src.automobile_type import AutomobileType
from pydantic import ValidationError


def test_deserialize(data_full_dict, data_expected_serialization_full):
    a = Automobile.model_validate(data_full_dict)
    assert a.model_dump() == data_expected_serialization_full


def test_deserialize_json_optional(data_optional_json, data_expected_serialization_optional_json):
    a = Automobile.model_validate_json(data_optional_json)
    assert a.model_dump() == data_expected_serialization_optional_json


def test_raise_missing_vin(data_full_dict):
    del data_full_dict["vin"]
    with pytest.raises(ValidationError):
        a = Automobile.model_validate(data_full_dict)


def test_raise_wrong_number_of_doors(data_full_dict):
    data_full_dict["number_of_doors"] = "wrong_value"
    with pytest.raises(ValidationError):
        a = Automobile.model_validate(data_full_dict)


def test_raise_extra_fields(data_full_dict):
    data_full_dict["extra_field"] = "extra_value"
    with pytest.raises(ValidationError):
        a = Automobile.model_validate(data_full_dict)



def test_strip_whitespace(data_full_dict, data_expected_serialization_full):
    data_full_dict["vin"] = f'    \t \n {data_full_dict["vin"]} \n\t'
    a = Automobile.model_validate(data_full_dict)
    assert a.model_dump() == data_expected_serialization_full


def test_raise_validate_default():
    pass

def test_raise_validate_assignement(data_full_dict):
    a = Automobile.model_validate(data_full_dict)
    with pytest.raises(ValidationError):
        a.vin = 1

