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


def read_video(name: str, path: str) -> bytes:
    r"""Reads the video file and returns a binary object.

    This function reads the video file with name `name` at path `path` as a
    binary object and returns it.

    Parameters
    ----------
    name : str
        A string that specifies the file name.
    path : str
        A string that represents the path to the object.

    Returns
    -------
    video_file : bytes
        THe binary representation of the video file.

    Raises
    ------
    FileNotFoundError
        When file path doesn't exist.

    Examples
    --------
    Pass a file name and a path to the object.

    >>> print(read_video("a.txt", "/").decode())
    Hello world
    """
    file_name = path + name
    try:
        with open(file_name, "rb+") as file_reader:
            video_file = file_reader.read()
            return video_file
    except Exception as e:
        lg.error(str(e))
