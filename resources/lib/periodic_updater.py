import logging
import time

import xbmcaddon

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))


class PeriodicUpdater():
    """
    Periodically calls the given update_function.
    Simple implementation, not accurate at all!
    """

    def __init__(self, period, callback):
        self.period = period
        self._callback = callback
        self._last_update = time.time()
        self._running = False
        self.total_period = 0

    def tick(self):
        if not self._running:
            time.sleep(self.period)
            logger.debug("SAASBOPS is not running...")
            return
        now = time.time()
        # 三分钟内完成切换
        if now > self._last_update + self.period:
            if self.total_period > 180:
                self._running = False
            self._last_update = now
            self.total_period += self.period
            self._callback()

    def start(self):
        """(re)start periodic updates"""
        # Restart period when (re)starting
        self._last_update = time.time()
        self._running = True
        self.total_period = 0

    def stop(self):
        self._running = False
