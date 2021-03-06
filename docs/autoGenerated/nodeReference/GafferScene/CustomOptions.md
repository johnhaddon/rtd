# CustomOptions

Applies arbitrary user-defined options to the root of the scene. Note
that for most common cases the StandardOptions, OpenGLOptions, RenderManOptions,
and ArnoldOptions nodes should be used in preference - they provide predefined
sets of options with customised user interfaces. The CustomOptions node is of most use when
needing to set a custom option not supported by the specialised nodes.

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

