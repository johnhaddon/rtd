# ObjectToScene

Converts objects to be used with the nodes in the
GafferScene module. Typically these objects would
come from a GafferCortex OpHolder node or ObjectReader
node.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs
an empty scene.

## name

 The name of the object in the output scene.

## sets

 A list of sets to include the object in. The
names should be separated by spaces.

## transform

 The transform applied to the object.

## object

 The object to be placed in the output scene.

