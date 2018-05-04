from ij import IJ
from ij.plugin import Duplicator
from ij.plugin.filter import ParticleAnalyzer
from ij.measure import ResultsTable, Measurements
import glob, os

def imgFiltering(inputPath, outputPath):
	""" filter the image and save the result as a csv file
	"""
	# open the target image
	pollenImg = IJ.openImage(inputPath)
	
	# Create duplicator
	duplicator = Duplicator()
	
	# Duplicate the image with channel 1
	pollenImgCopy = duplicator.run(pollenImg, 1, 1, 1, 1, 1, 1);
	
	# set auto threshold
	# IJ.setAutoThreshold(pollenImgCopy, "Default dark");
	
	# set threshold
	IJ.setThreshold(pollenImgCopy, 17000, 65520)
	
	# Call the Thresholder to convert the image to a mask
	IJ.run(pollenImgCopy, "Convert to Mask", "")
	
	# create result table
	rt = ResultsTable()
	
	# create particle analyzer
	pAnalyzer = ParticleAnalyzer(ParticleAnalyzer.SHOW_NONE, Measurements.ALL_STATS, rt, 20.0, 1000.0, 0.5 ,1.0)
	
	# Analyze the particle
	pAnalyzer.analyze(pollenImgCopy)
	
	# Save results as csv
	rt.saveAs(outputPath)

def multipleImgFiltering(inputFolder, inputFileNames, outputFolder):
	""" filter multiple images
	"""
	for name in inputFileNames:
		inputFile = name + ".TIF"
		outputFile = name + ".csv"
		imgFiltering(inputFolder+inputFile,outputFolder+outputFile)

def searchFolder(folderPath, extentions):
	""" Search folder for input images with TIF extentions
		Returns the file names without extention
	"""
	files = []
	os.chdir(folderPath)
	for ext in extentions:
		for file in glob.glob("*."+ext):
			files.append(os.path.splitext(file)[0])
	return files

def main():
	print('started')
	
	inputFolder = "/home/takaos/private_git_repos/imagej-pollen/img/"
	outputFolder = "/home/takaos/private_git_repos/imagej-pollen/results/"
	inputFiles = searchFolder(inputFolder, ['TIF', 'tif'])
	
	multipleImgFiltering(inputFolder, inputFiles, outputFolder)
	
	print('done!')

main()
