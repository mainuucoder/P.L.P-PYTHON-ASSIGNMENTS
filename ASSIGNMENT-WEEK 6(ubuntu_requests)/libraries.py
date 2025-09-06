import os
import requests
from urllib.parse import urlparse
import hashlib

def fetch_images():
    """
    Downloads one or more images from provided URLs.
    
    Features:
    - Uses requests for reliable fetching
    - Handles network and HTTP errors gracefully
    - Creates a dedicated directory for images
    - Prevents duplicate downloads (via content hash)
    - Implements safety checks (content type & size)
    """

    # Prompt for multiple URLs separated by spaces
    urls = input("Enter one or more image URLs (separated by spaces): ").strip().split()

    # Ensure a safe place for downloads
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Track previously downloaded images using hashes
    downloaded_hashes = set()

    for url in urls:
        print(f"\nProcessing: {url}")

        try:
            # Use requests with a friendly User-Agent
            headers = {"User-Agent": "Mozilla/5.0 (compatible; ImageFetcher/1.0)"}
            response = requests.get(url, headers=headers, timeout=10, stream=True)
            response.raise_for_status()  # Ensures 4xx/5xx errors are caught

            # Check important headers
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print("❌ Skipped: Not an image.")
                continue

            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 10 * 1024 * 1024:  # >10 MB
                print("⚠️ Skipped: File too large (over 10MB).")
                continue

            # Read the response safely
            image_data = response.content

            # Check for duplicates using MD5 hash
            file_hash = hashlib.md5(image_data).hexdigest()
            if file_hash in downloaded_hashes:
                print("⚠️ Skipped: Duplicate image detected.")
                continue
            downloaded_hashes.add(file_hash)

            # Derive filename from URL or generate fallback
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                extension = content_type.split("/")[-1] or "jpg"
                filename = f"downloaded_{file_hash[:8]}.{extension}"

            # Save image in binary mode
            save_path = os.path.join(save_dir, filename)
            with open(save_path, "wb") as file:
                file.write(image_data)

            print(f"✅ Saved: {save_path}")

        except requests.exceptions.HTTPError as http_err:
            print(f"❌ HTTP error: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"❌ Network error: {req_err}")
        except Exception as err:
            print(f"❌ Unexpected error: {err}")


if __name__ == "__main__":
    fetch_images()
