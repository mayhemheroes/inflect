#!/usr/bin/python3
import atheris
import sys
from pydantic import ValidationError

with atheris.instrument_imports():
    import inflect

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    word_1 = RandomString(fdp, 1, 100)
    word_2 = RandomString(fdp, 1, 100)

    p = inflect.engine()

    try:
        p.compare(word_1, word_2)
    except ValidationError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()