"""
    =======
    file.py
    =======

    This module provides the classes required to generate Django files ready to
    be stored in media directories.
"""

from django.core.files import File as DjangoFile
from .base import BasePlot, SVGZPlotMixin, PNGPlotMixin


class FileMixin:
    """
    This mixin provides the ``BasePlot`` class with the capability of
    generating a in memory file to be passed to an Image field.
    """
    file_class = DjangoFile
    filename = ""

    def get_filename(self):
        """
        Override this method to dinamically change the name of the file object
        created by the ``get_file()`` method.
        """
        name = self.filename
        ext = self.get_filetype()
        return f"{name}.{ext}"

    def get_file(self):
        """
        This method returns a Django file object ready to be assigned to an
        ImageField.
        """
        name = self.get_filename()
        file = self.file_class(self.get_image(), name)
        return file


class SVGZPlotToFile(SVGZPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a Django a ``File`` object storing an SVGZ
    plot.
    """
    pass


class PNGPlotToFile(PNGPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a Django a ``File`` object storing a PNG plot.
    """
    pass


SVGFilePlot = SVGZPlotToFile
PNGFilePlot = PNGPlotToFile
