# Animation

Generates keyframed animation to be applied to plugs
on other nodes.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## curves

 Stores animation curves. Rather than access
these directly, prefer to use the Animation::acquire()
method.

