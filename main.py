def get_domain(mapping: dict) -> set:
    return set(mapping.keys())

def get_range(mapping: dict) -> set:
    return set(mapping.values())

def is_well_defined(mapping: dict, target: set) -> bool:
    for v in mapping.values():
        if v not in target:
            return False
    return True

def is_injective(mapping: dict) -> bool:
    vals = list(mapping.values())
    return len(vals) == len(set(vals))

def is_surjective(mapping: dict, target: set) -> bool:
    return set(mapping.values()) == target

def is_bijective(mapping: dict, target: set) -> bool:
    return is_injective(mapping) and is_surjective(mapping, target)