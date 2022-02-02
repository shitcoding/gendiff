"""Read data from specific source."""

import pathlib


def read_file(file_path):
    """Reads data from target file.
    Returns data and file_type (file extension).
    """
    path = pathlib.Path(file_path)
    with path.open("r") as f:
        data = f.read()
    file_type = path.suffix.lower()
    return data, file_type
