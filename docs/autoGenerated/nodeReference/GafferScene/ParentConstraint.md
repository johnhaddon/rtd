# ParentConstraint

Constrains objects from one part of the scene hierarchy as if they were
children of another part of the hierarchy.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The processed output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs the input scene unchanged.

## in

 The input scene

## filter

 The filter used to control which parts of the scene are
processed. A Filter node should be connected here.

## target

 The scene location to which the objects are constrained.
The world space transform of this location forms the basis
of the constraint target, but is modified by the targetMode
and targetOffset values before the constraint is applied.

## targetMode

 The precise location of the target transform - this can be
derived from the origin or bounding box of the target location.

## targetOffset

 An offset applied to the target transform before the constraint
is applied. The offset is measured in the object space of the
target location.

## relativeTransform

 Transforms the constrained object relative to the target location.

