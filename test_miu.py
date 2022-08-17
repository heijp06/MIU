import pytest
from miu import produce, rule1_xI_becomes_xIU, rule2_Mx_becomes_Mxx, rule3_III_becomes_U, rule4_UU_becomes_U


@pytest.mark.parametrize("string,steps", (
    ("MII", ["MI", "MII"]),
    ("MUI", ["MI", "MII", "MIIII", "MUI"]),
    ("MIU", ["MI", "MIU"])
))
def test_produce(string: str, steps: list[str]) -> None:
    assert produce(string) == steps


@pytest.mark.parametrize("string,new_strings", (
    ("MI", ["MIU"]),
    ("MII", ["MIIU"])
))
def test_rule1(string: str, new_strings: list[str]):
    assert list(rule1_xI_becomes_xIU(string)) == new_strings


@pytest.mark.parametrize("string,new_strings", (
    ("MIU", ["MIUIU"]),
    ("MUM", ["MUMUM"]),
    ("MU", ["MUU"])
))
def test_rule2(string: str, new_strings: list[str]):
    assert list(rule2_Mx_becomes_Mxx(string)) == new_strings


@pytest.mark.parametrize("string,new_strings", (
    ("UMIIIMU", ["UMUMU"]),
    ("MIIII", ["MUI", "MIU"]),
    ("MIII", ["MU"]),
    ("MIIIII", ["MUII", "MIUI", "MIIU"])
))
def test_rule3(string: str, new_strings: list[str]):
    assert list(rule3_III_becomes_U(string)) == new_strings


@pytest.mark.parametrize("string,new_strings", (
    ("UUU", ["U"]),
    ("MUUUIII", ["MUIII"]),
    ("MUUIUU", ["MIUU", "MUUI"])
))
def test_rule4(string: str, new_strings: list[str]):
    assert list(rule4_UU_becomes_U(string)) == new_strings
