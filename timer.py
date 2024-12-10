import logging
from datetime import datetime
from time import sleep

# Настройка логгера
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    while True:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"🔷 {t}")
        sleep(1)

if __name__ == "__main__":
    main()