import arcpy, os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "count-poly-overlap"
        self.alias = "count-poly-overlap"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "count-poly-overlap"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
		
        p0 = arcpy.Parameter(
			displayName="Input Layer",
			name="InLyr",
			datatype="GPFeatureLayer",
			parameterType="Required",
			direction="Input")
        p1 = arcpy.Parameter(
			displayName="Output Location",
			name="OutLoc",
			datatype="DEWorkspace",
			parameterType="Required",
			direction="Input")
		
        return [p0, p1]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

    def execute(self, parameters, messages):
		"""The source code of the tool."""
		inlyr = parameters[0].valueAsText
		outloc = parameters[1].valueAsText
		base, fc = os.path.split(inlyr)
		# Remove '.shp' extension if input is shapefile
		fname = fc.split('.')[0]
		
		unionlyr = outloc + '/' + fname + '_Union'
		disslyr = outloc + '/' + fname + '_Diss'
		
		# If output location is not a geodatabase, append '.shp' file extension
		if len(os.path.basename(outloc).split('.')) == 1:
			unionlyr = unionlyr + '.shp'
			disslyr = disslyr + '.shp'
		
		arcpy.Union_analysis(inlyr, unionlyr)
		arcpy.AddField_management(unionlyr, 'DissField', 'TEXT', 100)
		arcpy.CalculateField_management(unionlyr, 'DissField', 'str(!SHAPE_Area!)+str(!SHAPE.CENTROID.X!)+str(!SHAPE.CENTROID.Y!)', 'PYTHON_9.3')
		arcpy.Dissolve_management(unionlyr, disslyr, 'DissField', [['DissField', 'COUNT']])
		return