import os
import zipfile as zipfile
import prod_logging as logging

log = logging.getLogger("rich")

def pack(project_path, ignored, exclude, output):
    # Zip the project
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(project_path):
            #Exclude ignored directories
            for ignored_dir in ignored:
                if os.path.isfile(os.path.join(root, ignored_dir)):
                    continue
                if ignored_dir in dirs:
                    dirs.remove(ignored_dir)

            #Exclude ignored files
            for ignored_file in ignored:
                if ignored_file in files:
                    if not os.path.isfile(os.path.join(root, ignored_file)):
                        continue
                    files.remove(ignored_file)

            for file in files:
                if file in exclude:
                    continue

                # Exclude package
                if file == output:
                    log.warning(f"Excluding [bold red blink]{file}[/]", extra={"markup": True})
                    continue
                
                # Write with relative path
                zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_path))