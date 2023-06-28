from gendiff.gendiff_engine import generate_diff


with (
    open('tests/fixtures/result_test.txt', 'r') as 
                                                    result_file,
    open('tests/fixtures/result_deep_test.txt', 'r') as 
                                                    result_deep_file,
    open('tests/fixtures/result_test_plain.txt', 'r') as 
                                                    result_plain,
    open('tests/fixtures/result_deep_test_plain.txt', 'r') as 
                                                    result_deep_plain,
    open('tests/fixtures/result_test_json_formater.txt', 'r') as 
                                                    result_json_form,
    open('tests/fixtures/result_deep_test_json_formater.txt', 'r') as 
                                                    result_json_deep_form ):
    RESULT = result_file.read()
    DEEP_RESULT = result_deep_file.read()
    RESULT_PLAIN = result_plain.read()
    RESULT_DEEP_PLAIN = result_deep_plain.read()
    RESULT_JSON_FORM = result_json_form.read()
    RESULT_JSON_DEEP_FORM = result_json_deep_form.read()
FILE_1_PATH = "tests/fixtures/file1.json"
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
    assert generate_diff(FILE_1_PATH, FILE_4_PATH) == RESULT


def test_yaml_to_json_result():
    assert generate_diff(FILE_3_PATH, FILE_2_PATH) == RESULT


def test_deep_generate_diff_json():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_2_DEEP_PATH) == DEEP_RESULT


def test_deep_generate_diff_yml():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_4_DEEP_PATH) == DEEP_RESULT


def test_deep_generate_cross_diff_json_yml():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_4_DEEP_PATH) == DEEP_RESULT


def test_deep_generate_cross_diff_yml_json():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_2_DEEP_PATH) == DEEP_RESULT


def test_generate_diff_json_format_plain():
    assert generate_diff(FILE_1_PATH, FILE_2_PATH,
                         format='plain') == RESULT_PLAIN


def test_generate_diff_yml_format_plain():
    assert generate_diff(FILE_3_PATH, FILE_4_PATH,
                         format='plain') == RESULT_PLAIN


def test_generate_cross_diff_json_yml_format_plain():
    assert generate_diff(FILE_1_PATH, FILE_4_PATH,
                         format='plain') == RESULT_PLAIN


def test_generate_cross_diff_yml_json_format_plain():
    assert generate_diff(FILE_3_PATH, FILE_2_PATH,
                         format='plain') == RESULT_PLAIN


def test_deep_generate_diff_json_format_plain():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_2_DEEP_PATH,
                         format='plain') == RESULT_DEEP_PLAIN


def test_deep_generate_diff_yml_format_plain():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_4_DEEP_PATH,
                         format='plain') == RESULT_DEEP_PLAIN


def test_deep_generate_cross_diff_json_yml_format_plain():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_4_DEEP_PATH,
                         format='plain') == RESULT_DEEP_PLAIN


def test_deep_generate_cross_diff_yml_json_format_plain():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_2_DEEP_PATH,
                         format='plain') == RESULT_DEEP_PLAIN


def test_generate_diff_json_format_json():
    assert generate_diff(FILE_1_PATH, FILE_2_PATH,
                         format='json') == RESULT_JSON_FORM


def test_generate_diff_yml_format_json():
    assert generate_diff(FILE_3_PATH, FILE_4_PATH,
                         format='json') == RESULT_JSON_FORM


def test_generate_cross_diff_json_yml_format_json():
    assert generate_diff(FILE_1_PATH, FILE_4_PATH,
                         format='json') == RESULT_JSON_FORM


def test_generate_cross_diff_yml_json_format_json():
    assert generate_diff(FILE_3_PATH, FILE_2_PATH,
                         format='json') == RESULT_JSON_FORM


def test_deep_generate_diff_json_format_json():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_2_DEEP_PATH,
                         format='json') == RESULT_JSON_DEEP_FORM


def test_deep_generate_diff_yml_format_json():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_4_DEEP_PATH,
                         format='json') == RESULT_JSON_DEEP_FORM


def test_deep_generate_cross_diff_json_yml_format_json():
    assert generate_diff(FILE_1_DEEP_PATH, FILE_4_DEEP_PATH,
                         format='json') == RESULT_JSON_DEEP_FORM


def test_deep_generate_cross_diff_yml_json_format_json():
    assert generate_diff(FILE_3_DEEP_PATH, FILE_2_DEEP_PATH,
                         format='json') == RESULT_JSON_DEEP_FORM
