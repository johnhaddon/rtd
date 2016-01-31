# CoordinateSystem

Produces scenes containing a coordinate system. Coordinate systems
have two main uses :

- To visualise the transform at a particular location. In this
  respect they're similar to locators or nulls in other packages.
- To define a named coordinate system to be used in shaders at
  render time. This is useful for defining projections or procedural
  solid textures. The full path to the location of the coordinate
  system should be used to refer to it within shaders.

