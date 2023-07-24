import os

class FileSystemIterator:
    def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
        """
         Инициализация объекта
        :param root: корневой каталог
        :param only_files: итерироваться только по файлам (по умолчанию False)
        :param only_dirs: итерироваться только по директориям (по умолчанию False)
        :param pattern: итерироваться только по объектам файловой системы, содержащим в имени строку pattern (по умолчанию None)
        """
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_dir = self.stack.pop()
            for name in os.listdir(current_dir):
                path = os.path.join(current_dir, name)
                if os.path.isdir(path):
                    if not self.only_files:
                        if not self.only_dirs or name == self.pattern:
                            self.stack.append(path)
                elif not self.only_dirs:
                    if self.pattern is None or self.pattern in name:
                        return path
        raise StopIteration
iterator = FileSystemIterator('/home/vova/Загрузки')
for file_path in iterator:
    print(file_path)