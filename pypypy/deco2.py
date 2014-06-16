def function(a):
    def function1(b):
        return a(b)+'s'
    return function1
def function3(d):
    def function4(e):
        return d(e)+' end this'
    return function4

@function3
@function
def function2(c):
    return 's'+c
