import os
import requests

from config.settings import PEXELS_API_KEY


PEXELS_URL = "https://api.pexels.com/v1/search"


def download_image(keyword, save_folder="images"):
    """
    Search an image on Pexels using a keyword,
    download the first result,
    and return the local image path.
    """

    os.makedirs(save_folder, exist_ok=True)

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": keyword,
        "per_page": 1
    }

    try:
        response = requests.get(
            PEXELS_URL,
            headers=headers,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        photos = data.get("photos", [])

        if not photos:
            print(f"No image found for: {keyword}")
            return None

        image_url = photos[0]["src"]["large"]

        filename = (
            keyword.replace(" ", "_")
            .replace("/", "_")
            .lower()
            + ".jpg"
        )

        image_path = os.path.join(save_folder, filename)

        image_response = requests.get(image_url, timeout=30)

        image_response.raise_for_status()

        with open(image_path, "wb") as f:
            f.write(image_response.content)

        print(f"Downloaded image: {image_path}")

        return image_path

    except Exception as e:
        print(f"Image Download Error: {e}")
        return None