# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2014-2023 William Edwards <shadowapex@gmail.com>, Benjamin Bean <superman2k5@gmail.com>
from __future__ import annotations

from tuxemon.event import MapCondition, collide, get_npc
from tuxemon.event.eventcondition import EventCondition
from tuxemon.session import Session


class CharAtCondition(EventCondition):
    """
    Check to see if the character is at the condition position on the map.

    Script usage:
        .. code-block::

            is char_at [character]

    Script parameters:
        character: Either "player" or character slug name (e.g. "npc_maple").

    """

    name = "char_at"

    def test(self, session: Session, condition: MapCondition) -> bool:
        character = get_npc(session, condition.parameters[0])
        if not character:
            return False
        return collide(condition, character.tile_pos)
