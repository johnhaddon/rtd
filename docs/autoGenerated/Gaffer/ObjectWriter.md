# ObjectWriter

Saves objects to disk using the writers provided by
the Cortex project.

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

 The object to be written to disk. 

## fileName 

 The name of the file to write. 

## parameters 

 Additional parameters specific to the format of the
file being written. These are created automatically
based on the extension when the fileName is specified. 

