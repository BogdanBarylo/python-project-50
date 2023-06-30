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


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1, path_2, result),
                          (path_3, path_4, result),
                          (path_1, path_4, result),
                          (path_3, path_2, result)])
def test_generate_diff_stylish(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='stylish') == true_result


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1_d, path_2_d, deep_result),
                          (path_3_d, path_4_d, deep_result),
                          (path_1_d, path_4_d, deep_result),
                          (path_3_d, path_2_d, deep_result)])
def test_generate_diff_deep_stylish(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='stylish') == true_result


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1, path_2, result_plain),
                          (path_3, path_4, result_plain),
                          (path_1, path_4, result_plain),
                          (path_3, path_2, result_plain)])
def test_generate_diff_plain(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='plain') == true_result


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1_d, path_2_d, result_deep_plain),
                          (path_3_d, path_4_d, result_deep_plain),
                          (path_1_d, path_4_d, result_deep_plain),
                          (path_3_d, path_2_d, result_deep_plain)])
def test_generate_diff_deep_plain(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='plain') == true_result


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1, path_2, result_json),
                          (path_3, path_4, result_json),
                          (path_1, path_4, result_json),
                          (path_3, path_2, result_json)])
def test_generate_diff_json(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='json') == true_result


@pytest.mark.parametrize('path_1, path_2, result',
                         [(path_1_d, path_2_d, result_json_deep),
                          (path_3_d, path_4_d, result_json_deep),
                          (path_1_d, path_4_d, result_json_deep),
                          (path_3_d, path_2_d, result_json_deep)])
def test_generate_diff_deep_json(path_1, path_2, result):
    with open(result) as f:
        true_result = f.read()
    assert generate_diff(path_1, path_2, format='json') == true_result
