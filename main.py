### Importing useful packages
import cv2
import numpy as np
from PIL import Image
import glob
import argparse



### Importing useful scripts
from utils import *



### Main functioning of code
def main(args):

	## Creating mean pixel intensity vs time plot
	if args.intensity:

		# Check if the input frames exist
		if len(glob.glob(args.fDir)) == 1:

			# Display that code is running
			print('\nCreating intensity vs time plot with source ' + args.fDir)

			# Run code to do intensity vs time
			intensity_vs_time(args.fDir, crop=[[769, 158], [1790, 977]])

		# If it does not exist
		else:

			# Display error message
			print('\nCould not find input directory ' + args.fDir)

	## End main
	return



### If main is called directly
if __name__ == '__main__':

	# Create argparse
	parser = argparse.ArgumentParser(description='Reading info for main.')

	# Arguments to create mean intensity graph
	parser.add_argument('--intensity', action='store_true', help='Flag to convert video to frames.')
	parser.add_argument('--fDir', action='store', type=str, default='input/example/', help='Source video.')
	# Example:
	# python main.py --intensity --fDir input/<input-frames>/

	# Parse arguments
	args = parser.parse_args()

	# Call main
	main(args)