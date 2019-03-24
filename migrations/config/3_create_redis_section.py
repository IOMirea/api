from migration import Migration


class Migration3(Migration):
    async def up(self, latest: int) -> None:
        self.config["redis"] = {
            "host": "localhost",
            "port": 6380,
            "password": None,
        }

    async def down(self) -> None:
        self.config.pop("redis")
