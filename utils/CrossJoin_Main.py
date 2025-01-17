
"""
The Clear BSD License

Copyright (c) 2024 SouthAlbertaAI
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted (subject to the limitations in the disclaimer
below) provided that the following conditions are met:

     * Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

     * Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

     * Neither the name of the copyright holder nor the names of its
     contributors may be used to endorse or promote products derived from this
     software without specific prior written permission.

NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import discord
from discord.ext import tasks
from discord.ext import commands
import structlog as sl


# Discord bot itself
class CrossJoin(discord.ext.commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = sl.get_logger()
        self.channel_main = None
        self.alert_mode = False

    async def setup_hook(self) -> None:
        self.scheduled_capacity_check.start()

    async def setup_alert_mode(self) -> None:
        self.alert_mode_on.start()

    async def on_ready(self):
        await self.tree.sync()
        self.logger.info(f"Logged On As {self.user} with ID {self.user.id}")
        self.logger.info("------------------------------------------------------")

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            return

    # These are skeletons until they can be refactored for the new command system
    @tasks.loop(hours=2)
    async def scheduled_capacity_check(self):
        self.logger.info("Skeleton For Now")
        # if self.channel_main is not None:
        #     sender = self.get_channel(self.channel_main)
        #     Output = Support.HotInfer("check-safe", self)
        #     Output.description += "\nNotice: This Is A Scheduled Run"
        #     # Check to see if alert mode should be triggered
        #     if "Alert Mode Triggered: True" in Output.description:
        #         self.alert_mode = True
        #     await sender.send(embed=Output)

    # These are skeletons until they can be refactored for the new command system
    @tasks.loop(minutes=10)
    async def alert_mode_on(self):
        self.logger.info("Skeleton For Now")
        # if self.alert_mode is True and self.channel_main is not None:
        #     sender = self.get_channel(self.channel_main)
        #     Output = Support.HotInfer("check-safe", self)
        #     Output.description += "\nNotice: This Is An Alert Mode Run"
        #     if "Alert Mode Triggered: True" in Output.description:
        #         self.alert_mode = True
        #     elif "Alert Mode Triggered: False" in Output.description:
        #         self.alert_mode = False
        #     await sender.send(embed=Output)

    @scheduled_capacity_check.before_loop
    async def before_scheduled_capacity_check(self):
        await self.wait_until_ready()

    @alert_mode_on.before_loop
    async def before_alert_mode_on(self):
        await self.wait_until_ready()
