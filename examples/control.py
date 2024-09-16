import asyncio

from aiohttp.client import ClientSession
from klyqa.cloud import KlyqaCloud
from klyqa.device import KlyqaDevice
from klyqa.models import Info, RGBColor, State


async def main():
    ## Cloud interaction

    # Login to klyqa cloud
    cloud = KlyqaCloud("email@email.com", "12345678")
    await cloud.login()

    ## Device interaction

    local_device_id = "012345678901"
    print("Trying to get accessToken for device id ", local_device_id)

    # get access token for device from cloud
    access_token = await cloud.get_device_access_token(local_device_id)
    print("Found token: ", access_token)

    # get device name from cloud
    print("Trying to get name for device id ", local_device_id)
    device_name = await cloud.get_device_name(local_device_id)
    print("Found name: ", device_name)

    # Open device connection
    device = KlyqaDevice("192.168.123.123", 3333, access_token, ClientSession())

    # Set device to on, blue, full brightness
    await device.light(
        on=True, color=RGBColor(red=0, green=0, blue=255), brightness=100
    )

    await cloud.close()
    await device.close()


asyncio.run(main())
