from textfile import __version__
import textfile


KENJIMARU = 'kenjimaru'


def test_version():
    assert __version__ == '0.1.0'


class TestWriteFunction:

    def test_pathlib_path(self, tmp_path):
        p = tmp_path / 'tmp.txt'
        textfile.write(p, KENJIMARU)

        with open(p, encoding='utf-8') as f:
            written = f.read()

        assert written == KENJIMARU

    def test_path_string(self, tmp_path):
        p = tmp_path / 'tmp.txt'
        textfile.write(str(p), KENJIMARU)

        with open(p, encoding='utf-8') as f:
            written = f.read()

        assert written == KENJIMARU

    def test_write_empty_string_should_only_create_file(self):
        raise NotImplemented()

    def test_write_empty_string_should_erase_content_of_already_existing_file(self):
        raise NotImplemented()

    def test_write_to_nonexist_directory_should_file_not_found_error(self):
        raise NotImplemented()

    def test_create_file_in_not_permitted_dir_should_permission_error(self):
        raise NotImplemented()


