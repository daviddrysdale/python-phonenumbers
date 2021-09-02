import os
import sys
import tempfile

from mypy import stubtest

if __name__ == "__main__":
    excluded = "\n".join(["phonenumbers.pb2.*"])  # exclude pb2/ (whitelist errors)
    with tempfile.NamedTemporaryFile("w+", delete=False) as file:
        file.write(excluded)
    ret = stubtest.test_stubs(stubtest.parse_options(["phonenumbers", "--whitelist", file.name]))
    os.remove(file.name)
    sys.exit(ret)
