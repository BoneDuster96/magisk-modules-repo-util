from typing import Mapping, TypeVar, Dict

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AttrDict(dict):
    def __init__(self, seq: Dict = None, **kwargs): ...
    def update(self, __m: Mapping[_KT, _VT] = None, **kwargs: _VT): ...
    def __setattr__(self, key, value): ...
    def __getattr__(self, item): ...
    def __bool__(self): ...
    def copy(self) -> AttrDict: ...
