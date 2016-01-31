# AlembicSource

Loads Alembic caches. Please note that Gaffer requires
a bounding box to be computable for every location in the
scene. Alembic files can store such bounding boxes, but
in practice they often don't. In this case Gaffer must perform
a full scene traversal to compute the appropriate bounding box.
It is recommended that if performance is a priority, bounding
boxes should be stored explicitly in the Alembic cache, or the
Cortex SceneCache (.scc) format should be used instead, since it
always stores accurate bounds.

