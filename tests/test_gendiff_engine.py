from gendiff.gendiff_engine import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result_test.txt', 'r') as result_file:
        result_diff = result_file.read()
    file_1_path = "tests/fixtures/file1.json"
    file_2_path = "tests/fixtures/file2.json"
    file_3_path = "tests/fixtures/file3.yml"
    file_4_path = "tests/fixtures/file4.yaml"
    assert generate_diff(file_1_path, file_2_path) == result_diff
    assert generate_diff(file_3_path, file_4_path) == result_diff
    assert generate_diff(file_1_path, file_4_path) == generate_diff(file_3_path, file_2_path)
    assert generate_diff(file_1_path, file_2_path) == generate_diff(file_3_path, file_4_path)
