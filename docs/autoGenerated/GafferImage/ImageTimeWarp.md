# ImageTimeWarp

Changes the time at which upstream nodes are evaluated using
the following formula :

`upstreamFrame = frame * speed + offset`

Note that this node does not perform frame blending of any sort -
it is the responsibility of nodes upstream to do this.

