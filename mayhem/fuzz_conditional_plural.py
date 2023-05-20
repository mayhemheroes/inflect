#!/usr/bin/python3
import atheris
import sys
from pydantic import ValidationError

with atheris.instrument_imports():
    import inflect


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeIntInRange(0, 10000000000000)
    word = fdp.ConsumeUnicodeNoSurrogates(100)
    p = inflect.engine()

    try:
        p.plural(word, num)
    except ValidationError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()