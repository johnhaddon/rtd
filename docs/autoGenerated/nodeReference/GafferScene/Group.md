# Group

Groups together several input scenes under a new parent.
If the input scenes contain locations with identical names,
they are automatically renamed to make them unique in the
output scene.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The processed output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs the input scene unchanged.

## in

 The input scenes

## name

 The name of the group to be created. All the input
scenes will be parented under this group.

## transform

 The transform for the group itself. This will be
inherited by the objects parented under it.

