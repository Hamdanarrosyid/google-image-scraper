from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import requests
import base64

from PIL import Image
from io import BytesIO
import os

def crawler(q: str, scroll: int = 2, folder_name: str = "", size: int = 0):
    print(f"Start Crawling {q}...")

    url = f"https://www.google.com/search?q={q}&source=lnms&tbm=isch"

    driver = webdriver.Chrome()
    driver.get(url)
    path = os.path.join("images", folder_name)
    os.makedirs(path, exist_ok=True)

    for _ in range(scroll):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    images = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")

    for i, image in enumerate(images):
        src = image.get_attribute("src")
        if src is not None:
            if "data:image/jpeg;base64" in src:
                src = src.split(",")[1]
                img = Image.open(BytesIO(base64.b64decode(src)))

                if size != 0:
                    img = img.resize((size, size), Image.LANCZOS)
                img = img.convert("RGB")
                img.save(os.path.join(path, f"{i}.jpg"))
            else:
                try:
                    response = requests.get(src, stream=True, timeout=10)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    if size != 0:
                        img = img.resize((size, size), Image.LANCZOS)
                    img = img.convert("RGB")
                    img.save(os.path.join(path, f"{i}.jpg"))
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading image {i}: {e}")
                except Exception as e:
                    print(f"Error processing image {i}: {e}")


    print("Finish Crawling")


if __name__ == "__main__":
    crawler("cat")