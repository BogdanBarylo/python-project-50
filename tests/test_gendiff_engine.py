from gendiff.gendiff_engine import generate_diff


with (
    open('tests/fixtures/result_test.txt', 'r') as result_file,         # Глеб можно ли выносить это в константу?
    open('tests/fixtures/result_deep_test.txt', 'r') as result_deep_file):
    RESULT = result_file.read()
    DEEP_RESULT = result_deep_file.read()
FILE_1_PATH = "tests/fixtures/file1.json"               # И пути тоже можно выносить в константу?
FILE_2_PATH = "tests/fixtures/file2.json"
FILE_3_PATH = "tests/fixtures/file3.yml"
FILE_4_PATH = "tests/fixtures/file4.yaml"
FILE_1_DEEP_PATH = "tests/fixtures/file1_deep.json"
FILE_2_DEEP_PATH = "tests/fixtures/file2_deep.json"
FILE_3_DEEP_PATH = "tests/fixtures/file3_deep.yml"
FILE_4_DEEP_PATH = "tests/fixtures/file4_deep.yaml"


def test_generate_diff_json():
    assert generate_diff(FILE_1_PATH, FILE_2_PATH) == RESULT


def test_generate_diff_yml():
    assert generate_diff(FILE_3_PATH, FILE_4_PATH) == RESULT


def test_generate_cross_diff_json_yml():
    assert generate_diff(FILE_1_PATH, FILE_4_PATH) == (     # Такая запись норм?
           generate_diff(FILE_3_PATH, FILE_2_PATH))


def test_generate_cross_diff_yml_json():
    assert generate_diff(FILE_1_PATH, FILE_2_PATH) == (     # Есть ли смысл в таком тесте?
           generate_diff(FILE_3_PATH, FILE_4_PATH))


def test_deep_generate_diff_json():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_2_DEEP_PATH) == DEEP_RESULT


def test_deep_generate_diff_yml():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_4_DEEP_PATH) == DEEP_RESULT


def test_deep_generate_cross_diff_json_yml():           #нейминги плохие?
    assert generate_diff(FILE_1_DEEP_PATH, FILE_3_DEEP_PATH) == (
           generate_diff(FILE_4_DEEP_PATH, FILE_2_DEEP_PATH))


def test_deep_generate_cross_diff_yml_json():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_2_DEEP_PATH) == (
           generate_diff(FILE_3_DEEP_PATH, FILE_4_DEEP_PATH))
