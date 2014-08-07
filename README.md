count-poly-overlap
==================

ArcGIS Python Toolbox used to count overlapping polygons within a layer.

This tool is a reponse to the rapidly dwindling number of available tools in the lower level licenses with each subsequent ESRI ArcGIS update.

This is not a complicated tool, it just combines a series of other tools in a workflow I use regularly. Given a polygon feature class or shapefile, the tool will perform a union. The resulting layer receives a new field [DissField] and each value is populated as a concatenation of the shape's area, centroid x-value and centroid y-value. These polygons are then dissolved based on [DissField] while summarizing the number of duplicate polygons. The sample below shows a resulting layer symbolized sequentially based on the count of duplicate dissolved polygons.

![screenshot](https://github.com/smoucka/smoucka.github.io/blob/master/sample_count-poly-overlap.png)

###Usage

Download zip or clone to local. Access through ArcCatalog or ArcMap. Tool takes two inputs, the polygon file to analyze (shapefile or feature class) and an output location. Brief testing showed tool works fine going back and forth between file formats.
