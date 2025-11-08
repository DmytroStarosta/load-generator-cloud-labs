import asyncio
from project.load_generator import start_generator_load
from my import MY_URL

URL = MY_URL

if __name__ == "__main__":
    while True:
        asyncio.run(start_generator_load(URL, total=300, concurrency=50))
