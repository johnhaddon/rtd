# RenderManAttributes

Applies RenderMan specific attributes to the scene.

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

 Whether or not objects are visible to the camera.
An object can be invisible to the camera but still
appear in reflections and shadows etc. To make an
object totally invisible, prefer the visibility
setting provided by the StandardAttributes node.

## attributes.cameraHitMode

 Specifies if shading is performed when the object
is hit by a camera ray, or if the primitive colour
is used as an approximation instead.

## attributes.transmissionVisibility

 Whether or not objects are visible to
transmission rays. Objects that are
visible to transmission rays will cast
shadows, and those that aren't won't.

## attributes.transmissionHitMode

 Specifies if shading is performed when the object
is hit by a tranmission ray, or if the primitive opacity
is used as an approximation instead.

## attributes.diffuseVisibility

 Whether or not objects are visible to
diffuse rays - typically this means whether
or not they cast occlusion and bounce light.

## attributes.diffuseHitMode

 Specifies if shading is performed when the object
is hit by a diffuse ray, or if the primitive colour
is used as an approximation instead.

## attributes.specularVisibility

 Whether or not objects are visible to
specular rays - typically this means whether
or not they are visible in reflections and
refractions.

## attributes.specularHitMode

 Specifies if shading is performed when the object
is hit by a specular ray, or if the primitive colour
is used as an approximation instead.

## attributes.photonVisibility

 Whether or not objects are visible to
photons.

## attributes.photonHitMode

 Specifies if shading is performed when the object
is hit by a photon, or if the primitive colour
is used as an approximation instead.

## attributes.shadingRate

 Specifies how finely objects are diced before they
are shaded. Smaller values give higher quality but
slower rendering.

## attributes.relativeShadingRate

 Specifies a multiplier on the shading rate. Note that
if shading rate is specified at multiple locations above
an object in the hierarchy, they are multiplied together
to arrive at the final shading rate.

## attributes.matte

 Matte objects don't appear in the render, but cut holes
in the alpha of all objects behind them.

## attributes.displacementBound

 Specifies the maximum amount the displacement shader will
displace by.

## attributes.maxDiffuseDepth

 The maximum depth for diffuse ray bounces.

## attributes.maxSpecularDepth

 The maximum depth for specular (reflection) ray bounces.

## attributes.traceDisplacements

 Whether or not displacements are taken into account
when raytracing. This can be fairly expensive.

## attributes.traceBias

 This bias value affects rays. It is an offset applied to the ray origin, moving it slightly away from the surface launch point in the ray direction. This offset can prevent blotchy artifacts resulting from the ray immediately finding an intersection with the surface it just left. Usually, 0.01 is the default scene value.

## global

 Causes the attributes to be applied to the scene globals
instead of the individual locations defined by the filter.

