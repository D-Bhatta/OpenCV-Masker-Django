import cv2
import numpy as np
from django_apps.settings import MEDIA_ROOT
from django_apps.utils import get_logger

lg = get_logger()


class Masker:
    r"""The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Parameters
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Methods
    ----------
    method_name(c='rgb')
        Description of public `method_name`.
    method_name(signature)
        Description of public `method_name`.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> from view_api.models import APIInfo
    >>> a1 = APIInfo(
    ...     name = "APOD",
    ...     description = "Astronomy Picture of the Day",
    ...     link = "https://api.nasa.gov/planetary/apod",
    ...     image = "img/1.jpg",
    ... )
    >>> a1.save()
    asyncio - 2020-10-18 05:53:05,483-5384-DEBUG-Using proactor: IocpProactor
    >>> a2 = APIInfo(
    ...     name = "EPIC",
    ...     description = "Latest Images from Earth Polychromatic Imaging Camera",
    ...     link = "https://api.nasa.gov/EPIC/api/natural",
    ...     image = "img/2.png",
    ... )
    >>> ...
    >>> a2.save()
    """

    def __init__(self, video_path=""):
        self.colors = {
            "BLUE": {
                "multiple": True,
                "num": 2,
                "ranges": [
                    (np.array([75, 125, 20]), np.array([95, 255, 255])),
                    (np.array([95, 125, 20]), np.array([130, 255, 255])),
                ],
            },
        }
        self.video_path = video_path
        self.output_path = MEDIA_ROOT + "output_video.mp4"
        self.input_colors = []
        self.masks = []
        self.hsv = np.ndarray(1)

    def apply_mask(self, video_path: str, colors: list):
        self.video_path = video_path
        for color in colors:
            try:
                self.colors[color]
            except KeyError:
                lg.error(
                    "Couldn't recognise color. Please try with a different color or check the color name entered."
                )
                raise ValueError("Unknown Color")
        self.input_colors = self.input_colors + colors
        return self.get_video()

    def get_video(self):
        self.gen_video()
        return self.output_path

    def get_colors(self):
        ranges = []
        for color_name in self.input_colors:
            color = self.colors[color_name]
            if color["multiple"]:
                for i in range(color["num"]):
                    ranges.append(color["ranges"][i])
            else:
                ranges.append(color["ranges"])

        return ranges

    def get_mask(self, color_range: tuple, hsv):
        upper, lower = color_range
        mask = cv2.inRange(hsv, lower, upper)  # pylint: disable=no-member
        return mask

    def get_masks(self, ranges: list, hsv):
        for color_range in ranges:
            mask = self.get_mask(color_range, hsv)
            self.masks.append(mask)
        return self.masks

    def add_masks(self, masks=None):
        if not masks:
            mask = self.masks[0]
            for i in range(1, len(self.masks)):
                mask = mask + self.masks[i]
            return mask
        else:
            mask = masks[0]
            for i in range(1, len(masks)):
                mask = mask + masks[i]
            return mask

    def and_masks(self):
        mask = self.masks[0]
        for i in range(1, len(self.masks)):
            mask = cv2.bitwise_and(
                mask, self.masks[i]
            )  # pylint: disable=no-member
        return mask

    def gen_mask(self, img):

        # Convert to hsv color range
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # pylint: disable=no-member

        # get the ranges for a color
        ranges = self.get_colors()

        # get the masks
        masks = self.get_masks(ranges, hsv)

        # Add all the masks
        mask = self.add_masks(masks)

        return mask

    def refine_mask(self, mask):

        mask = cv2.morphologyEx(
            mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1
        )  # pylint: disable=no-member
        mask = cv2.dilate(
            mask, np.ones((3, 3), np.uint8), iterations=1
        )  # pylint: disable=no-member

    def get_res(self, images: list):
        results = []
        for image in images:
            img1, img2, mask = image
            res = cv2.bitwise_and(
                img1, img2, mask=mask
            )  # pylint: disable=no-member
            results.append(res)
        return results

    def gen_video(self):
        pass
