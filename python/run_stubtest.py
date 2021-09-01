import os
import sys
import tempfile

from mypy import stubtest

if __name__ == "__main__":
    file_descriptor, file_name = tempfile.mkstemp(text=True)
    excluded = "\n".join(["phonenumbers.pb2.*"])  # exclude pb2/ (whitelist errors)
    with os.fdopen(file_descriptor, "w") as f:
        f.write(excluded)
    ret = stubtest.test_stubs(stubtest.parse_options(["phonenumbers", "--whitelist", file_name]))
    os.remove(file_name)
    sys.exit(ret)
