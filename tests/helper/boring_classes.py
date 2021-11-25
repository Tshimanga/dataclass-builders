from typing import Optional, Any

from dataclass_builders.has_builder import HasBuilder


class BoringClass:
    pass


class BoringBuildable(BoringClass, HasBuilder):
    pass


class BoringWithParameter(BoringBuildable):

    def __init__(self, foo: Any) -> None:
        self.foo = foo


class BoringWithOptional(BoringBuildable):

    def __init__(self, foo: Optional[str]) -> None:
        self.foo = foo


class BoringWithDefault(BoringBuildable):

    def __init__(self, foo: str = "bar") -> None:
        self.foo = foo
