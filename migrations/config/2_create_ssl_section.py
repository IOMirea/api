from migration import Migration


class Migration2(Migration):
    async def up(self, latest: int) -> None:
        self.config["ssl"] = {
            "cert-chain-path": "CERT-CHAIN-PATH",
            "cert-privkey-path": "CERT-PRIVKEY-PATH"
        }

    async def down(self) -> None:
        self.config.pop("ssl")
