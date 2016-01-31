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

