from typing import Iterator, Optional


INITIAL_STRING = "MI"


def produce(string: str) -> Optional[list[str]]:
    if not valid(string):
        return []

    rules = [rule1_xI_becomes_xIU, rule2_Mx_becomes_Mxx,
             rule3_III_becomes_U, rule4_UU_is_removed]
    seen = {INITIAL_STRING}
    active = [[INITIAL_STRING]]

    while active:
        new_active = []
        for steps in active:
            last_step = steps[-1]
            for rule in rules:
                for new_string in rule(last_step):
                    if new_string == string:
                        return [*steps, new_string]
                    if new_string not in seen:
                        seen.add(new_string)
                        new_active.append([*steps, new_string])
        active = new_active

    return None


def rule1_xI_becomes_xIU(string: str) -> Iterator[str]:
    if string and string[-1] == "I":
        yield string + "U"


def rule2_Mx_becomes_Mxx(string: str) -> Iterator[str]:
    if len(string) > 1 and string[0] == "M":
        yield "M" + string[1:] * 2


def rule3_III_becomes_U(string: str) -> Iterator[str]:
    return replace_rule(string, "III", "U")


def rule4_UU_is_removed(string: str) -> Iterator[str]:
    return iter(set(replace_rule(string, "UU", "")))


def replace_rule(string: str, pattern: str, replacement: str) -> Iterator[str]:
    start = 0
    while start < len(string):
        start = string.find(pattern, start)
        if start < 0:
            break
        yield string[:start] + replacement + string[start + len(pattern):]
        start += 1

def valid(string: str) -> bool:
    if not string:
        return False
    if any(c not in "MIU" for c in string):
        return False
    if string[0] != "M":
        return False
    if not sum(c == "I" for c in string) % 3:
        return False
    if "M" in string[1:]:
        return False
    return True
    