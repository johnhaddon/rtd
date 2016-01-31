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

## in 

 The scene to be written. 

## fileName 

 The name of the file to be written. Note that unlike
image sequences, many scene formats write animation into
a single file, so using # characters to specify a frame
number is generally not necessary. 

## out 

 A direct pass-through of the input scene. 

