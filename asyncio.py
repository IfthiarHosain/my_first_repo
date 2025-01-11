import time 
import asyncio
import aiohttp
async def function1():
  url = 'https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?auto=compress&cs=tinysrgb&w=600'
  async with aiohttp.ClientSession() as session:
     async with session.get(url) as response:
        content= await response.read()
        with open('google.jpg', 'wb') as file:
         file.write(content)
  print ("madarchod")
  return "main madarchod hoon"

async def function2():
    url = 'http://google.com/favicon.ico'
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as response:
        content= await response.read()
        with open('google.ico2', 'wb') as file: 
         file.write(content)
    return "choda"
async def func3():
    url = 'http://google.com/favicon.ico'
    async with aiohttp.ClientSession() as session:
     async with session.get(url) as response:
        content= await response.read()
        with open('google.ico3', 'wb') as file:
         file.write(content)
async def main():
 L= await asyncio.gather(
       function1(),
       function2(),
       func3()
       )
 print(L)
#asyncio.run(main())
 async def main():
    task=asyncio.create_task(function1())
    await function2()
    await func3()
asyncio.run(main())