import multiprocessing
import multiprocessing.pool
import aiohttp
import asyncio

def downloadfile(url,name):
    """Synchronous wrapper to fetch a url and save its content to a file"""
    async def fetch():
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content= await response.read()
                with open(name, 'wb') as file:
                    file.write(content)
    asyncio.run(fetch())
if __name__== "__main__":
    url="https://picsum.photos/id/237/200/300"
    task=[
        ("https://picsum.photos/id/237/200/300" ,"image 1"),
        ("https://picsum.photos/id/237/200/300" ,"image 2"),
        ("https://picsum.photos/id/237/200/300" , "image 3")
    ]
with multiprocessing.Pool(processes=3) as pool:
    pool.starmap(downloadfile,task)