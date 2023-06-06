from datetime import time

from ..libs.android import R__drawable
from ..libs.android.widget import (
    TimePickerDialog,
    TimePickerDialog__OnTimeSetListener as OnTimeSetListener,
)
from .internal.pickers import PickerBase


class TimePickerListener(OnTimeSetListener):
    def __init__(self, impl):
        super().__init__()
        self.impl = impl

    def onTimeSet(self, view, hour, minute):
        self.impl.set_value(time(hour, minute))


class TimeInput(PickerBase):
    @classmethod
    def _get_icon(cls):
        return R__drawable.ic_menu_recent_history

    def create(self):
        super().create()

        # Dummy values used during initialization
        self.native.setText("00:00")
        self._min_time = None
        self._max_time = None

    def get_value(self):
        return time.fromisoformat(str(self.native.getText()))

    def set_value(self, value):
        self.native.setText(value.isoformat(timespec="minutes"))
        self._dialog.updateTime(value.hour, value.minute)
        self.interface.on_change(None)

    # Unlike DatePicker, TimePicker does not natively support min or max, so these
    # properties currently have no effect.
    def get_min_time(self):
        return self._min_time

    def set_min_time(self, value):
        self._min_time = value

    def get_max_time(self):
        return self._max_time

    def set_max_time(self, value):
        self._max_time = value

    def _create_dialog(self):
        return TimePickerDialog(
            self._native_activity,
            TimePickerListener(self),
            0,  # hour
            0,  # minute
            True,  # is24HourView
        )
