import pickle

from dataclass_builders.builder import Builder
from tests.builder.helper.boring_dataclass_factory import BoringBuildable


def test_builder_pickles(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "temp"
    builder = BoringBuildable.Builder()
    pickle.dump(builder, p.open("wb"))
    builder = pickle.load(p.open("rb"))
    assert isinstance(builder, Builder)
