# Sphere

Produces scenes containing a sphere.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs
an empty scene.

## name

 The name of the object in the output scene.

## sets

 A list of sets to include the object in. The
names should be separated by spaces.

## transform

 The transform applied to the object.

## type

 The type of object to produce. May be a SpherePrimitive or a Mesh.

## radius

 Radius of the sphere.

## zMin

 Limits the extent of the sphere along the lower pole.
Valid values are in the range [-1,1] and should always
be less than zMax.

## zMax

 Limits the extent of the sphere along the upper pole.
Valid values are in the range [-1,1] and should always
be greater than zMin.

## thetaMax

 Limits the extent of the sphere around the pole axis.
Valid values are in the range [0,360].

## divisions

 Controls tesselation of the sphere when type is Mesh.

