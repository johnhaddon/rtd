# DeleteGlobals

A node which removes named items from the globals.
To delete outputs or options specifically, prefer
the DeleteOutputs and DeleteOptions nodes respectively,
as they provide improved interfaces for their specific
tasks.

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

## names

 The names of globals to be removed. Names should be
separated by spaces and can use Gaffer's standard wildcards.

## invertNames

 When on, matching names are kept, and non-matching names are removed.

