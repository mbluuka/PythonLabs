from ast import Num, arg
from glob import glob
from itertools import count
from tabnanny import verbose
from turtle import goto
from llvmlite import ir
import sys
import re

class SingleOP():
    def __init__(self, builder, module, left):
        self.builder = builder
        self.module = module
        self.left = left
    
class BinaryOP():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right
    
class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value
    
    def eval(self):
        if typeis == ir.IntType(32):
            i = ir.Constant(ir.IntType(32), int(self.value))
        else:
            i = ir.Constant(ir.FloatType(), float(self.value))
        return i

class Sum(BinaryOP):
    def eval(self):
        self.builder.add(self.left.eval(), self.right.eval())
        if typeis == ir.IntType(32):
            i = self.builder.add(self.left.eval(), self.right.eval())
        else:
            i = self.builder.fadd(self.left.eval(), self.right.eval())
        return i

class Sub(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        if typeis == ir.IntType(32):
            i = self.builder.sub(self.left.eval(), self.right.eval())
        else:
            i = self.builder.fsub(self.left.eval(), self.right.eval())
        return i

class Mul(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        if typeis == ir.IntType(32):
            i = self.builder.mul(self.left.eval(), self.right.eval())
        else:
            i = self.builder.fmul(self.left.eval(), self.right.eval())
        return i

class Div(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        #CHECKTYPE
        if typeis == ir.IntType(32):
            i = self.builder.sdiv(self.left.eval(), self.right.eval())
        else:
            i = self.builder.fdiv(self.left.eval(), self.right.eval())
        return i

class Equal(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('==', self.left.eval(), self.right.eval())
        return i

class More(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('>', self.left.eval(), self.right.eval())
        return i

class Less(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('<', self.left.eval(), self.right.eval())
        return i

class Gequal(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('>=', self.left.eval(), self.right.eval())
        return i

class Lequal(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('<=', self.left.eval(), self.right.eval())
        return i

class Not_equal(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.icmp_signed('!=', self.left.eval(), self.right.eval())
        return i

class And_(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.and_(self.left.eval(), self.right.eval())
        return i
    
class Or_(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.or_(self.left.eval(), self.right.eval())
        return i

class Not_(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        i = self.builder.not_(self.left.eval(), self.right.eval())
        return i

class if_then(BinaryOP):
    def eval(self):
        self.builder = b_func(self.builder)
        with self.builder,if_then(self.left.eval()):
            i = self.right.eval()
        return i

class While():
    def __init__(self, builder, module, boolean, right):
        self.builder = builder
        self.module = module
        self.boolean = boolean
        self.right = right
    
    def eval(self):
        global goto
        i = None
        self.builder = b_func(self.builder)
        for x in range(5):
            with self.builder,if_then(self.boolean.eval()):
                if goto == "break":
                    break
                elif goto == "continue":
                    continue
                i = self.right.eval()
        return i

class Eval_(BinaryOP):
    def eval(self):
        i = self.left.eval()
        y = self.left.eval()
        return i

func_num = 0

class Print():
    def __init__(self, builder, module, printf, right):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.right = right
    
    def eval(self):
        value = self.value.eval()
        
        voidptr_ty = ir.IntType(8).aspointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
        global func_num
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr" + str(func_num))
        func_num+=1
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt

        self.builder = b_func(self.builder)
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        self.builder.call(self.printf, [fmt_arg, value])

class Func_():
    def __init__(self, builder, module, func_name, param1, stmts):
        self.builder = builder
        self.module = module
        self.func_name = func_name
        self.param1 = param1
        self.stmts = stmts
    
    def eval():
        global func2
        global builder2
        global ptr
        global var_num
        global value_num
        global count
        global flag
        global func_return
        i = None

        func_type2 = ir.FunctionType(ir.Type(32), [ir.IntType(32), ir.IntType(32)])
        func2 = ir.Function(self.module, func_type2, name="function")
        block2 = func2.append_basic_block(name="entry")
        builder2 = ir.IRBuilder(block2)
        #STOREARGS - Нужно переделать на другие арги
        arg1, arg2 = func2.args
        ptr[var_num] = ir.GlobalVariable(self.module, ir.IntType(32), self.param1[0].value)
        ptr[var_num].linkage = 'internal'
        builder2.store(arg1, ptr[var_num])
        var_num += 1
        ptr[var_num] = ir.GlobalVariable(self.module, ir.IntType(32), self.param1[1].value)
        ptr[var_num].linkage = 'internal'
        builder2.store(arg1, ptr[var_num])
        var_num += 1

        flag = True
        y = self.stmts.eval()
        flag = False

        func_return = self.func_name.value
        for x in range(0, var_num):
            if("@\""+self.func_name.value+"\""in str(ptr[x])):
                i = builder2.load(ptr[x])
        ii = builder2.ret(i)
        if ii == None:
            sys.stderr.write("Error returning in function")
            sys.exit(1)
        return ii

class Call_():
    def __init__(self, builder, module, func_name, param):
        self.builder = builder
        self.module = module
        self.func_name = func_name
        self.param = param
    
    def eval(self):
        global func2

        self.builder = b_func(self.builder)
        for x in range(0, var_num):
            if("@\""+self.param[0].value+"\""in str(ptr[x])):
                arg1 = self.builder.load(ptr[x])
        
        for x in range(0, var_num):
            if("@\""+self.param[1].value+"\""in str(ptr[x])):
                arg2 = self.builder.load(ptr[x])
        
        i = self.builder.call(func2, [arg1, arg2])
        return i
