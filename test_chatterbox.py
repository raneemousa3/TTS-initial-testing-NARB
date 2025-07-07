from chatterbox_io import ChatterBox
import asyncio

# Replace with your actual API token from ChatterBox dashboard
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2ODY3OTcxODA4Zjg4YzZlNDdhMjk1ZWYiLCJlbWFpbCI6Im1vdXNhckBzaW1tb25zLmVkdSIsImlhdCI6MTc1MTYxOTM1MiwiZXhwIjoxNzU5Mzk1MzUyfQ.JW1AdEwHlsLms6_utUqiaiZfO1tUKelzTkgA-C6aDhM"

async def handle_transcript(data):
    print(f"Speaker: {data['speaker']}")
    print(f"Text: {data['text']}")

async def main():
    client = ChatterBox(authorization_token=API_TOKEN)
    try:
        # Replace with actual meeting details
        session = await client.send_bot(
            platform="zoom",
            meeting_id="972 1353 2139",
            meeting_password="meeting_password",
            bot_name="MyBot"
        )
        socket = client.connect_socket(session.id)
        socket.on_transcript_received(handle_transcript)
        await socket.connect()
        await socket.wait_closed()
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main()) 
    