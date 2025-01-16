import random
import uuid
from typing import Any, Dict, List, Tuple

KEY_PREFIX = "key_"
STRING_PREFIX = "value_"
VALUE_PREFIX = "value_"
NESTED_KEY = "nested"
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 1000
MIN_TTL = 10
MAX_TTL = 10 * 60
DEFAULT_MAPPING_KEYS_LENGTH = 3
DEFAULT_MAPPING_DEPTH_LENGTH = 3


def get_nested_mapping_key():
    return NESTED_KEY


def get_key_prefix():
    return KEY_PREFIX


def get_value_prefix():
    return VALUE_PREFIX


def generate_random_key() -> str:
    return str(uuid.uuid4())


def generate_test_key() -> str:
    key = get_key_prefix() + generate_random_key()
    return key


def generate_test_string() -> str:
    return get_value_prefix() + generate_random_key()


def generate_test_number() -> float:
    return random.uniform(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def generate_test_nested_mapping(
    length: int = DEFAULT_MAPPING_KEYS_LENGTH,
    depth: int = DEFAULT_MAPPING_DEPTH_LENGTH,
) -> Dict[str, Any]:
    nested_key = get_nested_mapping_key()
    mapping = generate_test_flat_mapping(length)
    current = mapping
    while depth > 0:
        current[nested_key] = generate_test_flat_mapping(length)
        current = current[nested_key]
        depth -= 1
    return mapping


def generate_test_set(length: int = DEFAULT_MAPPING_KEYS_LENGTH) -> set:
    return {
        random.choice(
            [
                generate_test_string(),
                generate_test_number(),
                generate_random_key(),
            ]
        )
        for _ in range(length)
    }


def generate_test_ttl() -> float:
    return random.randint(MIN_TTL, MAX_TTL)


def generate_test_key_value(length: int = 0) -> Tuple[str, Any]:
    key = generate_test_key()
    value_type = random.choice(
        [
            generate_test_string,
            generate_test_number,
            lambda: generate_test_flat_mapping(length - 1),
            lambda: generate_test_nested_mapping(length - 1),
            generate_test_set,
        ]
    )
    value = value_type()
    return (key, value)


def generate_test_keys_values(
    length: int = DEFAULT_MAPPING_KEYS_LENGTH,
) -> List[Tuple[str, Any]]:
    results = []
    for _ in range(length):
        (key, value) = generate_test_key_value()
        results.append((key, value))
    return results


def generate_test_flat_mapping(
    length: int = DEFAULT_MAPPING_KEYS_LENGTH,
) -> Dict[str, Any]:
    mapping = {}
    lst = generate_test_keys_values(length)
    for key, value in lst:
        mapping[key] = value
    return mapping


def get_random_mapping_field(mapping: Dict[str, Any]) -> str:
    return random.choice(list(mapping.keys()))


def get_random_mapping_key_value(mapping: Dict[str, Any]) -> Tuple[str, Any]:
    key = get_random_mapping_field(mapping)
    value = mapping[key]
    return key, value


def get_random_mapping_key_new_value(
    mapping: Dict[str, Any],
) -> Tuple[str, Any]:
    key = get_random_mapping_field(mapping)
    value = mapping[key]
    new_value = None

    if isinstance(value, dict):
        new_value = generate_test_flat_mapping()

    elif isinstance(value, set):
        new_value = generate_test_set()

    elif isinstance(value, (str, int, float)):
        if isinstance(value, str):
            if not value.isdigit():
                new_value = str(generate_test_number())
            else:
                new_value = generate_test_string()
        else:
            new_value = generate_test_number()

    return key, new_value
