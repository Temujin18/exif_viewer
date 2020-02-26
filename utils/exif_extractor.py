import os
import pyexiv2


def get_exif_exiv2(imagepath):
    """Generator for EXIF Tags of a given image using py3exiv2.
        Reference for installation: https://stackoverflow.com/questions/41075975/impossible-to-install-py3exiv2-with-pip"""
    _exif = {}
    try:
        metadata = pyexiv2.ImageMetadata(imagepath)
        metadata.read()
        for key,values in metadata.items():
            yield key,values.human_value
    except:
        pass