#!/usr/bin/python3
import atheris
import sys
from pydantic import ValidationError

with atheris.instrument_imports():
    import inflect

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    word_1 = fdp.ConsumeUnicodeNoSurrogates(100)
    word_2 = fdp.ConsumeUnicodeNoSurrogates(100)

    p = inflect.engine()

    try:
        p.compare(word_1, word_2)
    except ValidationError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()