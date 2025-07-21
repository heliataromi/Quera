import os
 
def explore(extension: str, directory_path: str) -> dict[str, int]:
    result = dict()
    extension = extension.lower()
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file = file.lower()
            if file.endswith(f".{extension}"):
                result[root] = result.get(root, 0) + 1
    
    return result
