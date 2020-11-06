from django.core.exceptions import ValidationError
from django_apps.utils import get_logger
from upload_validator import FileTypeValidator

lg = get_logger()

FILE_SIZES = {
    "2.5MB": 2621440,
    "5MB": 5242880,
    "10MB": 10485760,
    "20MB": 20971520,
    "50MB": 52428800,
    "100MB": 104857600,
    "250MB": 214958080,
    "500MB": 429916160,
}


def check_validation_file_upload_size(file):
    lg.debug("Checking file size")
    lg.debug(str(FILE_SIZES["50MB"]))
    if file.size > FILE_SIZES["50MB"]:
        raise ValidationError(f"File should be less than {FILE_SIZES['50MB']}")


def check_validation_file_upload_type(file):
    lg.debug("Checking file type")
    lg.debug("Checking file extension")
    validator = FileTypeValidator(
        allowed_types=[
            "video/mp4",
        ],
        allowed_extensions=[
            ".mp4",
        ],
    )
    return validator(file)


def check_validation_file_upload(file):
    lg.debug("Checking file size, type, and extension")
    check_validation_file_upload_size(file)
    check_validation_file_upload_type(file)
