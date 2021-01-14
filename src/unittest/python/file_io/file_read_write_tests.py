from unittest import TestCase, mock
from file_io.file_read_write import rm


class FileIoTest(TestCase):

    @mock.patch('file_io.file_read_write.os.path')
    @mock.patch('file_io.file_read_write.os')
    def test_file_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = True

        rm('foo')
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('foo')

    @mock.patch('file_io.file_read_write.os.path')
    @mock.patch('file_io.file_read_write.os')
    def test_file_rm_not_called(self, mock_os, mock_path):
        mock_path.isfile.return_value = False

        rm('foo')
        # test that rm called os.remove with the right parameters
        self.assertFalse(mock_os.remove.called, ''' 
                Tried to remove when file not present.''')
