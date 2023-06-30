import pytest
from gendiff.gendiff_engine import generate_diff


path_1 = "tests/fixtures/file1.json"
path_2 = "tests/fixtures/file2.json"
path_3 = "tests/fixtures/file3.yml"
path_4 = "tests/fixtures/file4.yaml"
path_1_d = "tests/fixtures/file1_deep.json"
path_2_d = "tests/fixtures/file2_deep.json"
path_3_d = "tests/fixtures/file3_deep.yml"
path_4_d = "tests/fixtures/file4_deep.yaml"
result = 'tests/fixtures/result_test.txt'
deep_result = 'tests/fixtures/result_deep_test.txt'
result_plain = 'tests/fixtures/result_test_plain.txt'
result_deep_plain = 'tests/fixtures/result_deep_test_plain.txt'
result_json = 'tests/fixtures/result_test_json_formater.txt'
result_json_deep = 'tests/fixtures/result_deep_test_json_formater.txt'
format = ['stylish', 'plain', 'json']


@pytest.mark.parametrize('path_1, path_2, format, result',
                          [(path_1, path_2, 'stylish', result),
                           (path_3, path_4, 'stylish', result),
                           (path_1, path_4, 'stylish', result),
                           (path_3, path_2, 'stylish', result),
                           (path_1_d, path_2_d, 'stylish', deep_result),
                           (path_3_d, path_4_d, 'stylish', deep_result),
                           (path_1_d, path_4_d, 'stylish', deep_result),
                           (path_3_d, path_2_d, 'stylish', deep_result),
                           (path_1, path_2, 'plain', result_plain),
                           (path_3, path_4, 'plain', result_plain),
                           (path_1, path_4, 'plain', result_plain),
                           (path_3, path_2, 'plain', result_plain),
                           (path_1_d, path_2_d, 'plain', result_deep_plain),
                           (path_3_d, path_4_d, 'plain', result_deep_plain),
                           (path_1_d, path_4_d, 'plain', result_deep_plain),
                           (path_3_d, path_2_d, 'plain', result_deep_plain),
                           (path_1, path_2, 'json', result_json),
                           (path_3, path_4, 'json', result_json),
                           (path_1, path_4, 'json', result_json),
                           (path_3, path_2, 'json', result_json),
                           (path_1_d, path_2_d, 'json', result_json_deep),
                           (path_3_d, path_4_d, 'json', result_json_deep),
                           (path_1_d, path_4_d, 'json', result_json_deep),
                           (path_3_d, path_2_d, 'json', result_json_deep)])
def test_generate_diff(path_1, path_2, format, result):
    with open (result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format) == true_result
