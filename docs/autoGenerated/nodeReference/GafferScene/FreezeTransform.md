# FreezeTransform

Resets the transforms at the specified scene locations,
baking the old transforms into the vertices of any child objects
so that they remain the same in world space. Essentially this
turns transforms in the hierarchy into rigid deformations of
the objects.

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

