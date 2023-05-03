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

    num = fdp.ConsumeIntInRange(0, 10000000000000)
    word = RandomString(fdp, 1, 100)

    p = inflect.engine()

    try:
        p.plural(word, num)
    except ValidationError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()