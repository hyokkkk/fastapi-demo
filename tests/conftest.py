# 이 파일은 테스트 시작점이 된다
# testfile이 필요로하는 애플리케이션의 인스턴스를 만듦.

import asyncio
import httpx
import pytest

from main import app
from models.events import Event
from models.users import User

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()