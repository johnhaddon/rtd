# RenderManShader

Loads shaders for use in RenderMan renderers. Use the ShaderAssignment node to assign shaders to objects in the scene.

## user 

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish. 

## name 

 The name of the shader being represented. This should
be considered read-only. Use the Shader.loadShader()
method to load a shader. 

## type 

 The type of the shader being represented. This should
be considered read-only. Use the Shader.loadShader()
method to load a shader. 

## parameters 

 Where the parameters for the shader are represented. 

## enabled 

 Turns the node on and off. 

## __nodeName 

 None 

## __nodeColor 

 None 

## out 

 The output from the shader. 
