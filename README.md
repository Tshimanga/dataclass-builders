![Actions Status](https://github.com/Tshimanga/dataclass-builders/actions/workflows/continuous-integration.yaml/badge.svg)

# Dataclass Builder

This is a small library for parametric builder patterns for
dataclasses. Builder patterns are a nice design pattern that
allows for separation of construction of an object from the
use of that object. This is particularly useful in cases where
you want an object to have flexibility in construction but
strict immutability during use - perhaps because you accrue the
constructor data over time rather than all at once.

Normally, however, one typically decides to define a builder on
a per class basis. Aside from exceptional use cases, this can
lead to a lot of boilerplate code. This library provides a
builder pattern implementation for python dataclasses that is
parametric in the target class, thus allowing one builder to
rule them all.
