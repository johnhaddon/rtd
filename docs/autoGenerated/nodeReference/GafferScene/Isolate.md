# Isolate

Isolates objects by removing paths not matching a filter from the scene.

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

## from

 The ancestor to isolate the objects from. Only locations below
this will be removed.

## adjustBounds

 By default, the bounding boxes of ancestor locations are
automatically updated when children are removed. This can
be turned off if necessary to get improved performance - in
this case the bounding boxes will still wholly contain the
contents at each location, but may be bigger than necessary.

