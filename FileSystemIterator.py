import os


class FileSystemIterator:
    def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
        """
        Инициализация объекта
        :param root: корневой каталог
        :param only_files: итерироваться только по файлам (по умолчанию False)
        :param only_dirs: итерироваться только по директориям (по умолчанию False)
        :param pattern: итерироваться только по объектам
         файловой системы, содержащим в имени строку pattern (по умолчанию None)
        """
        self.root = root
        if root == 'None':
            raise FileNotFoundError
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.generator = self._generate()

    def __iter__(self):
        return self

    def __next__(self):
        if self.root == 'None':
            raise FileNotFoundError
        else:
            return next(self.generator)

    def _generate(self):
        for dirpath, dirnames, filenames in os.walk(self.root):
            if self.only_files and not self.only_dirs:
                for filename in filenames:
                    if self.pattern and self.pattern not in filename:
                        continue
                    yield os.path.join(dirpath, filename)
            elif self.only_dirs and not self.only_files:
                for dirname in dirnames:
                    if self.pattern and self.pattern not in dirname:
                        continue
                    yield os.path.join(dirpath, dirname)
            elif self.only_dirs and self.only_dirs:
                raise ValueError
            else:
                for filename in filenames:
                    if self.pattern and self.pattern not in filename:
                     continue
                    yield os.path.join(dirpath, filename)
                for dirname in dirnames:
                    if self.pattern and self.pattern not in dirname:
                        continue
                    yield os.path.join(dirpath, dirname)
