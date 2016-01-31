# ImageWriter

Writes image files to disk using OpenImageIO. All file
types supported by OpenImageIO are supported by the
ImageWriter.

## user 

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish. 

## preTasks 

 Input connections to upstream nodes which must be
executed before this node. 

## postTasks 

 Input connections to nodes which must be
executed after this node, but which don't
need to be executed before downstream nodes. 

## task 

 Output connections to downstream nodes which must
not be executed until after this node. 

## dispatcher 

 Container for custom plugs which dispatchers use to
control their behaviour. 

## in 

 The image to be written to disk. 

## fileName 

 The name of the file to be written. File sequences with
arbitrary padding may be specified using the '#' character
as a placeholder for the frame numbers. 

## channels 

 The channels to be written to the file. 

## out 

 A pass-through of the input image. 

## openexr 

 Format options specific to OpenEXR files. 

## dpx 

 Format options specific to DPX files. 

## tiff 

 Format options specific to TIFF files. 

## field3d 

 Format options specific to Field3D files. 

## fits 

 Format options specific to FITS files. 

## iff 

 Format options specific to IFF files. 

## jpeg 

 Format options specific to Jpeg files. 

## jpeg2000 

 Format options specific to Jpeg2000 files. 

## png 

 Format options specific to PNG files. 

## rla 

 Format options specific to RLA files. 

## sgi 

 Format options specific to SGI files. 

## targa 

 Format options specific to Targa files. 

## webp 

 Format options specific to WebP files. 

