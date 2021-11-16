from dataclasses import dataclass
from typing import Optional

from dataclass_builders.has_builder import HasBuilder


@dataclass(frozen=True)
class BoringDataclass:
    pass


@dataclass(frozen=True)
class BoringBuildable(BoringDataclass, HasBuilder):
    pass


@dataclass(frozen=True)
class BoringWithParameter(BoringBuildable):
    foo: str


@dataclass(frozen=True)
class BoringWithOptional(BoringBuildable):
    foo: Optional[str]


@dataclass(frozen=True)
class BoringWithDefault(BoringBuildable):
    foo: str = "bar"
