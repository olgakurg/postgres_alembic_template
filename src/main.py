from core.config import settings
from core.logger import logger


def main() -> int:
    logger.info("i am main")
    return settings.some_setting


if __name__ == "__main__":
    print(main())
