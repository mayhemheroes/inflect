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

    word = RandomString(fdp, 1, 100)

    p = inflect.engine()
    
    try:
        p.plural(word)
    except ValidationError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()