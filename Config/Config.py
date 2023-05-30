import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "12233538")
        self.API_HASH: str = os.environ.get("API_HASH", "1140f52873a95287478ab500019370c0")
        self.SESSION: str = os.environ.get("SESSION", "BABdzmj3Yp6tapTeNpvF8vUnC5eeR8E5_tlmLo7wqdMpMjTM98l7mpH4baijSBYm1hnswV4aXCOXW6qvu9C657XvfdBg_-7kWM4ZQpaj52ViICS0hnaDosvI9IO0hie8lvNVcaJSkecvkGbxtLuYPU8ab1xpCSHmACgzVTHgR8FvVXGIey2rImpXn7wmqp9AMwa_ZJl0MDGD9AzzcJj9pk43kfQVZbnuyyL75ApGjl17jdxMiQumYb495da_i9MmmzWf2P-UgBvXZFoX8b0_PIIKwSMX56aupi5BePY924ELa2EAXDxyN5T_8x-vqYHj-TL3LgxlXMCF5D8svU4CKVHLf52_-gA")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "1158888206").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()


config = Config()
