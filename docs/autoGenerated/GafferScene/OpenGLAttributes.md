# OpenGLAttributes

Applies attributes to modify the appearance of objects in
the viewport and in renders done by the OpenGLRender node.

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

## filter 

 The filter used to control which parts of the scene are
processed. A Filter node should be connected here. 

## attributes 

 The attributes to be applied - arbitrary numbers of user defined
attributes may be added as children of this plug via the user
interface, or using the CompoundDataPlug API via python. 

## global 

 Causes the attributes to be applied to the scene globals
instead of the individual locations defined by the filter. 

