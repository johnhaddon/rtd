# PointConstraint

Translates objects so that they are constrained to
the world space position of the target. Leaves the
scale and orientation of the object untouched.

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

## offset

 A world space translation offset applied on top
of the target position.

## xEnabled

 Enables the constraint in the world space x axis.

## yEnabled

 Enables the constraint in the world space y axis.

## zEnabled

 Enables the constraint in the world space z axis.

