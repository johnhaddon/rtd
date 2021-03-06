# MapProjection

Applies texture coordinates to meshes via a camera projection.
In Gaffer, texture coordinates (commonly referred to as UVs)
are represented as primitive variables named "s" and "t".

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

## camera

 The location of the camera to use for the projection.

## sName

 The name of the primitive variable to store the s
coordinate of the projected texture coordinates.
This may be changed in order to store multiple
sets of texture coordinates on a single mesh.

## tName

 The name of the primitive variable to store the t
coordinate of the projected texture coordinates.
This may be changed in order to store multiple
sets of texture coordinates on a single mesh.

