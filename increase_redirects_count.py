import asyncio
import aiohttp


base_url = 'http://localhost:8000/'


async def send(short_link: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + f'{short_link}/') as response:
            return response.status


async def main(redirects_count: int, short_link: str) -> None:
    status_code = await send(short_link)

    if status_code == 404:
        print('Short link is invalid')
        return

    tasks = []
    for _ in range(redirects_count - 1):
        tasks.append(asyncio.create_task(send(short_link)))
        await asyncio.sleep(0.3)

    await asyncio.gather(*tasks)
    print(f'{redirects_count} redirects successfully completed.')


if __name__ == '__main__':
    redirects_count = int(input('Redirects count: '))
    short_link = str(input('Short link: '))
    asyncio.run(main(redirects_count, short_link))
