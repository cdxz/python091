all:
	cc    -c -o acceler.o acceler.c
	cc    -c -o bltinmodule.o bltinmodule.c
	cc    -c -o ceval.o ceval.c
	cc    -c -o classobject.o classobject.c
	cc    -c -o compile.o compile.c
	cc    -c -o dictobject.o dictobject.c
	cc    -c -o errors.o errors.c
	cc    -c -o fgetsintr.o fgetsintr.c
	cc    -c -o fileobject.o fileobject.c
	cc    -c -o floatobject.o floatobject.c
	cc    -c -o frameobject.o frameobject.c
	cc    -c -o funcobject.o funcobject.c
	cc    -c -o graminit.o graminit.c
	cc    -c -o grammar1.o grammar1.c
	cc    -c -o import.o import.c
	cc    -c -o intobject.o intobject.c
	cc    -c -o intrcheck.o intrcheck.c
	cc    -c -o listnode.o listnode.c
	cc    -c -o listobject.o listobject.c
	cc    -c -o mathmodule.o mathmodule.c
	cc    -c -o methodobject.o methodobject.c
	cc    -c -o modsupport.o modsupport.c
	cc    -c -o moduleobject.o moduleobject.c
	cc    -c -o node.o node.c
	cc    -c -o object.o object.c
	cc    -c -o parser.o parser.c
	cc    -c -o parsetok.o parsetok.c
	cc    -c -o posixmodule.o posixmodule.c
	cc    -c -o regexp.o regexp.c
	cc    -c -o regexpmodule.o regexpmodule.c
	cc    -c -o strdup.o strdup.c
	cc    -c -o stringobject.o stringobject.c
	cc    -c -o structmember.o structmember.c
	cc    -c -o sysmodule.o sysmodule.c
	cc    -c -o timemodule.o timemodule.c
	cc    -c -o tokenizer.o tokenizer.c
	cc    -c -o traceback.o traceback.c
	cc    -c -o tupleobject.o tupleobject.c
	cc    -c -o typeobject.o typeobject.c
	rm -f libpython
	ar cr libpython acceler.o bltinmodule.o ceval.o classobject.o compile.o dictobject.o errors.o fgetsintr.o fileobject.o floatobject.o  frameobject.o funcobject.o  graminit.o grammar1.o import.o intobject.o intrcheck.o listnode.o listobject.o mathmodule.o methodobject.o modsupport.o moduleobject.o node.o object.o parser.o parsetok.o posixmodule.o regexp.o regexpmodule.o strdup.o  stringobject.o  structmember.o sysmodule.o timemodule.o tokenizer.o traceback.o tupleobject.o typeobject.o
	ranlib   libpython
	mv libpython libpython.a
	cc    -c -o pythonmain.o pythonmain.c
	cc    -c -o config.o config.c
	cc  pythonmain.o config.o libpython.a      -lm -o tmpython
	mv tmpython python


clean:
	-rm *.o *.a libpython tmpython python
