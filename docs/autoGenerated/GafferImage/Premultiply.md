# Premultiply

Multiplies selected channels by a specified alpha channel.

## user 

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish. 

## out 

 The output image generated by this node. 

## enabled 

 Turns the node on and off. 

## in 

 The input image 

## channels 

 The subset of channels to operate on. 

## alphaChannel 

 The channel to use as the alpha channel.
The selected channel does not have to be 'A', but whichever
channel is chosen will act as the alpha for the sake of this
node.
This channel will never be multiplied by itself - it will
remain the same as the input. 
