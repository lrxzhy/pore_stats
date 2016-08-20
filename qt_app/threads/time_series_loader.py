import PyQt4.QtCore as QtCore
import sys
sys.path.append('/home/preston/Desktop/Science/Research/pore_stats/qt_app/')
sys.path.append('/home/preston/Desktop/Science/Research/pore_stats/')
import time_series as ts
import resistive_pulse as rp
import rp_file
import math

class TimeSeriesLoader(QtCore.QThread):
    loaders = 0
    def __init__(self, time_series):
        super(TimeSeriesLoader, self).__init__()
        self._max_pts_returned = time_series._max_pts_returned
        self._decimation_factor = time_series._decimation_factor
        self._decimation_tiers = time_series._decimation_tiers

        if time_series._full_data != None:
            self._full_data = time_series._full_data
        else:
            self._full_data = None

        if time_series._file_path:
            self._file_path = time_series._file_path

        self.loaders+=1
        self._id = self.loaders


    def __del__(self):
        pass


    def run(self):
        """
        * Description:
        * Return:
        * Arguments:
            -
        """

        if self._full_data == None:
            self._full_data = rp_file.get_data(self._file_path)
            self.emit(QtCore.SIGNAL('add_tier(PyQt_PyObject, int)'), self._full_data, 0)

        for i in xrange(self._decimation_tiers-1, 0, -1):
            current_decimation_factor = self._decimation_factor**i
            decimated_data = ts.decimate_data(self._full_data, current_decimation_factor)
            self.emit(QtCore.SIGNAL('add_tier(PyQt_PyObject, int)'), decimated_data, i)

        return