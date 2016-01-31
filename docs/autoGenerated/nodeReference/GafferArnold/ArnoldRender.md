# ArnoldRender

Performs offline batch rendering using the
Arnold renderer. This is done in two phases -
first a .ass file is generated and then Arnold
is invoked to render it. Note though that the .ass
file is lightweight, and contains little more than
a procedural which will use Gaffer to generate the
scene at render time.

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

 The scene to be rendered.

## out

 A pass-through of the input scene.

## mode

 When in the standard "Render" mode, an .ass
file is generated and then renderered in Arnold.
Alternatively, just the .ass file can be generated
and then another method can be used to post-process
it or launch the render - a SystemCommand node may
be useful for this. Finally, an expanded .ass file
may be generated - this will contain the entire
expanded scene rather than just a procedural, and can
be useful for debugging.

## fileName

 The name of the .ass file to be generated.

## verbosity

 Controls the verbosity of the Arnold renderer output.

