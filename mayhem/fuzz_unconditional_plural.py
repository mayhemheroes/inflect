#!/usr/bin/python3
import atheris
import sys
from pydantic import ValidationError

with atheris.instrument_imports():
    import inflect

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    word = fdp.ConsumeUnicodeNoSurrogates(100)

    p = inflect.engine()
    
    try:
        p.plural(word)
    except ValidationError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()