#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import inflect

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeIntInRange(0, 100000000000)

    p = inflect.engine()
    p.number_to_words(num)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()