from utils.text_utils import normalize_plate_text, is_plausible_plate


def test_normalize_plate_text():
    assert normalize_plate_text(" TS-09 AB 1234 ") == "TS09AB1234"


def test_plausible_plate():
    assert is_plausible_plate("TS09AB1234")
    assert not is_plausible_plate("12")
