# ObjectReader

Loads objects from disk using the readers provided by
the Cortex project. In most cases it is preferable to
use a dedicated SceneReader or ImageReader instead of
this node.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## fileName

 The file to load.

## out

 The loaded object. Note that the ObjectToScene node may
be used to convert this for use with the GafferScene
module.

