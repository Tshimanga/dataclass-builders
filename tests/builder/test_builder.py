from dataclasses import dataclass
from typing import Optional
from unittest import TestCase

from dataclass_builders.builder import Builder


class TestBuilder(TestCase):

    def test_builder_builds_correct_target(self):
        @dataclass(frozen=True)
        class Foo:
            pass

        foo = Builder(Foo).build()
        self.assertTrue(isinstance(foo, Foo))

    def test_builder_correctly_uses_setter(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        foo = Builder(Foo).with_bar("baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_can_set_via_assignment(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        builder = Builder(Foo)
        builder.bar = "baz"
        self.assertEqual("baz", builder.build().bar)

    def test_can_set_via_dict_lookup(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        builder = Builder(Foo)
        builder["bar"] = "baz"
        self.assertEqual("baz", builder.build().bar)

    def test_builder_can_take_args_in_constructor(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        foo = Builder(Foo, bar="baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_setter_can_overwrite_values(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        foo = Builder(Foo, bar="bat").with_bar("baz").build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_can_set_args_at_build_time(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        foo = Builder(Foo).with_bar("bat").build(bar="baz")
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_defaults_are_preserved(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str = "baz"

        foo = Builder(Foo).build()
        self.assertTrue(isinstance(foo, Foo))
        self.assertEqual("baz", foo.bar)

    def test_error_for_missing_required_parameter(self):
        @dataclass(frozen=True)
        class Foo:
            bar: str

        self.assertRaises(ValueError, Builder(Foo).build)

    def test_no_error_for_missing_optional_parameter(self):
        @dataclass(frozen=True)
        class Foo:
            bar: Optional[str]

        foo = Builder(Foo).build()
        self.assertEqual(None, foo.bar)
