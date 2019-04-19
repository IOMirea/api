"""
IOMirea-server - A server for IOMirea messenger
Copyright (C) 2019  Eugene Ershov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from migration import DBMigration


class Migration(DBMigration):
    async def up(self, latest: int) -> None:
        await self.conn.execute(
            """
            ALTER TABLE messages ADD CONSTRAINT messages_channelid_fkey FOREIGN KEY (channel_id) REFERENCES channels(id);
            ALTER TABLE messages ADD CONSTRAINT messages_authorid_fkey FOREIGN KEY (author_id) REFERENCES users(id);
                               
            ALTER TABLE files ADD CONSTRAINT files_channelid_fkey FOREIGN KEY (channel_id) REFERENCES channels(id);
            ALTER TABLE files ADD CONSTRAINT files_messageid_fkey FOREIGN KEY (message_id) REFERENCES messages(id);
                                                                                                                                                                                    
            ALTER TABLE bugreports ADD CONSTRAINT bugreports_userid_fkey FOREIGN KEY (user_id) REFERENCES users(id);
   
            ALTER TABLE tokens ADD CONSTRAINT tokens_userid_fkey FOREIGN KEY (user_id) REFERENCES users(id);
            ALTER TABLE tokens ADD CONSTRAINT tokens_appid_fkey FOREIGN KEY (app_id) REFERENCES applications(id) ON DELETE CASCADE;
            """
                                                                                                                                                                                                                                                        )
                    
