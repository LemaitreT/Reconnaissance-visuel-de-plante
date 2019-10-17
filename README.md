# Data format
Each image consists in a JPEG file and is associated with an XML file containing the following metadata:
- MediaId: identifier of the image
- ObservationId: identifier of the observation, each observation consists of one or more images of a observed plant specimen
- ClassId: identifier of the class (ground-truth); taxonomical number used by Tela Botanica
- Species: the species names (containing 3 parts: the Genus name, the Species name, the author(s) who discovered or revised the name of the species)
- Genus: the name of the Genus, one level above the Species in the taxonomical hierarchy used by Tela Botanica
- Family: the name of the Family, two levels above the Species in the taxonomical hierarchy used by Tela Botanica
- View Content: part of the plant represented in the picture (Branch, Entire, Flower, Fruit, Leaf, LeafScan or Stem)
- Date: (if available) the date when the plant was observed,
- Vote: the (round up) average of the user ratings on image quality
- Locality: (if available) locality name, most of the time a town
- Latitude & Longitude: (if available) the GPS coordinates of the observation in the EXIF metadata, or, if no GPS information were found in the EXIF, the GPS coordinates of the locality where the plant was observed (only for the towns of metropolitan France)
- Author: name of the author of the picture

And if the image was included in previous plant task:
- Year: ImageCLEF2011, ImageCLEF2012, ImageCLEF2013, PlantCLEF2014 when the image was integrated in the benchmark
- IndividualPlantId2013: the plant observation ID used last year during the ImageCLEF2013 plant task,
- ImageID2013: the image id.jpg used in 2013.