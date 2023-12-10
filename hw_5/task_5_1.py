import asyncio
from aiohttp import ClientSession
import os
import sys
import re


async def download_image(session: ClientSession, url: str, target_folder: str, file_prefix: str, file_index: int):
    async with session.get(url) as response:
        if response.status == 200:
            content_type = response.headers['Content-Type']
            extension = re.findall(r"\bimage/\b(\w+)", content_type)[0]

            file_name = f"{file_prefix}_{file_index}.{extension}"
            file_path = os.path.join(target_folder, file_name)

            with open(file_path, "wb") as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)

            print(f"Downloaded {file_name}")
        else:
            print(f"Error {response.status} while downloading image from {url}")


async def main(url: str, target_folder: str, num_files: int):
    os.makedirs(target_folder, exist_ok=True)

    async with ClientSession() as session:
        tasks = []
        for i in range(num_files):
            task = asyncio.ensure_future(download_image(session, url, target_folder, "image", i))
            tasks.append(task)
            await asyncio.sleep(1)  # ну и что то ожидание, зато картинки различные............
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python download_images.py <url> <target_folder> <num_images>")
        sys.exit(1)

    url = sys.argv[1]
    target_folder = sys.argv[2]
    num_files = int(sys.argv[3])

    asyncio.run(main(url, target_folder, num_files))
