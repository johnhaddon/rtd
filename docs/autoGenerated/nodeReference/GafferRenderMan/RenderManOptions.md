# RenderManOptions

Sets global scene options applicable to RenderMan
renderers. Use the StandardOptions node to set
global options applicable to all renderers.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The processed output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs the input scene unchanged.

## in

 The input scene

## options

 The options to be applied - arbitrary numbers of user defined options may be added
as children of this plug via the user interface, or using the CompoundDataPlug API via
python.

## options.pixelSamples

 The number of primary samples to divide each pixel into
in the X and Y directions. For example, 3x3 gives a total of
9 samples per pixel. This is the primary quality control for
geometric antialiasing and motion blur.

## options.hider

 The "Hidden" hider means the classic REYES algorithm
is used, and the "Raytrace" hider means a more modern
raytraced algorithm is used.

## options.hiderDepthFilter

 The filter used to compute a single depth
value per pixel from the depths in each
pixel sample.

## options.hiderJitter

 Whether or not each pixel sample is
jittered about the centre of its subpixel
position, or if they're aligned in a
regular grid. If in doubt, leave this on.

## options.hiderSampleMotion

 May be turned off to disable the sampling of
motion blur, but keep motion vectors available
for use in shaders. This is useful for
rendering a motion vector pass to allow
2D motion blur to be applied as a post process.
If you simply wish to turn off motion blur
entirely, then use the motion blur settings
in the StandardOptions node.

## options.hiderExtremeMotionDOF

 An alternative sampling algorithm which
is more expensive, but gives higher quality
results when objects are both moving quickly
and are out of focus.

## options.hiderProgressive

 Renders at progressively increasing levels
of quality, to give quick low quality feedback
at the start of an interactive render. Only
applies when the raytrace hider is used.

## options.statisticsLevel

 Determines the verbosity of statistics
output.

## options.statisticsFileName

 The name of a file where the statistics
will be written.

## options.statisticsProgress

 Turning this on causes a render progress
percentage to be printed out continuously
during rendering.

## options.shaderSearchPath

 The filesystem paths where shaders are
searched for. Paths should be separated
by ':'.

## options.textureSearchPath

 The filesystem paths where shaders are
located. Paths should be separated
by ':'.

## options.displaySearchPath

 The filesystem paths where display driver
plugins are located. These will be used when searching
for drivers specified using the Outputs
node. Paths should be separated by ':'.

## options.archiveSearchPath

 The filesystem paths where RIB archives
are located. These will be used when searching
for archives specified using the ExternalProcedural
node. Paths should be separated by ':'.

## options.proceduralSearchPath

 The filesystem paths where DSO procedurals
are located. These will be used when searching
for procedurals specified using the ExternalProcedural
node. Paths should be separated by ':'.

