# SceneReader

Reads scenes in any of the formats supported by Cortex's SceneInterface.

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

 The name of the file to be loaded. The file can be
in any of the formats supported by Cortex's SceneInterfaces.

## refreshCount

 May be incremented to force a reload if the file has
changed on disk - otherwise old contents may still
be loaded via Gaffer's cache.

## tags

 Limits the parts of the scene loaded to only those
with a specific set of tags.

