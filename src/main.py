from __future__ import annotations

from db.postgres import async_session
from db.fake_repo import proto_add, proto_selectin, proto_streaming_selectin
# from core.logger import logger
# import time

import asyncio




async def async_main():
    """Main program function."""

    await proto_add(value="some_value", async_session=async_session)
    await proto_selectin(value="a1", async_session=async_session)
    await proto_streaming_selectin(value="a2", async_session=async_session)


if __name__ == "__main__":
    print("asyncio start")
    try:
        asyncio.run(async_main())
    except Exception as e:
        print(f"loop is broken because of {e}")
