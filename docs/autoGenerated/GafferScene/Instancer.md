# Instancer

Instances an input scene onto the vertices of a target
object, making one copy per vertex. Note that in Gaffer,
the instances are not limited to being a single object,
and each instance need not be identical. Instances can
instead include entire hierarchies and can be varied
from point to point, and individual instances may be
modified downstream without affecting the others. Gaffer
ensure's that where instances happen to be identical,
they share memory, and performs automatic instancing at
the object level when exporting to the renderer (this
occurs for all nodes, not just the Instancer).

Per-instance variation can be achieved using the
${instancer:id} variable in the upstream instance graph.
A common use case is to use this to randomise the index
on a SceneSwitch node, to choose randomly between several
instances, but it can be used to drive _any_ property of
the upstream graph.

