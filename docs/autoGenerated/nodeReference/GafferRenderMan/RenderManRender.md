# RenderManRender

Performs offline batch rendering using a
RenderMan renderer. This is done in two
phases - first a RIB file is generated and
then the renderer is invoked to render it in
a separate process. Note though that the RIB
file is lightweight, and contains a single
procedural which will invoke Gaffer to generate
the scene on demand at runtime. The RIB therefore
requires very little disk space.

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

## dispatcher.batchSize

 Maximum number of frames to batch together when dispatching tasks.

## dispatcher.immediate

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

 When in "Render" mode, a RIB file is generated
and then renderered by running the renderer on
it. In "Generate RIB only" mode, only the RIB
is generated, and a subsequent node could be used
to post-process or launch the render in another
way - a SystemCommand node may be useful for this.

## ribFileName

 The name of the RIB file to be generated.

## command

 The system command used to invoke the renderer - this
can be edited to add any custom flags that are necessary,
or to use a different renderer. The rib filename is
automatically appended to the command before it is invoked.

