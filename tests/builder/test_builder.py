from unittest import TestCase

from dataclass_builders.builder import Builder
from tests.builder.helper.boring_dataclass_factory import BoringDataclass, BoringWithParameter, BoringWithDefault, \
    BoringWithOptional


class TestBuilder(TestCase):

    def test_builder_builds_correct_target(self):
        foo = Builder(BoringDataclass).build()
        self.assertTrue(isinstance(foo, BoringDataclass))

    def test_builder_correctly_uses_setter(self):
        foo = Builder(BoringWithParameter).with_foo("bar").build()
        self.assertEqual("bar", foo.foo)

    def test_can_set_via_assignment(self):
        builder = Builder(BoringWithParameter)
        builder.foo = "bar"
        self.assertEqual("bar", builder.build().foo)

    def test_can_set_via_dict_lookup(self):
        builder = Builder(BoringWithParameter)
        builder["foo"] = "bar"
        self.assertEqual("bar", builder.build().foo)

    def test_builder_can_take_args_in_constructor(self):
        foo = Builder(BoringWithParameter, foo="bar").build()
        self.assertEqual("bar", foo.foo)

    def test_setter_can_overwrite_values(self):
        foo = Builder(BoringWithParameter, foo="bat").with_foo("bar").build()
        self.assertEqual("bar", foo.foo)

    def test_can_set_args_at_build_time(self):
        foo = Builder(BoringWithParameter).with_foo("bat").build(foo="bar")
        self.assertEqual("bar", foo.foo)

    def test_defaults_are_preserved(self):
        foo = Builder(BoringWithDefault).build()
        self.assertEqual("bar", foo.foo)

    def test_error_for_missing_required_parameter(self):
        self.assertRaises(ValueError, Builder(BoringWithParameter).build)

    def test_no_error_for_missing_optional_parameter(self):
        foo = Builder(BoringWithOptional).build()
        self.assertEqual(None, foo.foo)

    def test_parameter_in_builder(self):
        self.assertTrue("foo" in BoringWithParameter.Builder())

    def test_parameter_not_in_builder(self):
        self.assertFalse("baz" in BoringWithParameter.Builder())
