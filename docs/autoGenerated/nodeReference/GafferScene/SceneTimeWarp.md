# SceneTimeWarp

Changes the time at which upstream nodes are evaluated using
the following formula :

`upstreamFrame = frame * speed + offset`

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

## speed

 Multiplies the current frame value.

## offset

 Adds to the current frame value (after multiplication with speed).

