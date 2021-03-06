# Prune

A node for removing whole branches from the scene hierarchy.

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

 The branches to prune. The specified locations and all locations below them will be removed from the scene.

## adjustBounds

 Computes new tightened bounding boxes taking into account the removed locations. This can be an expensive operation - turn on with care.

