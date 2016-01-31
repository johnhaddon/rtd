# SystemCommand

Runs system commands via a shell.

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

## command 

 The command to be run. This may reference values
from substitutions with '{substitutionName}' syntax. 

## substitutions 

 An arbitrary set of name/value pairs which can be
referenced in command with '{substitutionsName}' syntax. 

## environmentVariables 

 An arbitrary set of name/value pairs which will be set as
environment variables when running the command. 

