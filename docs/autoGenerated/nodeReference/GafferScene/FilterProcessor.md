# FilterProcessor

The base type for all filters which operate using one or more input filters.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## enabled

 The on/off state of the filter. When it is off, the
filter does not match any locations.

## out

 The result of the filter. This should be connected into
the "filter" plug of a FilteredSceneProcessor.

## in

 The input filter

