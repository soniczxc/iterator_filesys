from file_system_iterator import FileSystemIterator
root = './tests'
for item in FileSystemIterator(root, False, True, None):
    print(item)
print('#' * 50)


