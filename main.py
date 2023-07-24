from file_system_iterator import FileSystemIterator
root = '/home/vova/Загрузки'
for item in FileSystemIterator(root, True, False, None):
    print(item)
print('#' * 50)


