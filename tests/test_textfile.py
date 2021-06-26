from textfile import __version__
import textfile
from pytest import fixture
import pytest


_ENCODING = 'utf-8'
KENJIMARU = 'kenjimaru😃'


def test_version():
    assert __version__ == '0.1.3'


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


class TestAppendFunction:
    @fixture
    def file_with_content(self, tmp_file):
        with open(tmp_file, "w", encoding=_ENCODING) as writer:
            writer.write(KENJIMARU)

        return tmp_file

    def test_pathlib_path(self, file_with_content):
        textfile.append(file_with_content, KENJIMARU)
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == KENJIMARU * 2

    def test_path_string(self, file_with_content):
        textfile.append(str(file_with_content), KENJIMARU)
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == KENJIMARU * 2

    def test_set_file_parameter_to_none_should_type_error(self):
        with pytest.raises(TypeError):
            textfile.append(None, KENJIMARU)

    def test_set_s_parameter_to_none_should_type_error(self, file_with_content):
        with pytest.raises(TypeError):
            textfile.append(file_with_content, None)

    def test_append_empty_string_should_not_vary_content(self, file_with_content):
        textfile.append(file_with_content, '')
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == KENJIMARU

    def test_append_empty_string_to_nonexistence_file_should_create_empty_file(self, tmp_file):
        textfile.append(tmp_file, '')
        assert tmp_file.exists()
        assert tmp_file.stat().st_size == 0

    def test_append_to_nonexistent_directory_should_file_not_found_error(self, tmp_path):
        p = tmp_path / 'not_exist' / 'tmp.txt'
        with pytest.raises(FileNotFoundError):
            textfile.append(p, KENJIMARU)

    def test_create_file_in_not_permitted_dir_should_permission_error(self, tmp_path):
        p = tmp_path / 'not_permitted'
        p.mkdir(mode=0o444)
        with pytest.raises(PermissionError):
            textfile.append(p / 'tmp.txt', KENJIMARU)

    def test_append_to_not_permitted_file_should_permission_error(self, file_with_content):
        file_with_content.chmod(0o444)
        with pytest.raises(PermissionError):
            textfile.append(file_with_content, KENJIMARU)

    def test_append_target_is_directory_should_is_a_directory_error(self, tmp_path):
        with pytest.raises(IsADirectoryError):
            textfile.append(tmp_path, KENJIMARU)


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


class TestReplace:
    @fixture
    def file_with_content(self, tmp_file):
        content = KENJIMARU * 2
        with open(tmp_file, 'w', encoding=_ENCODING) as writer:
            writer.write(content)

        return tmp_file

    def test_pathlib_path(self, file_with_content):
        textfile.replace(file_with_content, '😃', '🙃')
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == 'kenjimaru🙃kenjimaru🙃'

    def test_path_string(self, file_with_content):
        textfile.replace(str(file_with_content), '😃', '🙃')
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == 'kenjimaru🙃kenjimaru🙃'

    def test_none_parameter_should_type_error(self, file_with_content):
        with pytest.raises(TypeError):
            textfile.replace(None, '😃', '🙃')

        with pytest.raises(TypeError):
            textfile.replace(file_with_content, None, '🙃')

        with pytest.raises(TypeError):
            textfile.replace(file_with_content, '😃', None)

    def test_set_old_parameter_to_empty(self, file_with_content):
        textfile.replace(file_with_content, '', '_')
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == '_k_e_n_j_i_m_a_r_u_😃_k_e_n_j_i_m_a_r_u_😃_'

    def test_set_new_parameter_to_empty(self, file_with_content):
        textfile.replace(file_with_content, '😃', '')
        with open(file_with_content, encoding=_ENCODING) as reader:
            assert reader.read() == 'kenjimaru' * 2

    def test_not_permitted_file_should_permission_error(self, file_with_content):
        file_with_content.chmod(0o444)
        with pytest.raises(PermissionError):
            textfile.replace(file_with_content, '😃', '🙃')

        file_with_content.chmod(0o222)
        with pytest.raises(PermissionError):
            textfile.replace(file_with_content, '😃', '🙃')

    def test_target_is_directory_should_is_a_directory_error(self, tmp_path):
        with pytest.raises(IsADirectoryError):
            textfile.replace(tmp_path, '😃', '🙃')

    def test_file_not_exist_should_file_not_found_error(self, tmp_path):
        p = tmp_path / 'tmp.txt'
        with pytest.raises(FileNotFoundError):
            textfile.replace(p, '😃', '🙃')


