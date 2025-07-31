import pytest
from unittest.mock import patch
from src.CSV_Excel import csv_reader_fnc, excel_reader_fnc


@patch("pandas.read_csv")
def test_csv_reader_fnc(mock_read):
    mock_read.return_value.to_dict.return_value = [{'id;state': '4699552;EXECUTED'}]
    assert csv_reader_fnc("test_path") == [{'id;state': '4699552;EXECUTED'}]
    mock_read.assert_called_once_with("test_path")



with patch('pandas.read_csv', side_effect=FileNotFoundError) as mock_read_csv:
    path_csv = "invalid_path.csv"
    result = csv_reader_fnc(path_csv)
    expected = f"Ошибка! Файл {path_csv} не найден!"
    assert result == expected
    mock_read_csv.assert_called_once_with(path_csv)


@patch("pandas.read_excel")
def test_excel_reader_fnc(mock_read):
    mock_read.return_value.to_dict.return_value = [{'id;state': '4699552;EXECUTED'}]
    assert excel_reader_fnc("test_path") == [{'id;state': '4699552;EXECUTED'}]
    mock_read.assert_called_once_with("test_path")



with patch('pandas.read_excel', side_effect=FileNotFoundError) as mock_read_excel:
    path_excel = "invalid_path.xlsx"
    result = excel_reader_fnc(path_excel)
    expected = f"Ошибка! Файл {path_excel} не найден!"
    assert result == expected
    mock_read_excel.assert_called_once_with(path_excel)






