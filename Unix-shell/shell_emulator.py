import os
import tarfile
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime


class ShellEmulator:
    def __init__(self, user, hostname, fs_path, logfile):
        self.user = user
        self.hostname = hostname
        self.logfile = logfile
        self.current_dir = "/"
        self.fs_path = fs_path
        self.vfs = self._load_filesystem(fs_path)
        self.root = ET.Element("log")
        self.log_action(f"Session started by {self.user}.")

    def _load_filesystem(self, fs_path):
        # Разархивируем файловую систему в память
        vfs = {}
        with tarfile.open(fs_path, 'r') as tar:
            tar.extractall("/programs/tmp/emulator_fs")
            for member in tar.getmembers():
                vfs[member.name] = member
        return vfs

    def log_action(self, action):
        log_entry = ET.SubElement(self.root, "action", user=self.user, time=str(datetime.now()))
        log_entry.text = action

    def save_log(self):
        tree = ET.ElementTree(self.root)
        with open(self.logfile, 'wb') as f:
            tree.write(f)

    def prompt(self):
        return f"{self.user}@{self.hostname}:{self.current_dir}$ "

    def ls(self):
        try:
            if self.current_dir == "/":
                files = os.listdir("/programs/tmp/emulator_fs")
            else:
                files = os.listdir(self.current_dir)
            for file in files:
                self.vfs[file] = file  # Добавляем файлы в vfs
            print("\n".join(files))
            self.log_action(f"Executed ls in {self.current_dir}.")
        except FileNotFoundError:
            print(f"ls: cannot access '{self.current_dir}': No such file or directory")
            self.log_action(f"Failed to execute ls in {self.current_dir}.")

    def cd(self, path):
        if path == "/":
            self.current_dir = "/"
        elif path in self.vfs and os.path.isdir(os.path.join(self.current_dir, path)):  # Проверяем директорию в vfs
            self.current_dir = path
            self.log_action(f"Changed directory to {path}.")
        else:
            print(f"cd: no such file or directory: {path}")
            self.log_action(f"Failed to change directory to {path}.")

    def who(self):
        print(self.user)
        self.log_action("Executed who.")

    def tac(self, filepath):
        try:
            with open(os.path.join(self.current_dir, filepath), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                lines.reverse()  # Переворачиваем строки
                print("".join([line.rstrip() for line in lines]))  # Убираем лишний символ новой строки
            self.log_action(f"Executed tac on {filepath}.")
        except FileNotFoundError:
            print(f"tac: {filepath}: No such file or directory")
            self.log_action(f"Failed to execute tac on {filepath}.")

    def exit(self):
        self.log_action("Session ended.")
        self.save_log()
        print("Goodbye!")
        exit(0)


def rev(h):
    g: str = ""
    for element in h:
        g += element
    return g


def main():
    parser = argparse.ArgumentParser(description="UNIX shell emulator")
    parser.add_argument("--user", required=True, help="Username for the session")
    parser.add_argument("--hostname", required=True, help="Hostname for the session")
    parser.add_argument("--fs", required=True, help="Path to the virtual filesystem tar archive")
    parser.add_argument("--logfile", required=True, help="Path to the log file")
    args = parser.parse_args()

    shell = ShellEmulator(args.user, args.hostname, args.fs, args.logfile)

    while True:
        command = input(shell.prompt()).strip().split()
        if not command:
            continue
        if command[0] == "ls":
            shell.ls()
        elif command[0] == "cd":
            if len(command) > 1:
                shell.cd(command[1])
            else:
                print("cd: missing operand")
        elif command[0] == "who":
            shell.who()
        elif command[0] == "tac":
            if len(command) > 1:
                shell.tac(command[1])
            else:
                print("tac: missing operand")
        elif command[0] == "exit":
            shell.exit()
        else:
            print(f"{command[0]}: command not found")


if __name__ == "__main__":
    main()
