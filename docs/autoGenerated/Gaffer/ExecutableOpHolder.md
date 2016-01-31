# ExecutableOpHolder

Hosts Cortex Ops, allowing them to take perform
tasks in graphs executed by Gaffer's dispatchers.
graph. This is most appropriate for hosting Ops
which generate files on disk - for Ops which output
objects directly, an OpHolder is a more appropriate
host.

