#A blender script to export the position of each vertex in a mesh to a text file, over a series of frames (one file per frame)

import bpy
import os

# Set the range of frames to export based on currently active timeline
startFrame = bpy.context.scene.frame_start
endFrame = bpy.context.scene.frame_end

# Set the output directory
outputDir = 'C:/Users/pfalk/Desktop/stls/'

# Set the object to export
obj = bpy.context.active_object

depsgraph = bpy.context.evaluated_depsgraph_get()

# Loop through the frames and for each frame, write stl 
for frame in range(startFrame, endFrame + 1):
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()  # Update the view layer after setting the frame

    # Apply all modifiers to the mesh
    mesh = obj.to_mesh(depsgraph=depsgraph)

    # Export the mesh as an STL file
    filepath = outputDir + obj.name + str(frame) + '.stl'
    bpy.ops.export_mesh.stl(filepath=filepath, use_selection=True)

# Reset the frame to the start
bpy.context.scene.frame_set(startFrame)
