from struct import unpack

HANDLE = -1 # Anonymous

# Memory map configuration, as taken from scs-telemetry-common.hpp
MM_SIZE = 32*1024
MM_NAME = 'SCSTelemetry'

# Types configuration; values as taken from scs-telemetry-common.hpp
MM_TYPES = {
    'bool': {
        'size': 1,
        'proc_func': lambda b: unpack('?', b)[0]
    },
    'bool2': {
        'size': 2,
        'proc_func': lambda b: unpack('2?', b)
    },
    'bool16': {
        'size': 16,
        'proc_func': lambda b: unpack('16?', b)
    },
    'string': {
        'size': 64,
        'proc_func': lambda s: s.decode().rstrip('\x00')
    },
    'string16': {
        'size': 16,
        'proc_func': lambda s: s.decode().rstrip('\x00')
    },
    'string32': {
        'size': 32,
        'proc_func': lambda s: s.decode().rstrip('\x00')
    },
    'int': {
        'size': 4,
        'proc_func': lambda i: unpack('i', i)[0]
    },
    'int32': {
        'size': 4*32,
        'proc_func': lambda i: unpack('32i', i)
    },
    'uint': {
        'size': 4,
        'proc_func': lambda u: unpack('I', u)[0]
    },
    'uint16': {
        'size': 4*16,
        'proc_func': lambda u: unpack('16I', u)
    },
    'uint32': {
        'size': 4*32,
        'proc_func': lambda u: unpack('32I', u)
    },
    'double': {
        'size': 8,
        'proc_func': lambda d: unpack('d', d)
    },
    'long long': {
        'size': 8,
        'proc_func': lambda l: unpack('q', l)[0]
    },
    'unsigned long long': {
        'size': 8,
        'proc_func': lambda l: unpack('Q', l)[0]
    },
    'float': {
        'size': 4,
        'proc_func': lambda f: unpack('f', f)[0]
    },
    'float8': {
        'size': 4*8,
        'proc_func': lambda f: unpack('8f', f)
    },
    'float16' : {
        'size': 4*16,
        'proc_func': lambda f: unpack('16f', f)
    },
    'float24': {
        'size': 4*24,
        'proc_func': lambda f: unpack('24f', f)
    }
}

SUBSTANCE_SIZE = 25