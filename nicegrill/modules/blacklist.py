#    This file is part of NiceGrill.

#    NiceGrill is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    NiceGrill is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with NiceGrill.  If not, see <https://www.gnu.org/licenses/>.

import logging
from database import blacklistdb as blacklist

class Blacklist:

    async def blacklistxxx(message):
        chat = message.chat_id
        await blacklist.add_blacklist(chat)
        await message.edit("<i>This chat is now blacklisted</i>")


    async def whitelistxxx(message):
        chat = message.chat_id
        if await blacklist.check_blacklist(chat):
            await blacklist.delete_blacklist(chat)
            await message.edit("<i>This chat is now whitelisted</i>")
        else:
            await message.edit("<i>This chat is already whitelisted</i>")
