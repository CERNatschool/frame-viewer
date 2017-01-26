#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 frame-viewer.py

 See the README.md file and the GitHub wiki for more information.

 http://www.researchinschools.org/CERN

"""

#...for the Operating System stuff.
import os

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for file listing.
import glob

#...for making an image of the frame.
from visualisation import make_frame_image

if __name__ == "__main__":

    print("*")
    print("*=================*")
    print("* frame-viewer.py *")
    print("*=================*")
    print("*")

    # Parse the command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("inputDirectory",  help="Path to the input directory.")
    parser.add_argument("outputPath",      help="Path to the output folder.")
    parser.add_argument("--num-frames",    help="The number of frames to look at.",  default=-1, type=int)
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The output path.
    output_path = args.outputPath
    #
    # Check if the output directory exists. If it doesn't, raise an error.
    if not os.path.isdir(output_path):
        raise IOError("* ERROR: '%s' output directory does not exist!" % (output_path))

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    ## Log file path.
    log_file_path = os.path.join(output_path, 'log_frame-viewer.log')

    # Configure the logging.
    lg.basicConfig(filename=log_file_path, filemode='w', level=level)

    ## The path to the input file.
    input_path = args.inputDirectory
    #
    if not os.path.isdir(input_path):
        raise IOError("* ERROR: Unable to find input directory at '%s'." % (input_path))

    # The number of frames to look at.
    n_frames_to_process = args.num_frames

    lg.info(" *=================*")
    lg.info(" * frame-viewer.py *")
    lg.info(" *=================*")
    lg.info(" *")
    lg.info(" * Input path      : %s" % (input_path))
    lg.info(" * Output path     : %s" % (output_path))
    lg.info(" *")
    if n_frames_to_process > 0:
        lg.info(" * Number of frames to view: %d" % (n_frames_to_process))
    else:
        lg.info(" * Looking at all frames.")
    lg.info(" *")

    ## The list of frame filenames.
    frame_file_list = sorted(glob.glob(os.path.join(input_path, "*.txt")))

    lg.info(" * Frame files found:")
    # Loop over the files in the input data directory
    for i, filename in enumerate(frame_file_list):
        lg.info(" *--> File % 3d: '%s'" % (i, filename))

        if i + 1 > n_frames_to_process and n_frames_to_process > 0: break

        # Open the file containing the data

        ## The base name of the frame.
        base_name = os.path.basename(filename)[:-4]

        print("* Processing frame '%s'..." % (filename))

        ## A dictionary for the pixels {X:Pixel}.
        pixels = {}

        with open(filename, 'r') as df:
            data = df.read()

            # Loop over the rows of data read out from the data file.
            for data_row in data.splitlines():

                # Separate the x, y, and C values.
                pixel_data = data_row.split('\t')

                # Extract the x, y, and C values, converting them to integers.

                ## The pixel x position.
                x = int(pixel_data[0])

                ## The pixel y position.
                y = int(pixel_data[1])

                ## The pixel count value (i.e. the energy).
                C = int(pixel_data[2])

                ## A unique value for the pixel x, y position.
                X = (256 * y) + x

                # Assign a Pixel object to the dictionary, using X as the key.
                pixels[X] = C

            # Make an image of the frame.
            make_frame_image(base_name, pixels, output_path)

    lg.info(" *")

    print("*")
    print("* Complete! View the results using an image viewer, for example:")
    print("$ eog %s/ &" % (output_path))
    print("*")
