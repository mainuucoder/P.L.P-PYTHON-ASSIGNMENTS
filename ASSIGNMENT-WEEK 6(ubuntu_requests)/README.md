# Ubuntu_Requests


# Image Fetcher

A Python script for safely downloading one or more images from URLs.  
It emphasizes **reliability**, **error handling**, and **respectful resource usage**, in line with Ubuntu principles of community and respect.

---

## ✨ Features

- ✅ **Multiple URL support** — download several images at once.  
- ✅ **Safe downloads** — checks that the file is actually an image.  
- ✅ **Error handling** — gracefully handles HTTP errors, timeouts, and invalid URLs.  
- ✅ **Directory management** — automatically creates a `Fetched_Images/` directory if it doesn’t exist.  
- ✅ **Duplicate prevention** — uses an MD5 hash to avoid saving the same image twice.  
- ✅ **File size safeguard** — skips files larger than 10 MB.  
- ✅ **Smart filenames** — extracts a filename from the URL, or generates one if missing.  

---

## 🛠 Requirements

- Python 3.7+  
- [`requests`](https://docs.python-requests.org/) library  

Install dependencies with:

```bash
pip install requests
````

---

## 🚀 Usage

1. Clone or download this repository.
2. Run the script:

```bash
python fetch_images.py
```

3. Enter one or more image URLs, separated by spaces:

```text
Enter one or more image URLs (separated by spaces): https://example.com/cat.jpg https://example.com/dog.png
```

4. The images will be saved in the `Fetched_Images/` directory.

---

## 🔒 Precautions

This script follows good security and community practices:

* **Validates content type**: Only saves files with `Content-Type: image/*`.
* **Respects resources**: Skips images larger than 10 MB.
* **Prevents duplicates**: Detects identical images by computing an MD5 hash.
* **Polite requests**: Uses a custom `User-Agent` header.

---

## 📂 File Management

* All images are stored in the `Fetched_Images/` directory.
* Filenames are taken from the URL path.
* If no filename exists, a unique one is generated using part of the image’s hash.

Example:

```
Fetched_Images/
├── cat.jpg
├── dog.png
└── downloaded_a1b2c3d4.jpg
```

---

## ⚡ Error Handling

The script provides clear messages in case of issues:

* `❌ Skipped: Not an image.` → URL does not point to an image.
* `⚠️ Skipped: File too large.` → Image exceeds the 10 MB safety limit.
* `⚠️ Skipped: Duplicate image detected.` → Already downloaded.
* `❌ HTTP error: 404 Client Error` → URL not found.
* `❌ Network error: Timeout` → Connection issue.

---

## 🤝 Ubuntu Principles of Community & Respect

* **Community-minded**: Ensures responsible and ethical use of internet resources.
* **Respectful**: Avoids excessive downloads, duplicate files, or unnecessary storage.
* **Transparent**: Clear messages inform the user about success, skips, or errors.

---


```
