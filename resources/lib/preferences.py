import logging
from typing import Any, Dict, Optional

import xbmcaddon

ADDON = xbmcaddon.Addon()
addon_id = ADDON.getAddonInfo('id')
logger = logging.getLogger(addon_id)


class Preferences():
    def __init__(self, load, save) -> None:
        self._storage = {}
        self._load = load
        self._save = save

        if self._load:
            self._storage = self._load()

    def reset(self, ) -> None:
        self._storage = {}

    def get(self, show: int) -> Optional[Dict]:
        # Strings to allow for storing as JSON (easier debugging than binary formats)
        show_str = str(show)

        if show_str not in self._storage.keys():
            return None
        try:
            info = self._storage[show_str]
            return info
        except KeyError:
            pass

    def set(self, show: int, info: Any) -> None:
        # Strings to allow for storing as JSON (easier debugging than binary formats)
        show_str = str(show)
        # episode_str = str(episode)
        
        # if show not in self._storage.keys():
        #     self._storage[show_str] = {}
        # if season not in self._storage[show_str].keys():
        #     self._storage[show_str][season_str] = {}
        self._storage[show_str] = info
        # self._storage[show_str][season_str][episode_str] = info
        if self._save:
            self._save(self._storage)
