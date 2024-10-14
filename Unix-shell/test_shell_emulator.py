import os
import tarfile
import pytest
from unittest import mock
from io import StringIO
import xml.etree.ElementTree as ET
from shell_emulator import ShellEmulator

@pytest.fixture
def shell():
    # Фикстура для создания экземпляра ShellEmulator для каждого теста
    with mock.patch('tarfile.open'):
        return ShellEmulator("testuser", "localhost", "testfs.tar", "log.xml")


@mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
def test_ls(mocked_listdir, shell, capsys):
    shell.ls()
    captured = capsys.readouterr()
    assert captured.out == "file1.txt\nfile2.txt\n"
    assert shell.current_dir == "/"
    assert shell.vfs['file1.txt'] == 'file1.txt'


@mock.patch('os.listdir', return_value=['dir1', 'dir2'])
def test_cd_valid_dir(mocked_listdir, shell):
    shell.vfs = {'dir1': 'dir1', 'dir2': 'dir2'}  # добавляем директории в vfs
    shell.cd('/')
    assert shell.current_dir == '/'


def test_cd_invalid_dir(shell, capsys):
    shell.cd('nonexistent_dir')
    captured = capsys.readouterr()
    assert captured.out == "cd: no such file or directory: nonexistent_dir\n"
    assert shell.current_dir == "/"


def test_who(shell, capsys):
    shell.who()
    captured = capsys.readouterr()
    assert captured.out == "testuser\n"


@mock.patch('builtins.open', new_callable=mock.mock_open, read_data="Line1\nLine2\nLine3\n")
def test_tac(mocked_open, shell, capsys):
    shell.tac("testfile.txt")
    captured = capsys.readouterr()
    assert captured.out == "Line3Line2Line1\n"


def test_exit(shell):
    with mock.patch('builtins.exit') as mocked_exit:
        shell.exit()
        mocked_exit.assert_called_once_with(0)


# Тесты для проверки логирования
def test_log_creation(shell):
    assert shell.root.tag == "log"
    assert len(shell.root) == 1  # Первый элемент лога должен быть началом сессии

def test_log_action(shell):
    shell.log_action("Test action")
    assert shell.root[-1].text == "Test action"


@mock.patch('xml.etree.ElementTree.ElementTree.write')
def test_save_log(mocked_write, shell):
    shell.save_log()
    mocked_write.assert_called_once()
