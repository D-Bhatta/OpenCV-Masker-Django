from django.core.files.uploadedfile import TemporaryUploadedFile
from django_apps.utils import get_logger

lg = get_logger()


def store_file(name: str, path: str, file: TemporaryUploadedFile):
    r"""Stores the file sent in a request body.

    Stores the file sent in the request body with a particular name at a
    particular place, defined by the `name` and `path` paramteters.

    Parameters
    ----------
    name : str
        Name of the file.
    path : str
        Path of the storage location.
    file: FileType object
        A python wrapper around a file, sent in a request body.

    Returns
    -------
    None
        Writes the file to a location.

    Raises
    ------
    FileNotFoundError
        When file path doesn't exist.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> store_file("a.mp4", "", request.FILES['video'])
    """
    file_name = path + name
    try:
        with open(file_name, "wb+") as file_writer:
            for chunk in file.chunks():
                file_writer.write(chunk)
        lg.debug(f"Written file to {file_name}")
    except Exception as e:
        lg.error(str(e))
