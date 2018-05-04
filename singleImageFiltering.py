from ij import IJ
from ij.plugin import Duplicator
from ij.plugin.filter import ParticleAnalyzer
from ij.measure import ResultsTable, Measurements

print('started')

# open the target image
pollenImg = IJ.openImage("/home/takaos/private_git_repos/imagej-pollen/pollenImg/SU17_070907_188.TIF")

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

#IJ.run("Analyze Particles...", "size=20-Infinity circularity=0.50-1.00 show=Overlay display clear");
#saveAs("Results", "/home/takaos/Desktop/pollen/pollen070519_002.csv");

# create result table
rt = ResultsTable()

# create particle analyzer
pAnalyzer = ParticleAnalyzer(ParticleAnalyzer.SHOW_NONE, Measurements.ALL_STATS, rt, 20.0, 1000.0, 0.5 ,1.0)
pAnalyzer.analyze(pollenImgCopy)

rt.saveAs("/home/takaos/private_git_repos/imagej-pollen/results/SU17_070907_188.csv")

print('done!')

#outputImg = pAnalyzer.getOutputImage();
#outputImg.show()

# Show duplicated image
#pollenImgCopy.show()

