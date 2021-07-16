import check50
import check50.c

@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists) # only run this check if the exists check has passed
def prints_hello():
    """prints "hello, world\\n" """
    check50.run("python3 hello.py").stdout("[Hh]ello, [Ww]orld!?\n", regex=True).exit(0)

@check50.check(exists)
def id():
    """hello.py prints what you give it"""
    check50.run("python3 hello.py").stdin("foo").stdout("foo").stdin("bar").stdout("bar")