# MeshType

Changes between polygon and subdivision representations
for mesh objects, and optionally recalculates vertex
normals for polygon meshes.

Note that currently the Gaffer viewport does not display
subdivision meshes with smoothing, so the results of using
this node will not be seen until a render is performed.

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

## meshType

 The interpolation type to apply to the mesh.

## calculatePolygonNormals

 Causes new vertex normals to be calculated for
polygon meshes. Has no effect for subdivision
surfaces, since those are naturally smooth and do
not require surface normals. Vertex normals are
represented as primitive variables named "N".

## overwriteExistingNormals

 By default, vertex normals will only be calculated for
polygon meshes which don't already have them. Turning
this on will force new normals to be calculated even for
meshes which had them already.

