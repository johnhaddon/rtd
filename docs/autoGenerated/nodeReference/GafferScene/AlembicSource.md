# AlembicSource

Loads Alembic caches. Please note that Gaffer requires
a bounding box to be computable for every location in the
scene. Alembic files can store such bounding boxes, but
in practice they often don't. In this case Gaffer must perform
a full scene traversal to compute the appropriate bounding box.
It is recommended that if performance is a priority, bounding
boxes should be stored explicitly in the Alembic cache, or the
Cortex SceneCache (.scc) format should be used instead, since it
always stores accurate bounds.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs
an empty scene.

## fileName

 The path to the .abc file to load. Both
older HDF5 and newer Ogawa caches are supported.

## refreshCount

 Can be incremented to invalidate Gaffer's memory
cache and force a reload if the .abc file is
changed on disk.

