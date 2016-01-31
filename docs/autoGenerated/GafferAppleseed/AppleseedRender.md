# AppleseedRender

Performs offline batch rendering using the
appleseed renderer. This is done in two phases -
first the scene geometry is exported to mesh files and an appleseed project
is generated, and then appleseed is invoked to render it.

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

## in 

 The scene to be rendered. 

## out 

 A pass-through of the input scene. 

## mode 

 When in the standard "Render" mode, an appleseed project
is generated and then renderered in appleseed.
Alternatively, just the appleseed project can be generated
and then another method can be used to post-process
it or launch the render - a SystemCommand node may
be useful for this. 

## fileName 

 The name of the appleseed project file to be generated. 

## verbosity 

 Controls the verbosity of the appleseed renderer output. 

