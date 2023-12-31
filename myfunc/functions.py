import types
import inspect
from pymonad import maybe
from pymonad.io import IO
from pymonad import list
from pymonad.monad import Monad
from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing, Option
import operator
from functools import lru_cache
from functools import partial
from oslash import Just
from oslash import Nothing
from oslash import list






"""*******************************************************************************"""
# Fun_code_simple
#
##*  Simple Functional Programming Library
#
#  http://www.lags.dev
#
#  Luiz Antonio Garcia Simões (LAGS)
#
#  This file is free for use of any kind and is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
""" ****************************************************************************** """
# **
# **

##
#  id function - Return the unique first parameter
# @author   LAGS luiz@lags.dev
#
# @example id(3) => returns 3
#
# @param x any - the element
#
##

def id(x : any) -> any:
    return x

##
#
#  idCPS  function  - id function in CPS (Continuation Passing Style (CPS)
#  @author - luiz@lags.dev
#
# @example: idCPS(3, alert)  -> shows 3
# @param: any x (The element)
# @param: function cont
#
# @return  function(x)
##
def function(x: any, cont: callable) -> callable:
    return function(x)

##
#
#  makeTimesDo function  - Make a function to execute nTimes another function later
#  @author - luiz@lags.dev
#
# @example: var log5times = timesDo(5, function(n) { Logger.log(n);});
#
# @example:  fun = makeTimesDo(id)
#            print(fun(10))
#
# @param: any x (The element)
# @param: function fun
#
# @return  function(x)
##

def makeTimesDo(f: callable) -> any:
    return lambda n: [f(t) for t in range(n)]

##
# compose function - Compose two functions
# @author   LAGS luiz@lags.dev
#
# @example:  var inc = function(a) { return a + 1 };
#           var double = function(b) { return b + b;};
#          var doubleAndInc = compose(inc, double);
#          alert(doubleAndInc(3)); // displays 7
#
#           f(x) = x + 1;
#           g(x) = 2x;
#          f(g(x)) = g(x) + 1;
#           f(g(x)) = 2x + 1;
#
# @return {function} A composed function for the param functions.
#
##
def compose(*funs) -> callable:
    return (lambda x:
        x if len(funs) == 0
         else compose(*funs[:-1])(funs[-1](x)))



##
# makeSingleton function - Use a function to generate
# @author   LAGS luiz@lags.dev
#
# @example: var
#           def func():
#               return 5
#
#          x = makeSingleton(func)
#          print(x)
#
# @return {function} A singleton function.
#
##
def makeSingleton(f: callable) -> callable:
    value = None
    def internal():
        nonlocal value
        if value is None:
            value = f()
        return value
    return internal

##
# makeCounter function - function to generate a counter
# @author   LAGS luiz@lags.dev
#
# @param: initial - value to be incrmented
# @param: increment - value to increment
#
# @return {function} A singleton function.
#
##
def makeCounter(initial: int, increment: int) -> callable:
    value = initial
    incr = increment
    if value is None:
        value = 0
    if incr is None:
        incr = 1
    def counter() -> int :
        nonlocal value
        nonlocal incr
        value += incr
        return value
    return counter

##
# makeMemoised function - function to make a cached function -useful for 'pue functions' only
# @author   LAGS luiz@lags.dev
#
# @param: fun - function to cache results
#
# @return {function} A function.
#
# @exemplo:
# def doue(x):
#     return 2 * x
# dob = makeMemoised(doue)
# print( dob(2))
# print( dob(5))
#
#  Obs note que o primeiro parâmetro da funçã serve como índice
#
##
def makeMemoised(func: callable) -> callable:
    myresults = {}
    kwd_mark = object()
    def cached(*args):
        nonlocal myresults
        key = args[0]
        res = myresults.get(key)
        if res is None:
            myresults[key] = func(key)
        return myresults.get(key)
    return cached

##
# curry function - Make functions especialized from another by parameter fixing
# @author   LAGS luiz@lags.dev
#
# @example:  var inc = curry(
#               function add(a,b):
#                 return a + b
#               }
#           ,1)
#           print(inc(6)); // displays 1 + 6
#
# @return {function} A modified function
#
##
def curry(func: callable, argini: any) -> callable:
    fixed_arg = argini
    def internal(arg) :
        nonlocal fixed_arg
        return func(fixed_arg, arg )
    return internal

##
# curryCPS function - versão do curry para CPS (continuation)
# @author   LAGS luiz@lags.dev
#
#
# @return {function} A modified function
#
##
def curryCPS(fun: callable , callback:callable) -> callable:
    def internal( first: any ) -> callable:
        return (fun, callback)


##
# getCallerName function - get the function name of the function that call the current
# @author   LAGS luiz@lags.dev
#
#
# @return a caller function name
#
##
def getCallerName() -> str:
    return inspect.stack()[2][3]


##
# getMyName function - get the name od current funcion
# @author   LAGS luiz@lags.dev
#
#
# @return the function name
#
##
def getMyName() -> str:
    return inspect.stack()[1][3]

##
# getParamNames function - get the param names of a funcion
# @author   LAGS luiz@lags.dev
#
# @param: a function
# @return a caller function name
#
##
def getParamNames(fun: callable) -> tuple:
    return inspect.signature(fun)

##
# getMyParamNames function - get the param names of a funcion
# @author   LAGS luiz@lags.dev
#
# @return a param function name
#
##
def getMyParamNames() -> tuple:
    nme: str = getCallerName()
    fun: callable = globals().get(nme)
    return inspect.signature(fun)

##
# makeExecuteOnce function - get the param names of a funcion
# @author   LAGS luiz@lags.dev
#
# @param: func - a function which is "excluded" after its first execution
#
# @return a function that can be executed (the function param, really) only one time
#
##
def makeExecuteOnce(fun: callable) -> callable:
    def inner_fun(*args) -> callable:
        nonlocal fun
        f: callable = fun
        fun = lambda *args : None
        return f(*args)
    return inner_fun

##
# Z function - (Z combinator) versão do Y combinator para python
# @author   LAGS luiz@lags.dev
#
# @param: func - a function which is "excluded" after its first execution
#
# @example: fac = lambda f: lambda n: 1 if n <= 1 else n * f(n - 1)
#           print(Z(fac)(5))
#
# @return a function that can be executed (the function param, really) only one time
#
##
Z = lambda f: lambda *args: f(Z(f))(*args)


##
# unit function - Cria uma função que devolve o valor passado
#
# @author   LAGS luiz@lags.dev
#
# @param: value - o valor que a função criada sempre retorna
#
# @example: func = unit("abcd")
#           print(func())    # returns "abcd"
#
# @return a function that can be executed (the function param, really) only one time
# @docs:  https://pypi.org/project/PyMonad/
##
def unit( value: any, fun: callable) -> callable:
    unt = Just.unit(value)
    result = unt >> fun
    return result

##
# bind function - Cria uma função func applied to the parameter monadicValue
#
# @author   LAGS luiz@lags.dev
#
# @param: monadic_value - o valor a ser aplicado na função
# @param:         func  - a função a ser aplicada no monadic_value
#
# @example: print(bind(3, lambda x: x +2))
#
# @return a function that can be executed (the function param, really) only one time
#
##
def bind_list(monadic_value: list[any], func: callable) -> any:
    ls = list(monadic_value)
    ls.bind(lambda x: list([x, -x]))
    return ls

##
# xxx function - xxxx
#
# @author   LAGS luiz@lags.dev
#
# @param:xxx

#
# @example: xxxx
#
# @return xxxx
#
##





