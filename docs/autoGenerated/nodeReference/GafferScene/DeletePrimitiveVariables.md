# DeletePrimitiveVariables

Deletes primitive variables from objects. The primitive
variables to be deleted are chosen based on name.

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

## names

 The names of the primitive variables to be deleted.
Names should be specified by spaces, and Gaffer's
standard wildcard characters may be used.

## invertNames

 When on, the primitive variables matched by names
are kept, and the non-matching primitive variables
are deleted.

