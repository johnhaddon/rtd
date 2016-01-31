# TaskSwitch

Switches between upstream tasks, so that only
one is chosen for execution.

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

## index 

 The index of the input task which is executed. A value
of 0 chooses the first input, 1 the second and so on. Values
larger than the number of available inputs wrap back around to
the beginning. 

