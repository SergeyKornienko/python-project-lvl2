"""Module of tests get_diff."""
import json
import pathlib

from gendiff.gendiff import get_diff
from gendiff.parser import open_file, parse

PATH_FILE_DIFF = 'tests/fixtures/diff_file1_file2.json'


def test_get_diff_json_two_files():
    """Test of function get_diff with two files."""
    with open('tests/fixtures/expected_file1_file2.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(*open_file(pathlib.Path('tests/fixtures/file1.json'))),
                parse(*open_file(pathlib.Path('tests/fixtures/file2.json'))),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_get_diff_json_empty_files():
    """Test of function get_diff with two empty files."""
    with open('tests/fixtures/expected_empty.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(*open_file(pathlib.Path('tests/fixtures/file_empty.json'))),
                parse(*open_file(pathlib.Path('tests/fixtures/file_empty2.json'))),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_get_diff_json_file_empty():
    """Test of function get_diff with first file and second empty file."""
    with open('tests/fixtures/expected_file1_empty.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(*open_file(pathlib.Path('tests/fixtures/file1.json'))),
                parse(*open_file(pathlib.Path('tests/fixtures/file_empty.json'))),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_get_diff_json_empty_file():
    """Test of function get_diff with first empty file and second file."""
    with open('tests/fixtures/expected_empty_file1.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(*open_file(pathlib.Path('tests/fixtures/file_empty.json'))),
                parse(*open_file(pathlib.Path('tests/fixtures/file1.json'))),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_get_diff_json_nested():
    """Test of function get_diff with nested files."""
    with open('tests/fixtures/expected_nested_files.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(*open_file(pathlib.Path('tests/fixtures/file_nested1.json'))),
                parse(*open_file(pathlib.Path('tests/fixtures/file_nested2.json'))),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected