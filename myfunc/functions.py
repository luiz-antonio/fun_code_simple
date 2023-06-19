import types
"""*******************************************************************************"""
# Fun_code_simple
#
##*  Functional programming library
#
#  http://www.lags.pro.br
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
# @author   LAGS luiz@lags.pro.br
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
#  @author - luiz@lags.pro.br
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
#  @author - luiz@lags.pro.br
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
    return lambda n: [  f(t) for t in range(n)]


##
# compose function - Compose two functions
# @author   LAGS luiz@lags.pro.br
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

