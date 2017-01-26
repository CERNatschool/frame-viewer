# The CERN@school Frame Viewer
This repository contains some simple Python code for visualising
CERN@school Timepix frame data using a GridPP CernVM
and the `matplotlib` software suite.


## Disclaimers
* _This code dates from 2016. While every attempt has been
made to ensure that it is usable, some work may be required to get it
running on your own particular system.
We recommend using a GridPP CernVM; please refer to
[this guide](http://doi.org/10.6084/m9.figshare.4552825.v1)
for further instructions.
Unfortunately CERN@school cannot guarantee further support for this code.
Please proceed at your own risk_.
* _This repository is now deprecated, and remains here for legacy purposes.
For future work regarding CERN@school, please refer to the
[Institute for Research in Schools](http://researchinschools.org) (IRIS)
[GitHub repository](https://github.com/InstituteForResearchInSchools).
Please also feel free to fork and modify this code as required for
your own research._


## Running the code
To run the example code from a CernVM, type the following commands
from the directory you cloned the repository into:

```bash
$ . setup.sh
$ mkdir ../tmp
$ python frame-viewer.py testdata/ ../tmp/
```

This should create an image for each frame in the `testdata` folder
in the output directory.

_Note: if you are not using a GridPP CernVM, the `setup.sh` script
will not work as you won't have access to the CERN@school CVMFS
repository and will have to source your own version of
`matplotlib` via e.g. the
[Anaconda Python distribution](http://anaconda.org)._


## Viewing the images
Any standard image viewer should be able to display the images
created by the Python script. On the GridPP CernVM, for example,
you can use the Eye of Gnome viewer:

```bash
$ sudo yum install eog
[... say 'yes' to everything and type your password when asked ...]
$ eog ../tmp &
```

You can then view each image by pressing the left or right arrow keys.


## The data
The data in the `testdata` folder is taken from the
[Crookes dataset](http://doi.org/10.6084/m9.figshare.734262.v1),
a sample set of measurements made at the Royal Institution of
Great Britain during the BIG SCIENCE event of 18th June 2013.


## Acknowledgements
CERN@school was supported by
the UK [Science and Technology Facilities Council](http://www.stfc.ac.uk) (STFC)
via grant numbers ST/J000256/1 and ST/N00101X/1,
as well as a Special Award from the Royal Commission for the Exhibition of 1851.
The CERN@school Collaboration would also like to acknowledge the support
provided by the [GridPP Collaboration](http://www.gridpp.ac.uk)
in terms of both computing resources and technical guidance from
collaboration members.


## Useful links
* [Setting up a GridPP CernVM](http://doi.org/10.6084/m9.figshare.4552825.v1);
* The [Crookes dataset on FigShare](http://doi.org/10.6084/m9.figshare.734262.v1);
* The [Institute for Research in Schools](http://researchinschools.org) (IRIS) homepage;
* The [IRIS CERN@school website](http://researchinschools.org/CERN);
* The [Official IRIS GitHub Organization](https://github.com/InstituteForResearchInSchools).
