from typing import get_args

import pytest

from parametric_builder.builder import Builder
from tests.helper.boring_classes import BoringClass, BoringWithParameter, BoringWithDefault, BoringWithOptional


def test_builder_builds_correct_target():
    foo = Builder(BoringClass).build()
    assert isinstance(foo, BoringClass)


def test_builder_correctly_uses_setter():
    foo = Builder(BoringWithParameter).with_foo("bar").build()
    assert "bar" == foo.foo


def test_can_set_via_assignment():
    builder = Builder(BoringWithParameter)
    builder.foo = "bar"
    assert "bar" == builder.build().foo


def test_can_set_via_dict_lookup():
    builder = Builder(BoringWithParameter)
    builder["foo"] = "bar"
    assert "bar" == builder.build().foo


def test_builder_can_take_args_in_constructor():
    foo = Builder(BoringWithParameter, foo="bar").build()
    assert "bar" == foo.foo


def test_setter_can_overwrite_values():
    foo = Builder(BoringWithParameter, foo="bat").with_foo("bar").build()
    assert "bar" == foo.foo


def test_can_set_args_at_build_time():
    foo = Builder(BoringWithParameter).with_foo("bat").build(foo="bar")
    assert "bar" == foo.foo


def test_defaults_are_preserved():
    foo = Builder(BoringWithDefault).build()
    assert "bar" == foo.foo


def test_error_for_missing_required_parameter():
    with pytest.raises(ValueError):
        Builder(BoringWithParameter).build()


def test_no_error_for_missing_optional_parameter():
    foo = Builder(BoringWithOptional).build()
    assert foo.foo is None


def test_parameter_in_builder():
    assert "foo" in BoringWithParameter.Builder()


def test_parameter_not_in_builder():
    assert "baz" not in BoringWithParameter.Builder()
