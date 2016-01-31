# Grade

Performs a simple per-channel colour grading operation
as follows :

A = multiply * (gain - lift) / (whitePoint - blackPoint)
B = offset + lift - A * blackPoint
result = pow( A * input + B, 1/gamma )

See the descriptions for individual plug for a slightly
more practical explanation of the formula.

