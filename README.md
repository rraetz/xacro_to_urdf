# xacro_to_urdf
A small utility to compile a xacro file (e.g., from a ROS package) into a URDF. This is a wrapper around [xacrodoc](https://pypi.org/project/xacrodoc/). This utility does **NOT** require ROS to be installed.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
The script can be run with the following command:

```bash
python xacro_to_urdf.py --package_dir <package_dir> \
                        --xacro_file <xacro_file> \
                        --output_urdf_file <urdf_file> \
                        [--resolve_paths <true|false>] \
                        [--args '{"key1": "value1", "key2": "value2"}']
```

### Parameters
- `--package_dir` (str): Directory of the package containing the xacro file.
- `--xacro_file` (str): Relative path to the xacro file within the package directory.
- `--output_urdf_file` (str): Path to the output URDF file.
- `--resolve_paths` (bool, optional): Whether to replace `package://` paths with absolute paths. Defaults to `false`.
- `--args` (str, optional): Extra arguments for Xacro parsing in JSON format (e.g., `'{"key1": "value1", "key2": "value2"}'`).

### Example
```bash
python xacro_to_urdf.py --package_dir kortex_description  \
--xacro_file robots/gen3.xacro   \
--output_urdf_file  gen3.urdf  \
--args '{"arm": "gen3", "dof": "7", "gripper": "robotiq_2f_85", "vision": "true", "sim": "false", "prefix": ""}'
```

## Features
1. **Automatic `package.xml` creation**: If a `package.xml` file is missing in the package directory, the script generates a minimal one based on the package directory name.
2. **Xacro processing**: The script uses the `xacrodoc` library to convert the xacro file into a URDF.
3. **Flexible path handling**: Replace `package://` paths with absolute paths if required.
4. **Customizable Xacro arguments**: Pass additional parameters for Xacro file parsing using the `--args` option.

## Requirements
- The dependencies listed in `requirements.txt`

## Notes
- Ensure the `xacro_file` path is **relative** to the `package_dir`.
- If `package.xml` is missing, it will be auto-generated with minimal content:

  ```xml
  <package>
    <name>{package_name}</name>
  </package>
  ```