import bpy
import math
import random
import string

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Parameters
num_cubes = 200
radius = 1.0
height = 0.1
turns = 3.0

# Create double helix
for i in range(num_cubes):
    angle = 2.0 * math.pi * i / num_cubes
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    z = (height * i / num_cubes) * turns

    bpy.ops.mesh.primitive_cube_add(size=0.05, location=(x, y, z))
    cube = bpy.context.active_object

    # Generate random name
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    random_number = random.randint(100, 999)
    cube.name = f"{random_name}:{random_number}"

# Print statistics
num_objects = len(bpy.data.objects)
num_vertices = sum(len(mesh.data.vertices) for mesh in bpy.data.meshes)
num_materials = len(bpy.data.materials)

print("Total number of objects:", num_objects)
print("Total number of vertices:", num_vertices)
print("Total number of materials:", num_materials)
