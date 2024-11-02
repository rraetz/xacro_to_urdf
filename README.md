# xacro_to_urdf
Small utility to compile a xacro file from a ROS package to a  urdf. This is a wrapper around [xacrodoc](https://pypi.org/project/xacrodoc/)

## Installation
1. Clone the repository
2. Run `pip install -r requirements.txt` in the root of the repository

## Usage
The script can be run with the following command:
```bash
python xacro_to_urdf.py --package_dir <package_dir> --xacro_file <xacro_file> --urdf_file <urdf_file>
```
The xacro_file path must be relative to the package_dir.