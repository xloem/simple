import ast

def Constant(const):
    return ast.Constant(const, None)

def Module(*statements):
    return ast.Module(statements, [])

def LoadSym(name):
    return ast.Name(name, ast.Load())

def StoreSym(name):
    return ast.Name(name, ast.Store())

def Call(funcsym, *params, **kwparams):
    return ast.Call(funcsym, params, [ast.keyword(arg, value) for arg, value in kwparams.items()])
