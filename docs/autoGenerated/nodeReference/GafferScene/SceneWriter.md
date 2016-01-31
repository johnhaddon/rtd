# SceneWriter

Writes scenes to disk. Supports all formats for which a
writeable Cortex SceneInterface exists.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## preTasks

 Input connections to upstream nodes which must be
executed before this node.

## postTasks

 Input connections to nodes which must be
executed after this node, but which don't
need to be executed before downstream nodes.

## task

 Output connections to downstream nodes which must
not be executed until after this node.

## dispatcher

 Container for custom plugs which dispatchers use to
control their behaviour.

### dispatcher.batchSize

 Maximum number of frames to batch together when dispatching tasks.

### dispatcher.immediate

 Causes this node to be executed immediately upon dispatch,
rather than have its execution be scheduled normally by
the dispatcher. For instance, when using the LocalDispatcher,
the node will be executed immediately in the dispatching process
and not in a background process as usual.

When a node is made immediate, all upstream nodes are automatically
considered to be immediate too, regardless of their settings.

## in

 The scene to be written.

## fileName

 The name of the file to be written. Note that unlike
image sequences, many scene formats write animation into
a single file, so using # characters to specify a frame
number is generally not necessary.

## out

 A direct pass-through of the input scene.
