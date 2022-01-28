# Prod

Prod is a tool that ignore some files in production but not in repositories.

## Installation
Using pip:
```bash
pip install prod
```

Using source code:
```bash
git clone https://github.com/amireshoon/prod.git && cd prod
pip install .
```

## Usage
To initilize Prod add a prod file to your root of your project. The prod file name should be `.prod` in the beta version, but custom name for prod file will be supported in first release.

### Syntax
Prod file syntax is very similar and simple as `.gitignore` file.
You can use `!` to exclude file or folder from removing in production.

### Building package
You can use
```bash
prod make .
```
or
```bash
prod make <project_path> -o <package_output_path>
```
