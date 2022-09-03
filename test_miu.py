from typing import Iterable
import pytest
import miu


@pytest.mark.parametrize("string,steps", (
    ("MII", ["MI", "MII"]),
    ("MUI", ["MI", "MII", "MIIII", "MUI"]),
    ("MIU", ["MI", "MIU"]),
    ("MIX", [])
))
def test_produce(string: str, steps: list[str]) -> None:
    assert miu.produce(string) == steps


@pytest.mark.parametrize("string,new_strings", (
    ("MI", ["MIU"]),
    ("MII", ["MIIU"])
))
def test_rule1(string: str, new_strings: list[str]):
    assertItemsEqual(miu.rule1_xI_becomes_xIU(string), new_strings)


@pytest.mark.parametrize("string,new_strings", (
    ("MIU", ["MIUIU"]),
    ("MUM", ["MUMUM"]),
    ("MU", ["MUU"])
))
def test_rule2(string: str, new_strings: list[str]):
    assertItemsEqual(miu.rule2_Mx_becomes_Mxx(string), new_strings)


@pytest.mark.parametrize("string,new_strings", (
    ("UMIIIMU", ["UMUMU"]),
    ("MIIII", ["MUI", "MIU"]),
    ("MIII", ["MU"]),
    ("MIIIII", ["MUII", "MIUI", "MIIU"])
))
def test_rule3(string: str, new_strings: list[str]):
    assertItemsEqual(miu.rule3_III_becomes_U(string), new_strings)


@pytest.mark.parametrize("string,new_strings", (
    ("UUU", ["U"]),
    ("MUUUIII", ["MUIII"]),
    ("MUUIUU", ["MIUU", "MUUI"])
))
def test_rule4(string: str, new_strings: list[str]):
    assertItemsEqual(miu.rule4_UU_is_removed(string), new_strings)

@pytest.mark.parametrize("string,result", (
    ("MIX", False),
    ("IM", False),
    ("", False),
    ("MIM", False),
    ("MU", False),
    ("M", False),
    ("MIII", False),
    ("MIU", True),
    ("MI", True),
))
def test_valid(string: str, result: bool):
    assert miu.valid(string) == result


def assertItemsEqual(items1: Iterable[str], items2: Iterable[str]) -> bool:
    assert sorted(list(items1)) == sorted(list(items2))
