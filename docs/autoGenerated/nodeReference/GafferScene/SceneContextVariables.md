# SceneContextVariables

Adds variables which can be referenced by upstream expressions.

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

## variables

 The variables to be added - arbitrary numbers of variables
can be added here.

