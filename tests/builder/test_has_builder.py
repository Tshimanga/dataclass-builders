from unittest import TestCase

from tests.builder.helper.boring_dataclass_factory import BoringBuildable, BoringWithParameter, BoringWithDefault, \
    BoringWithOptional


class TestHasBuilder(TestCase):

    def test_builder_builds_correct_target(self):
        foo = BoringBuildable.Builder().build()
        self.assertTrue(isinstance(foo, BoringBuildable))

    def test_builder_correctly_uses_setter(self):
        foo = BoringWithParameter.Builder().with_foo("bar").build()
        self.assertEqual("bar", foo.foo)

    def test_builder_can_take_args_in_constructor(self):
        foo = BoringWithParameter.Builder(foo="bar").build()
        self.assertEqual("bar", foo.foo)

    def test_setter_can_overwrite_values(self):
        foo = BoringWithParameter.Builder(foo="bat").with_foo("bar").build()
        self.assertEqual("bar", foo.foo)

    def test_can_set_args_at_build_time(self):
        foo = BoringWithParameter.Builder().with_foo("bat").build(foo="bar")
        self.assertEqual("bar", foo.foo)

    def test_defaults_are_preserved(self):
        foo = BoringWithDefault.Builder().build()
        self.assertEqual("bar", foo.foo)

    def test_error_for_missing_required_parameter(self):
        self.assertRaises(ValueError, BoringWithParameter.Builder().build)

    def test_no_error_for_missing_optional_parameter(self):
        foo = BoringWithOptional.Builder().build()
        self.assertEqual(None, foo.foo)

