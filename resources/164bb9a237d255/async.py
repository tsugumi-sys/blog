import asyncio


class AsyncTask:
    async def run(self):
        print("async task!")
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(AsyncTask().run())
