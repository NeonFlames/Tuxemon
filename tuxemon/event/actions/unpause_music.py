# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2014-2024 William Edwards <shadowapex@gmail.com>, Benjamin Bean <superman2k5@gmail.com>
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import final

from tuxemon.event.eventaction import EventAction

logger = logging.getLogger(__name__)


@final
@dataclass
class UnpauseMusicAction(EventAction):
    """
    Unpause the current (paused) music playback.

    Script usage:
        .. code-block::

            unpause_music

    """

    name = "unpause_music"

    def start(self) -> None:
        self.session.client.current_music.unpause()