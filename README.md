# ⚡ Thordata: Global Proxy Network for AI & Web Data

<p align="center">
  Residential, Mobile, ISP & Datacenter proxies, plus Scraping APIs<br/>
  — built for AI pipelines, growth teams, and large-scale data collection.
</p>

<p align="center">
  <a href="https://www.thordata.com/">Website</a> •
  <a href="https://doc.thordata.com">Docs</a> •
  <a href="https://pypi.org/project/thordata-sdk/">Python SDK</a>
</p>

---

## 🧩 Product Overview

Thordata provides a full-stack web data platform:

### 1. Proxy Network (Core)

| Product              | Description                                         |
|----------------------|-----------------------------------------------------|
| Residential Proxy    | City-level IP rotation for difficult targets.      |
| Mobile Proxy         | 4G/5G carrier IPs for mobile-only experiences.     |
| Static ISP Proxy     | Static, ISP-grade IPs with high trust.            |
| Datacenter Proxy     | High-bandwidth IPs for bulk crawling.              |
| Datacenter ISP Proxy | Blended ISP + DC routes for performance & trust.   |

All proxies are exposed via a simple HTTP/HTTPS gateway.

### 2. Scraping APIs

| API                 | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| SERP API            | Real-time Google/Bing/Yandex/DuckDuckGo search results with rich options. |
| Universal Scraping  | JS-rendered HTML/PNG from any URL, bypassing antibot systems.             |
| Web Scraper API     | Task-based scraping using pre-built spiders from the Web Scraper Store.   |

### 3. Data Layer (In Progress)

| Product     | Description                                                 |
|------------|-------------------------------------------------------------|
| Datasets   | Ready-to-use web datasets for AI training and analytics.   |
| Integrations | RAG pipelines, vector databases, and MCP toolchains.     |

---

## 🛠 Open Source Projects

| Repository | Description |
|-----------|-------------|
| **[thordata-python-sdk](https://github.com/Thordata/thordata-python-sdk)** | Official Python SDK for Thordata proxies & scraping APIs. Supports sync/async, SERP, Universal, and Web Scraper APIs. |
| **[thordata-cookbook](https://github.com/Thordata/thordata-cookbook)** | Real-world recipes: RAG pipelines, MCP server for LLMs, GitHub intelligence, app store reviews, and more. |
| **[thordata-proxy-examples](https://github.com/Thordata/thordata-proxy-examples)** | Minimal Python & curl examples for using Thordata's proxy gateway (IP check, basic geo targeting, concurrent requests). |
| **[google-news-scraper](https://github.com/Thordata/google-news-scraper)** | Full Google News scraper using Thordata SERP API (`engine=google_news`), supporting `q`, `gl`, `hl` and advanced tokens, exportable to CSV. |

More language SDKs (Node.js, Go) are planned.

---

## 🚀 Quick Start (Python)

Install the SDK:

```bash
pip install thordata-sdk
```

### 1. Use the Proxy Network

Python

```python
from thordata import ThordataClient

client = ThordataClient(
    scraper_token="YOUR_SCRAPER_TOKEN",
    public_token="YOUR_PUBLIC_TOKEN",
    public_key="YOUR_PUBLIC_KEY",
)

# Send a request through the proxy gateway
resp = client.get("http://httpbin.org/ip")
print(resp.json())
```

### 2. SERP API (Google, Bing, Yandex, DuckDuckGo)

Python

```python
from thordata import ThordataClient, Engine

client = ThordataClient("SCRAPER_TOKEN", "PUBLIC_TOKEN", "PUBLIC_KEY")

results = client.serp_search(
    query="Thordata proxy network",
    engine=Engine.GOOGLE,
    num=10,
    # All engine-specific parameters can be passed via **kwargs
    # e.g. type="shopping", location="United States"
)

print("Organic results:", len(results.get("organic", [])))
```

### 3. Universal Scraping API (HTML / PNG)

Python

```python
from thordata import ThordataClient

client = ThordataClient("SCRAPER_TOKEN", "PUBLIC_TOKEN", "PUBLIC_KEY")

html = client.universal_scrape(
    url="https://www.google.com",
    js_render=True,
    output_format="HTML",
)
print(html[:200])
```

### 4. Web Scraper API (Task-based)

Python

```python
import time
from thordata import ThordataClient

client = ThordataClient("SCRAPER_TOKEN", "PUBLIC_TOKEN", "PUBLIC_KEY")

task_id = client.create_scraper_task(
    file_name="demo_youtube_data",
    spider_id="youtube_video-post_by-url",
    spider_name="youtube.com",
    individual_params={
        "url": "https://www.youtube.com/@stephcurry/videos",
        "order_by": "",
        "num_of_posts": "",
    },
)

for _ in range(10):
    status = client.get_task_status(task_id)
    print("Status:", status)
    if status in ["Ready", "Success"]:
        break
    if status in ["Failed", "Error"]:
        raise RuntimeError("Task failed")
    time.sleep(3)

download_url = client.get_task_result(task_id, file_type="json")
print("Download URL:", download_url)
```

For more examples, see the examples/ directory in the Python SDK and the thordata-cookbook repository.

## 📚 Documentation & Support

- Dashboard: https://www.thordata.com/
- Docs: https://doc.thordata.com
- Python SDK: https://github.com/Thordata/thordata-python-sdk
- Cookbook: https://github.com/Thordata/thordata-cookbook
- Support: mailto:support@thordata.com

<p align="center">
  <i>Thordata powers the proxy network and web data pipelines behind modern AI.</i>
</p>

---
_Last updated: **[11/27/2025]**_
