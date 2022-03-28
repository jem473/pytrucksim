from mmap import mmap, ACCESS_READ
from os import SEEK_CUR

class BinaryMemoryMap:
    def __init__(self, descriptor: int, name: str, size: int, types):
        self.descriptor = descriptor
        self.name = name
        self.size = size
        self.types = types
    
    def update(self):
        self.mm = mmap(self.descriptor, self.size, self.name, ACCESS_READ)
    
    def seek(self, offset):
        self.mm.seek(offset)
    
    def advance(self, offset):
        self.mm.seek(offset, SEEK_CUR)
    
    def current_offset(self):
        return self.mm.tell()
    
    def read(self, _type):
        return self.types[_type]['proc_func'](self.mm.read(self.types[_type]['size']))