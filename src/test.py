# import asyncio
# from kasa import SmartBulb
# from kasa import Discover
# import time

# bulb = SmartBulb("10.0.1.3")
# asyncio.run(bulb.update())
# asyncio.run(bulb.set_brightness(10, transition=3_000))

# asyncio.run(bulb.set_hsv(0, 100, 80))
# while True:
#     asyncio.run(bulb.set_brightness(10, transition=3_000))
#     time.sleep(3)
# asyncio.run(bulb.set_brightness(1, transition=3_000))
#     time.sleep(3)

# devices = asyncio.run(Discover.discover())
# for addr, dev in devices.items():
#     asyncio.run(dev.update())
#     print(f"{addr} >> {dev}")



# This function 'print' the message 'Turn on the light!' in the Terminal


def main():
    # This function 'print' the message 'The light is on!' in the Terminal
    print("The light is on!")

main()