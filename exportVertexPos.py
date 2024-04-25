#A blender script to export the position of each vertex in a mesh to a text file, over a series of frames (one file per frame)

import bpy
import os

# Set the range of frames to export based on currently active timeline
startFrame = bpy.context.scene.frame_start
endFrame = bpy.context.scene.frame_end

# Set the output directory
outputDir = 'C:/Users/pfalk/Desktop/VertexPos/'

# Set the object to export
obj = bpy.context.active_object

depsgraph = bpy.context.evaluated_depsgraph_get()

# Loop through the frames and for each frame, write xyz coordinates of each vertex to a text file
for frame in range(startFrame, endFrame + 1):
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()  # Update the view layer after setting the frame

    # Get a new mesh object with all modifiers applied
    mesh = obj.evaluated_get(depsgraph).to_mesh()

    with open(outputDir + obj.name + str(frame) + '.txt', 'w') as f:
        for vertex in mesh.vertices:  # Use the new mesh object
            # Transform the vertex coordinate from local space to world space
            world_co = obj.matrix_world @ vertex.co
            f.write(str(world_co.x) + ' ' + str(world_co.y) + ' ' + str(world_co.z) + '\n')

    # Clean up the new mesh object to save memory
    obj.evaluated_get(depsgraph).to_mesh_clear()

# Reset the frame to the start
bpy.context.scene.frame_set(startFrame)