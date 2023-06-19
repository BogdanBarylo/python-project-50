from gendiff.gendiff_engine import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result_test.txt', 'r') as result_file:
        result_diff = result_file.read()
    with open('tests/fixtures/result_deep_test.txt', 'r') as result_deep_file:
        result_deep_diff = result_deep_file.read()
    file_1_path = "tests/fixtures/file1.json"
    file_2_path = "tests/fixtures/file2.json"
    file_3_path = "tests/fixtures/file3.yml"
    file_4_path = "tests/fixtures/file4.yaml"
    file_1_deep_path = "tests/fixtures/file1_deep.json"
    file_2_deep_path = "tests/fixtures/file2_deep.json"
    file_3_deep_path = "tests/fixtures/file3_deep.yml"
    file_4_deep_path = "tests/fixtures/file4_deep.yaml"
    assert generate_diff(file_1_path, file_2_path) == result_diff
    assert generate_diff(file_3_path, file_4_path) == result_diff
    assert generate_diff(file_1_path, file_4_path) == generate_diff(file_3_path, file_2_path)
    assert generate_diff(file_1_path, file_2_path) == generate_diff(file_3_path, file_4_path)
    assert generate_diff(file_1_deep_path, file_2_deep_path) == result_deep_diff
    assert generate_diff(file_3_deep_path, file_4_deep_path) == result_deep_diff
    assert generate_diff(file_1_deep_path, file_4_deep_path) == generate_diff(file_3_deep_path, file_2_deep_path)
    assert generate_diff(file_1_deep_path, file_2_deep_path) == generate_diff(file_3_deep_path, file_4_deep_path)
