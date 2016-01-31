# ArnoldOptions

Sets global scene options applicable to the Arnold
renderer. Use the StandardOptions node to set
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

### options.aaSamples

 Controls the number of rays per pixel
traced from the camera. The more samples,
the better the quality of antialiasing,
motion blur and depth of field. The actual
number of rays per pixel is the square of
the AA samples value - so a value of 3
means 9 rays are traced, 4 means 16 rays are
traced and so on.

### options.giDiffuseSamples

 Controls the number of rays traced when
computing indirect illumination ("bounce light").
The number of actual diffuse rays traced is the
square of this number.

### options.giGlossySamples

 Controls the number of rays traced when
computing glossy specular reflections.
The number of actual specular rays traced
is the square of this number.

### options.giRefractionSamples

 Controls the number of rays traced when
computing refractions. The number of actual
specular rays traced is the square of this number.

### options.giDiffuseDepth

 Controls the number of ray bounces when
computing indirect illumination ("bounce light").

### options.giGlossyDepth

 Controls the number of ray bounces when
computing glossy specular reflections.

### options.giReflectionDepth

 Controls the number of ray bounces when
computing reflections.

### options.giRefractionDepth

 Controls the number of ray bounces when
computing refractions.

### options.ignoreTextures

 Ignores all file textures, rendering as
if they were all white.

### options.ignoreShaders

 Ignores all shaders, rendering as a
simple facing ratio shader instead.

### options.ignoreAtmosphere

 Ignores all atmosphere shaders.

### options.ignoreLights

 Ignores all lights.

### options.ignoreShadows

 Skips all shadow calculations.

### options.ignoreSubdivision

 Treats all subdivision surfaces
as simple polygon meshes instead.

### options.ignoreDisplacement

 Ignores all displacement shaders.

### options.ignoreBump

 Ignores all bump mapping.

### options.ignoreMotionBlur

 Ignores motion blur. Note that the turn
off motion blur completely, it is more
efficient to use the motion blur controls
in the StandardOptions node.

### options.ignoreSSS

 Disables all subsurface scattering.

### options.textureSearchPath

 The locations used to search for texture
files.

### options.proceduralSearchPath

 The locations used to search for procedural
DSOs.

### options.shaderSearchPath

 The locations used to search for shader plugins.

### options.errorColorBadTexture

 The colour to display if an attempt is
made to use a bad or non-existent texture.

### options.errorColorBadMesh

 The colour to display if bad geometry
is encountered.

### options.errorColorBadPixel

 The colour to display for a pixel where
a NaN is encountered.

### options.errorColorBadShader

 The colour to display if a problem occurs
in a shader.

