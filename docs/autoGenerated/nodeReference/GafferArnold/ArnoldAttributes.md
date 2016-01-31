# ArnoldAttributes

Applies Arnold attributes to objects
in the scene.

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

## attributes

 The attributes to be applied - arbitrary numbers of user defined
attributes may be added as children of this plug via the user
interface, or using the CompoundDataPlug API via python.

## attributes.cameraVisibility

 Whether or not the object is visible to camera
rays. To hide an object completely, use the
visibility settings on the StandardAttributes
node instead.

## attributes.shadowVisibility

 Whether or not the object is visible to shadow
rays (whether or not it casts shadows).

## attributes.reflectedVisibility

 Whether or not the object is visible in
tight mirror reflections.

## attributes.refractedVisibility

 Whether or not the object is visible in
refractions.

## attributes.diffuseVisibility

 Whether or not the object is visible to diffuse
rays - whether it casts bounce light or not.

## attributes.glossyVisibility

 Whether or not the object is visible in
soft specular reflections.

## attributes.subdivIterations

 The maximum number of subdivision
steps to apply when rendering subdivision
surface. To set an exact number of
subdivisions, set the pixel error to
0 so that the maximum becomes the
controlling factor.

Use the MeshType node to ensure that a
mesh is treated as a subdivision surface
in the first place.

## attributes.subdivPixelError

 The maximum allowable deviation from the true
surface and the subdivided approximation. How
the error is measured is determined by the
metric below. Note also that the iterations
value above provides a hard limit on the maximum
number of subdivision steps, so if changing the
pixel error setting appears to have no effect,
you may need to raise the maximum.

## attributes.subdivAdaptiveMetric

 The metric used when performing adaptive
subdivision as specified by the pixel error.
The flatness metric ensures that the subdivided
surface doesn't deviate from the true surface
by more than the pixel error, and will tend to
increase detail in areas of high curvature. The
edge length metric ensures that the edge length
of a polygon is never longer than the pixel metric,
so will tend to subdivide evenly regardless of
curvature - this can be useful when applying a
displacement shader. The auto metric automatically
uses the flatness metric when no displacement
shader is applied, and the edge length metric when
a displacement shader is applied.

## global

 Causes the attributes to be applied to the scene globals
instead of the individual locations defined by the filter.

