import sys

if sys.version_info < (3, 7):
    from ._cumulative import Cumulative
    from ._error_x import ErrorX
    from ._error_y import ErrorY
    from ._hoverlabel import Hoverlabel
    from ._marker import Marker
    from ._selected import Selected
    from ._stream import Stream
    from ._unselected import Unselected
    from ._xbins import XBins
    from ._ybins import YBins
    from . import hoverlabel
    from . import marker
    from . import selected
    from . import unselected
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".hoverlabel", ".marker", ".selected", ".unselected"],
        [
            "._cumulative.Cumulative",
            "._error_x.ErrorX",
            "._error_y.ErrorY",
            "._hoverlabel.Hoverlabel",
            "._marker.Marker",
            "._selected.Selected",
            "._stream.Stream",
            "._unselected.Unselected",
            "._xbins.XBins",
            "._ybins.YBins",
        ],
    )
