import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.core.management.utils import get_random_secret_key


def get_logger():
    r"""Return a logger.

    Configure logger lg with config for appLogger from config.json["logging"],
    and return it.
    Might need to configure the log path manually.

    Returns
    -------
    lg
        Logger object.

    Examples
    --------
    Get the logging object and use it to log

    >>> lg = get_logger()
    >>> lg.debug("Form is valid")
    appLogger - 2020-11-05 23:52:35,166-2984-DEBUG-Form is valid
    """
    # Configure logger lg with config for appLogger from config.json["logging"]
    CONFIG_DIR = Path(__file__).resolve().parent.parent.parent.parent
    with open(CONFIG_DIR / "config.json", "r") as f:
        config = jload(f)
        logging.config.dictConfig(config["logging"])
    lg = logging.getLogger("appLogger")
    # lg.debug("This is a debug message")
    return lg


def generate_secret_key(env_file_name):
    r"""Generates a secret key and stores inside a `.env` file

    Generates a secret key for Django's `settings.py`. Stores it in a `.env`
    file with filename `env_file_name`.
    This can later be retrieved and set as an environment variable.

    Parameters
    ----------
    env_file_name : string
        Name of the `.env` file

    Returns
    -------
    None

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] Distributing Django projects with unique SECRET_KEYs
    https://stackoverflow.com/a/49362490

    Examples
    --------
    in the `setting.py` file of a django project, write the following lines of
    code. This will generate and set a DJANGO_SECRET_KEY as an environment
    variable.

    import dotenv
    from [project-folder-name] import utils
    ...
    try:
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    except KeyError:
        path_env = os.path.join(BASE_DIR, '.env')
        utils.generate_secret_key(path_env)
        dotenv.read_dotenv(path_env)
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    """
    with open(env_file_name, "a+") as f:
        generated_key = get_random_secret_key()
        f.write(f"DJANGO_SECRET_KEY = {generated_key}\n")
