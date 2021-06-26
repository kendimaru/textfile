from textfile import __version__
import textfile
from pytest import fixture
import pytest


KENJIMARU = 'kenjimaru😃'


def test_version():
    assert __version__ == '0.1.1'


@fixture
def tmp_file(tmp_path):
    return tmp_path / 'tmp.txt'


class TestWriteFunction:
    def test_pathlib_path(self, tmp_file):
        textfile.write(tmp_file, KENJIMARU)

        with open(tmp_file, encoding='utf-8') as reader:
            written = reader.read()

        assert written == KENJIMARU

    def test_path_string(self, tmp_file):
        textfile.write(str(tmp_file), KENJIMARU)

        with open(tmp_file, encoding='utf-8') as reader:
            written = reader.read()

        assert written == KENJIMARU

    def test_set_file_parameter_to_none_should_type_error(self):
        with pytest.raises(TypeError):
            textfile.write(None, '')

    def test_set_s_parameter_to_none_should_type_error(self, tmp_file):
        with pytest.raises(TypeError):
            textfile.write(tmp_file, None)

    def test_write_empty_string_should_only_create_file(self, tmp_file):
        textfile.write(tmp_file, '')
        assert tmp_file.exists()

    def test_write_empty_string_should_erase_content_of_already_existing_file(self, tmp_file):
        textfile.write(tmp_file, KENJIMARU)
        textfile.write(tmp_file, '')
        with open(tmp_file, encoding='utf-8') as reader:
            assert reader.read() == ''

    def test_write_to_nonexistent_directory_should_file_not_found_error(self, tmp_path):
        file_in_nonexistent_directory = tmp_path / 'not_exist' / 'tmp.txt'

        with pytest.raises(FileNotFoundError):
            textfile.write(file_in_nonexistent_directory, KENJIMARU)

    def test_create_file_in_not_permitted_dir_should_permission_error(self, tmp_path):
        read_only_dir = tmp_path / 'readonly'
        read_only_dir.mkdir(mode=0o444)

        with pytest.raises(PermissionError):
            textfile.write(read_only_dir / 'tmp.txt', KENJIMARU)

        print(read_only_dir)

    def test_write_target_is_directory_should_is_a_directory_error(self, tmp_path):
        with pytest.raises(IsADirectoryError):
            textfile.write(tmp_path, KENJIMARU)


class TestReadFunction:
    def test_pathlib_path(self, tmp_file):
        textfile.write(tmp_file, KENJIMARU)
        assert textfile.read(tmp_file), KENJIMARU

    def test_path_string(self, tmp_file):
        textfile.write(tmp_file, KENJIMARU)
        assert textfile.read(tmp_file.__fspath__(), KENJIMARU)

    def test_set_file_parameter_to_none_should_type_error(self):
        with pytest.raises(TypeError):
            textfile.read(None)

    def test_read_from_empty_file(self, tmp_file):
        textfile.write(tmp_file, '')
        assert textfile.read(tmp_file) == ''

    def test_read_from_nonexistence_file_should_file_not_found_error(self, tmp_file):
        with pytest.raises(FileNotFoundError):
            textfile.read(tmp_file)

    def test_read_from_nonexistence_file_with_silent_true_should_get_empty_string(self, tmp_file):
        assert textfile.read(tmp_file, silent=True) == ''

    def test_read_from_directory_should_is_a_directory_error(self, tmp_path):
        with pytest.raises(IsADirectoryError):
            textfile.read(tmp_path)

    def test_read_from_not_permitted_file_should_permission_error(self, tmp_file):
        textfile.write(tmp_file, KENJIMARU)
        tmp_file.chmod(0o222)
        with pytest.raises(PermissionError):
            textfile.read(tmp_file)


