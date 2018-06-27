#!/usr/bin/env python
# Find the real location of this script and invoke the python file there named
# for how this script was called.

import os.path
import sys

# Find the actual executable
self = os.path.realpath(sys.argv[0])
command_name = os.path.basename(sys.argv[0])
bin_root = os.path.dirname(self)
target = os.path.join(bin_root, command_name)

if self == target:
    print >>sys.stderr, "Must be installed as a symlink!"
    sys.exit(1)

# Determine the fastest way to invoke the target. The actual invocation is
# deferred to after closing the file handle to avoid polluting their space.
with open(target, 'rb') as fh:
    header = fh.readline(1024)
    if header.startswith('#!') and 'python' and not 'python3' in header:
        # If it's targeted at this version of python, then run it locally to
        # avoid another startup overhead.
        runner = execfile
    else:
        # Otherwise just invoke it directly.
        runner = lambda cmdfile: os.execlp(cmdfile, *sys.argv)

runner(target)
