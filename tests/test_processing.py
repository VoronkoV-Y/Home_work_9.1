import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(state_fixture):
    assert filter_by_state(state_fixture) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке
def test_filter_by_state_without_state_elem():
    assert filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]) == []


# Параметризация тестов для различных возможных значений статуса state
@pytest.mark.parametrize("state, excpected", [('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 594886727, 'state': 'CANCELED', 'date': '2025-09-12T21:00:25.241339'}
                            ]),
                                              ('EXECUTED', [{'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]),
                                              ('OTHER', [])])
def test_filter_by_state_parametrize(state, excpected):
    assert filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 594886727, 'state': 'CANCELED', 'date': '2025-09-12T21:00:25.241339'}
                            ], state) == excpected


