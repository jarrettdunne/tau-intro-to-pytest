import pytest

from stuff.accum import Accumulator

#
# Fixtures
#

@pytest.fixture
def accum():
    return Accumulator()

#
# Tests
#

@pytest.mark.accumulator
def test_accumulator_init(accum):
    accum.add(1)
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10