import json
with open('Sponza.gltf', 'r') as f:
    data = json.load(f)
    if 'extensionsUsed' in data and 'KHR_draco_mesh_compression' in data['extensionsUsed']:
        print("Model uses Draco compression")
    else:
        print("Model does NOT use Draco compression")
