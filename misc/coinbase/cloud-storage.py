# cloud storage system

# Level 1: 添加文件并记录文件大小； 复制文件； retrieve文件并返回
# Level 2: 找到符合prefix 和suffix的文件，用文件大小排序后返回

# level 3: 添加用户和用户拥有得存储空间； 给定用户添加文件，超过存储空间上限则不能操作
# Level 4: 压缩和解压文件

class CloudStorageSystem:
    def __init__(self):
        self.files = {}  # 存储文件名和文件大小的字典
        self.users = {}  # 存储用户名和用户存储空间的字典
    def add_file(self, file_name, file_size):
        """添加文件并记录文件大小"""
        self.files[file_name] = file_size
    def copy_file(self, source_file, destination_file):
        """复制文件"""
        if source_file in self.files:
            self.files[destination_file] = self.files[source_file]
        else:
            raise ValueError("Source file does not exist")
    def retrieve_file(self, file_name):
        """检索文件并返回文件大小"""
        if file_name in self.files:
            return self.files[file_name]
        else:
            raise ValueError("File does not exist")
    def find_files_by_prefix_and_suffix(self, prefix, suffix):
        """根据前缀和后缀查找文件，并按文件大小排序"""
        matched_files = [(file_name, file_size) for file_name, file_size in self.files.items()
                          if file_name.startswith(prefix) and file_name.endswith(suffix)]
        matched_files.sort(key=lambda x: x[1])
        return matched_files
    def add_user(self, user_name, storage_limit):
        """添加用户并设置存储空间上限"""
        self.users[user_name] = {'storage_limit': storage_limit, 'used_storage': 0}
    def add_file_for_user(self, user_name, file_name, file_size):
        """为用户添加文件，检查是否超过存储空间上限"""
        if user_name not in self.users:
            raise ValueError("User does not exist")
        if self.users[user_name]['used_storage'] + file_size > self.users[user_name]['storage_limit']:
            raise ValueError("Storage limit exceeded")
        self.files[file_name] = file_size
        self.users[user_name]['used_storage'] += file_size
    def compress_file(self, file_name, compression_ratio):
        """压缩文件"""
        if file_name not in self.files:
            raise ValueError("File does not exist")
        self.files[file_name] = int(self.files[file_name] * compression_ratio)
    def decompress_file(self, file_name, decompression_ratio):
        """解压文件"""
        if file_name not in self.files:
            raise ValueError("File does not exist")
        self.files[file_name] = int(self.files[file_name] * decompression_ratio)