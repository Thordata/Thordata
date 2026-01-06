# ⚡ Thordata: Global Proxy Network for AI & Web Data

<p align="center">
  Residential, Mobile, ISP & Datacenter proxies, plus Scraping APIs<br/>
  — built for AI pipelines, growth teams, and large-scale web data collection.
</p>

<p align="center">
  <a href="https://www.thordata.com/">
    <img src="assets/728 x 90 (2).gif" alt="Thordata overview" width="728">
  </a>
</p>

<p align="center">
  <a href="https://www.thordata.com/">Website</a> •
  <a href="https://doc.thordata.com">Docs</a> •
  <a href="https://dashboard.thordata.com">Dashboard</a>
</p>

---

## 🚀 Official SDKs

We provide enterprise-grade, spec-compliant SDKs for major languages. All SDKs support:
*   **Proxy Generation**: Residential, Mobile, Datacenter, ISP with geo-targeting.
*   **SERP API**: Real-time search results (Google, Bing, Yandex).
*   **Web Unlocker**: Universal scraping with antibot bypass.
*   **Web Scraper API**: Async task management for large-scale crawling.

| Language | Package | Version | Features | Links |
| :--- | :--- | :--- | :--- | :--- |
| **Python** | `thordata-sdk` | v1.1.0+ | Sync/Async, Connection Pooling | [![PyPI](https://img.shields.io/pypi/v/thordata-sdk?style=flat-square)](https://github.com/Thordata/thordata-python-sdk) |
| **Node.js** | `thordata-js-sdk` | v1.1.0+ | TypeScript, Proxy Agent | [![NPM](https://img.shields.io/npm/v/thordata-js-sdk?style=flat-square)](https://github.com/Thordata/thordata-js-sdk) |
| **Go** | `thordata-go-sdk` | v1.1.0+ | Generics, High Performance | [![Go Reference](https://pkg.go.dev/badge/github.com/Thordata/thordata-go-sdk.svg)](https://github.com/Thordata/thordata-go-sdk) |
| **Java** | `thordata-java-sdk` | v1.1.0+ | OkHttp, Maven Central | [![Maven](https://img.shields.io/maven-central/v/com.thordata/thordata-java-sdk?style=flat-square)](https://github.com/Thordata/thordata-java-sdk) |

---

## 🧩 Product Overview

### 1. Proxy Network (Core)

| Product              | Description                                         | Port |
|----------------------|-----------------------------------------------------|------|
| **Residential**      | 90M+ IPs, City-level targeting, rotating/sticky.    | 9999 |
| **Mobile**           | 4G/5G carrier IPs for mobile-first scraping.        | 5555 |
| **Datacenter**       | High-speed IPs for bulk data collection.            | 7777 |
| **Static ISP**       | Stable, long-term IPs with high trust scores.       | 6666 |

### 2. Scraping APIs

| API                | Capability                                                                 |
|--------------------|----------------------------------------------------------------------------|
| **SERP API**       | Real-time search results from Google, Bing, Yandex, DuckDuckGo.            |
| **Universal API**  | JS-rendered HTML/PNG from any URL, automatically bypassing CAPTCHAs.       |
| **Web Scraper API**| Task-based asynchronous scraping (Text & Video/Audio) for massive scale.   |

---

## 🛠️ Quick Start (Python Example)

```python
# pip install thordata-sdk
from thordata import ThordataClient, ProxyConfig, ProxyProduct, Engine

# 1. Initialize
client = ThordataClient(scraper_token="YOUR_TOKEN")

# 2. Use Proxy Network (High Performance)
# SDK handles connection pooling automatically
proxy = ProxyConfig(
    username="user", password="pass",
    product=ProxyProduct.RESIDENTIAL,
    country="us",
    city="new_york"
)
resp = client.get("https://httpbin.org/ip", proxy_config=proxy)
print(resp.json())

# 3. SERP Search
results = client.serp_search("Thordata SDK", engine=Engine.GOOGLE)
print(results["organic"][0]["link"])

# 4. Universal Scrape (Web Unlocker)
html = client.universal_scrape("https://example.com", js_render=True)
```

---

## 📚 Ecosystem

- **[thordata-sdk-spec](https://github.com/Thordata/thordata-sdk-spec)**: The canonical specification for all SDKs.
- **[API Reference](https://thordata.github.io/thordata-sdk-spec/)**: Auto-generated API documentation.
- **[Mock Server](https://github.com/Thordata/thordata-sdk-spec/pkgs/container/thordata-sdk-spec%2Fmock-server)**: Dockerized mock server for offline development.

---

## 🤝 Support

- **Official website:** https://www.thordata.com/
- **Dashboard:** https://dashboard.thordata.com/
- **Docs:** https://doc.thordata.com
- **Email:** support@thordata.com

<p align="center">
  <sub>Last updated: <b>2026-01-06</b></sub>
</p>