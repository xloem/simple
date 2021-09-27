import ast
import inspect

_builtin_hash = hash
_builtin_list = list
_builtin_type = type
_builtin_str = str
_builtin_repr = repr

def list(*items):
    '''Constructs and returns a list composed of the items passed.'''
    return _builtin_list(items)

def nposparams(callable):
    '''Returns a tuple, (mincount, maxcount), of positional parameters a function or constructor takes.'''
    try:
        nmin = 0
        noptional = 0
        for param in inspect.signature(callable).parameters.values():
            if param.kind is param.POSITIONAL_OR_KEYWORD or param.kind is param.POSITIONAL_ONLY:
                if param.default is inspect._empty:
                    nmin += 1
                else:
                    noptional += 1
            elif param.kind is param.VAR_POSITIONAL:
                noptional = float('inf')
    except ValueError:
        if callable is print:
            nmin, noptional = 0, float('inf')
        elif callable in (set, list, dict):
            nmin, noptional = 0, 1
        elif issubclass(callable, ast.AST):
            nmin = len(callable._fields)
            noptional = len(callable._attributes)
        else:
            raise
    return (nmin, nmin + noptional)

def hash(obj, type=None):
    '''Hashes AST objects and lists in addition to primitives.'''
    if isinstance(obj, ast.AST):
        return _builtin_hash(tuple(ast.AST, *(getattr(obj, field) for field in obj._fields)))
    elif type(obj) is list:
        return _builtin_hash(tuple(list, *obj))
    elif type(obj) is dict:
        return _builtin_hash(tuple(dict, *obj.items()))
    else:
        return _builtin_hash(obj)

def eq(obj, other):
    '''Compares AST objects for content equality in addition to primitives.'''
    if type(obj) != type(other):
        return False
    elif isinstance(obj, ast.AST):
        for field in obj._fields:
            if not eq(getattr(obj, field), getattr(other, field)):
                return False
        return True
    else:
        return obj == other

def repr(obj):
    '''Converts AST objects to strings in addition to primitives.'''
    if isinstance(obj, ast.AST):
        return ast.dump(obj, False)
    else:
        return _builtin_repr(obj)

def str(obj):
    '''Converts AST objects to strings in addition to primitives.'''
    if isinstance(obj, ast.AST):
        return ast.dump(obj, False)
    else:
        return _builtin_str(obj)

class hashed:
    '''Wraps an object with simple.hash and simple.eq for use in containers.'''
    def __init__(self, object):
        self.object = object
    def __hash__(self):
        return hash(self.object)
    def __eq__(self, other):
        if isinstance(other, hashed):
            other = other.object
        return eq(self.object, other)
    def __str__(self):
        return str(self)
    def __repr__(self):
        return repr(self)
