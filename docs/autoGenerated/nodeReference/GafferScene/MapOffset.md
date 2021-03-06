# MapOffset

Adds an offset to object texture coordinates. Provides a convenient way of looking at specific texture UDIMs.

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

## offset

 An offset added to the texture coordinates. Note that moving the texture coordinates in the positive direction will move the texture in the negative direction.

## udim

 A specific UDIM to offset the texture coordinates to. The UDIM is converted to an offset which is added to the offset above.

## sName

 The name of the primitive variable holding the s coordinate.

## tName

 The name of the primitive variable holding the t coordinate.

