### Importing useful packages
import cv2
import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt



### Convert an RGB numpy array to grayscale
def rgb2gray(rgb):

	## Separate relevant channels
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]

    ## Add channels with necessary weights
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    ## Return grayscale array
    return gray



### Creating mean intensity vs time plot
def intensity_vs_time(frame_directory, crop=[]):

	## Read frame paths
	fPaths = glob.glob(frame_directory + '*')

	## Display how many frames were discovered
	print('\nFound ' + str(len(fPaths)) + ' frames.')

	## Use to store intensities
	intensities = []

	## Use to store frames
	frames = []

	## Choose start and end frame
	sF = 0
	eF = 581

	## Iterate through the frame paths
	for i, fPath in enumerate(fPaths):

		# Make sure selected frame is between start and end frames
		if i >= sF and i <= eF:

			# Display progress
			if i%10 == 0:

				# Print statement
				print(str(100*i/len(fPaths))[:5] + '%')

			# Read the frame as PIL Image
			frame = Image.open(fPath)

			# Convert the frame to numpy array
			fArray = np.asarray(frame)

			# Check if it is a colour array
			if len(fArray.shape) == 3:

				# Convert it to grayscale
				fArray = rgb2gray(fArray)

			# If crop
			if len(crop) != 0:

				# Top left
				top_left = crop[0]

				# Bottom right
				bottom_right = crop[1]

				# Crop the array
				fArray = fArray[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

				# # Plot the frame
				# plt.imshow(fArray, cmap='gray')

				# # Show plot
				# plt.show()

			# Get the mean intensity of the array
			meanIntensity = np.mean(fArray)

			# Add the mean intensity to the list
			intensities.append(meanIntensity)

			# Add the frame to the list
			frames.append(i)

	## Convert intensities to numpy 1-D array
	intensities = np.asarray(intensities)

	## Get minima
	minIntensity = np.amin(intensities)

	## Get indices
	minIndices = np.where(intensities == minIntensity)

	## Print minima
	print('Minimum: ' + str(minIntensity)[:4] + ' at ' + str(minIndices))

	## Get maxima
	maxIntensity = np.amax(intensities)

	## Get indices
	maxIndices = np.where(intensities == maxIntensity)

	## Print maxima
	print('Maximum: ' + str(maxIntensity)[:4] + ' at ' + str(maxIndices))

	## Plot intensity vs frame
	plt.scatter(frames, intensities, s=1)

	## Plot min
	# plt.scatter(frames, intensities, s=1)

	## Show plot
	plt.show()