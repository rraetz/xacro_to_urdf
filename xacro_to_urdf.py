import os
from os.path import join
import xacrodoc as xd
import argparse
import json

# Argument parsing
parser = argparse.ArgumentParser(description='Convert xacro files to urdf files')
parser.add_argument('--package_dir', type=str, help='Directory of the package containing the xacro file')
parser.add_argument('--xacro_file', type=str, help='Relative path to the xacro file')
parser.add_argument('--output_urdf_file', type=str, help='Path to the output urdf file')
parser.add_argument('--resolve_paths', default=False, type=bool, help='Wheter the replace the packages:// paths with absolute paths')
parser.add_argument(
    '--args', 
    type=str,
    help="Extra arguments for Xacro parsing in JSON format (e.g., '{\"key1\": \"value1\", \"key2\": \"value2\"}')"
)
args = parser.parse_args()

# Parse the input dictionary
subargs = {}
if args.args:
    try:
        subargs = json.loads(args.args)
        if isinstance(subargs, dict):
            print("Parsed dictionary:")
            print(subargs)
        else:
            print("Error: The provided input is not a valid dictionary.")
    except json.JSONDecodeError as e:
        print(f"Error parsing dictionary: {e}")

# Get package infos
package_name = os.path.basename(args.package_dir)
package_dir_parent = os.path.dirname(args.package_dir)
print(f'Package name: {package_name}')
print(f'Package directory: {args.package_dir}')
print(f'Xacro file: {args.xacro_file}')

# Check for package.xml and create it if missing
package_xml_path = join(args.package_dir, 'package.xml')
if not os.path.exists(package_xml_path):
    print(f'No package.xml found in {args.package_dir}. Creating one.')
    package_xml_content = f"""<package>
  <name>{package_name}</name>
</package>
"""
    with open(package_xml_path, 'w') as package_xml_file:
        package_xml_file.write(package_xml_content)
    print(f'package.xml created at {package_xml_path}')
else:
    print(f'package.xml found at {package_xml_path}')
    
# Resolve Xacro file path
xacro_file_path = join(args.package_dir, args.xacro_file)
if not os.path.exists(xacro_file_path):
    raise FileNotFoundError(f"The xacro file does not exist: {xacro_file_path}")
print(f'Resolved xacro file path: {xacro_file_path}')

# Xacro processing
print('Converting xacro to urdf')
xd.packages.look_in([package_dir_parent, args.package_dir])
doc = xd.XacroDoc.from_file(xacro_file_path, subargs=subargs, resolve_packages=args.resolve_paths)
doc.to_urdf_file(args.output_urdf_file)

print(f'Output file saved to {args.output_urdf_file}')

