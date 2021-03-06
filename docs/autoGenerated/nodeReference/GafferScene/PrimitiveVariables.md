# PrimitiveVariables

Adds arbitrary primitive variables to objects. Currently only primitive variables with constant interpolation
are supported - see the OSLObject node for a means of creating variables with vertex interpolation.

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

## primitiveVariables

 The primitive variables to be applied - arbitrary numbers of user defined primitive variables may be added
as children of this plug via the user interface, or using the CompoundDataPlug API via
python.

