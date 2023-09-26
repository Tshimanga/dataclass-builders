import pytest

from tests.helper.boring_classes import BoringBuildable, BoringWithParameter, BoringWithDefault, \
    BoringWithOptional, BoringWithNullable


def test_builder_builds_correct_target():
    foo = BoringBuildable.Builder().build()
    assert isinstance(foo, BoringBuildable)


def test_builder_correctly_uses_setter():
    foo = BoringWithParameter.Builder().with_foo("bar").build()
    assert "bar" == foo.foo


def test_builder_can_take_args_in_constructor():
    foo = BoringWithParameter.Builder(foo="bar").build()
    assert "bar" == foo.foo


def test_setter_can_overwrite_values():
    foo = BoringWithParameter.Builder(foo="bat").with_foo("bar").build()
    assert "bar" == foo.foo


def test_can_set_args_at_build_time():
    foo = BoringWithParameter.Builder().with_foo("bat").build(foo="bar")
    assert "bar" == foo.foo


def test_defaults_are_preserved():
    foo = BoringWithDefault.Builder().build()
    assert "bar" == foo.foo


def test_error_for_missing_required_parameter():
    with pytest.raises(ValueError):
        BoringWithParameter.Builder().build()


def test_no_error_for_missing_optional_parameter():
    foo = BoringWithOptional.Builder().build()
    assert foo.foo is None


def test_no_error_for_missing_nullable_parameter():
    foo = BoringWithNullable.Builder().build()
    assert foo.foo is None
