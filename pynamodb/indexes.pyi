from typing import Any, Dict, List, Optional, Text, Type, TypeVar

from pynamodb.expressions.condition import Condition
from pynamodb.pagination import ResultIterator

_T = TypeVar('_T', bound='Index')

class IndexMeta(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class Index(metaclass=IndexMeta):
    Meta: Any
    def __init__(self) -> None: ...
    @classmethod
    def count(cls, hash_key, consistent_read: bool = ..., **filters) -> int: ...
    @classmethod
    def query(
        cls: Type[_T],
        hash_key,
        scan_index_forward: Optional[Any] = ...,
        consistent_read: bool = ...,
        limit: Optional[Any] = ...,
        last_evaluated_key: Optional[Dict[Text, Dict[Text, Any]]] = ...,
        attributes_to_get: Optional[Any] = ...,
        **filters,
    ) -> ResultIterator[_T]: ...
    @classmethod
    def scan(
            cls: Type[_T],
            filter_condition: Optional[Condition] = ...,
            segment: Optional[int] = ...,
            total_segments: Optional[int] = ...,
            limit: Optional[int] = ...,
            last_evaluated_key: Optional[Dict[str, Dict[str, Any]]] = ...,
            page_size: Optional[int] = ...,
            rate_limit: Optional[float] = ...,
            attributes_to_get: Optional[List[str]] = ...,
    ) -> ResultIterator[_T]: ...

class GlobalSecondaryIndex(Index): ...
class LocalSecondaryIndex(Index): ...

class Projection(object):
    projection_type: Any
    non_key_attributes: Any

class KeysOnlyProjection(Projection):
    projection_type: Any

class IncludeProjection(Projection):
    projection_type: Any
    non_key_attributes: Any
    def __init__(self, non_attr_keys: Optional[Any] = ...) -> None: ...

class AllProjection(Projection):
    projection_type: Any
