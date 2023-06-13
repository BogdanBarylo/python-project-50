from gendiff.gendiff_engine import generate_diff
#from tests.fixtures import result_test


def test_generate_diff():
    with open('tests/fixtures/result_test.txt', 'r') as result_file:
        result_diff = result_file.read()
    file_1_path = "tests/fixtures/file1.json"
    file_2_path = "tests/fixtures/file2.json"
    assert generate_diff(file_1_path, file_2_path) == result_diff
