from dataclasses import dataclass
from typing import Optional
from unittest import TestCase

from dataclass_builders.has_builder import HasBuilder


class TestHasBuilder(TestCase):

    def test_builder_builds_correct_target(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            pass

        foo = Foo.Builder().build()
        self.assertTrue(isinstance(foo, Foo))

    def test_builder_correctly_uses_setter(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str

        foo = Foo.Builder().with_bar("baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_builder_can_take_args_in_constructor(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str

        foo = Foo.Builder(bar="baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_setter_can_overwrite_values(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str

        foo = Foo.Builder(bar="bat").with_bar("baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_can_set_args_at_build_time(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str

        foo = Foo.Builder().with_bar("bat").build(bar="baz")
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_defaults_are_preserved(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str = "baz"

        foo = Foo.Builder().build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_error_for_missing_required_parameter(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: str

        self.assertRaises(ValueError, Foo.Builder().build)

    def test_no_error_for_missing_optional_parameter(self):
        @dataclass(frozen=True)
        class Foo(HasBuilder):
            bar: Optional[str]

        foo = Foo.Builder().build()
        self.assertEqual(None, foo.bar)

