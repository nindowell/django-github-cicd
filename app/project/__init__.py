from pathlib import Path
from typing import List, Optional
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

TRUE = ('1', 'true', 'True', 'TRUE', 'on', 'yes')


def is_true(val: Optional[str]) -> bool:
    return val in TRUE


def split_with_comma(val: str) -> List[str]:
    return list(filter(None, map(str.strip, val.split(','))))
