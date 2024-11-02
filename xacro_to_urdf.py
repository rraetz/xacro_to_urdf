import os
from os.path import join
import xacrodoc as xd
import argparse

parser = argparse.ArgumentParser(description='Convert xacro files to urdf files')
parser.add_argument('--package_dir', type=str, help='Directory of the package containing the xacro file')
parser.add_argument('--xacro_file', type=str, help='Relative path to the xacro file')
parser.add_argument('--urdf_file', type=str, help='Path to the output urdf file')
args = parser.parse_args()

package_name = os.path.basename(args.package_dir)
package_dir_parent = os.path.dirname(args.package_dir)

print(f'Package name: {package_name}')
print(f'Package directory: {args.package_dir}')
print(f'Xacro file: {args.xacro_file}')
print('Converting xacro to urdf')

xd.packages.look_in([package_dir_parent, args.package_dir])
doc = xd.XacroDoc.from_package_file(package_name, args.xacro_file)
doc.to_urdf_file(args.output_file)

print(f'Output file saved to {args.urdf_file}')

