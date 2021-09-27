# simple

This is a python package for simple relations that are missing from the library and are helpful to the runtime design of code.

## simple.list

Constructs and returns a list ocmposed of the items passed.

`simple.list(1,2,3) == list([1,2,3])`

## simple.nposparams

Returns a tuple, (mincount, maxcount), of positional parameters a function or constructor takes.

Presently mostly handles user-defined functions and the AST constructors, and a couple builtins.

`simple.nposparams(ast.Expr) == (1,5)`

## simple.hash

Hashes AST objects, lists, and dicts in addition to primitives.

Line numbering is ignored when hashing.

`simple.hash({1:3})`

## simple.eq

Compares AST objects for content equality in addition to primitives.

Line numbering is ignored when comparing.

`simple.eq(ast.parse(''), ast.Module([],[])) == True`

## simple.repr, simple.str

Converts AST objects to strings in addition to primitives.

AST objects are passed to ast.dump(,False).
Primitives are passed to repr or str respectively.

`simple.str(ast.parse('')) == 'Module([], [])'`

## simple.hashed

Wraps an object with simple.hash, simple.eq, etc for use in containers.

```
wrapped_dict = simple.hashed({1: 3})
set().add(wrapped_dict)
wrapped_dict.object == {1: 3}
str(wrapped_dict) == '{1: 3}'
```

## simple.ast

Slightly simplified versions of AST constructors for tighter introspective discovery or other use.

- `simple.ast.Constant(const)`
- `simple.ast.Module(*statements)`
- `simple.ast.LoadSym(name)`
- `simple.ast.StoreSym(name)`
- `simple.ast.Call(funcsym, *params, **kwparams)`

```
simple.ast.Module(
    ast.Expr(simple.ast.Call(
        simple.ast.LoadSym('print'), simple.ast.Constant('hello world')
    ))
)
```
