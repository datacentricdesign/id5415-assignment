import asyncio
from kasa import SmartBulb
# 'async' transform our main() into an asynchronous function
async def main():
    # Call the definition of a light bulb, replace the IP address with the one found with kasa discover
    bulb = SmartBulb("10.0.1.3")
    # 'await' tells the program to wait till getting a result from the light bulb
    result = await bulb.turn_on()
    # Once we receive it, we call print() to show the result in the Terminal
    print(result)

# We call main() in the asynchronous environment 
asyncio.run(main())