import bpy
import random

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Positions of the cubes
positions = [
    [4, 6, 3],
    [6, 6, 3],
    [3, 3, 3],
    [3, 2, 3],
    [7, 3, 3],
    [7, 2, 3],
    [4, 1, 3],
    [5, 1, 3],
    [6, 1, 3]
]

# Create cubes at the specified positions
cubes = []
for pos in positions:
    bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
    cube = bpy.context.active_object
    cubes.append(cube)

# Animate jittered rotation
for frame in range(101):
    bpy.context.scene.frame_set(frame)
    for cube in cubes:
        random_rotation = [random.uniform(0, 0.1), random.uniform(0, 0.1), random.uniform(0, 0.1)]
        cube.rotation_euler = [r + j for r, j in zip(cube.rotation_euler, random_rotation)]
        cube.keyframe_insert(data_path="rotation_euler", index=-1)

# Give each cube a random color
for cube in cubes:
    r = random.uniform(0.0, 1.0)
    g = random.uniform(0.0, 1.0)
    b = random.uniform(0.0, 1.0)
    mat = bpy.data.materials.new(name="Color")
    mat.diffuse_color = (r, g, b, 1)
    cube.data.materials.append(mat)
