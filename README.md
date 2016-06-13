# The CERN@school Frame Viewer
Some simple Python code for displaying CERN@school Timepix frame data.

To run the example code from a CernVM, type the following commands
from the directory you cloned the repository into:

```bash
$ . setup.sh
$ mkdir ../tmp
$ python frame-viewer.py testdata/ ../tmp/
```

This should display each frame from the `testdata` folder in turn.
Close the frame and press any key to see the next frame.
