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

## 🧩 Product Overview

Thordata provides a full‑stack web data platform:

### 1. Proxy Network (Core)

| Product | Description |
|---------|-------------|
| Residential Proxy | City‑level IP rotation for difficult targets. |
| Mobile Proxy | 4G/5G carrier IPs for mobile‑only experiences. |
| Static ISP Proxy | Static, ISP‑grade IPs with high trust. |
| Datacenter Proxy | High‑bandwidth IPs for bulk crawling. |
| Datacenter ISP Proxy | Blended ISP + DC routes for performance & trust. |

All proxies are exposed via a simple HTTP/HTTPS gateway.

### 2. Scraping APIs

| API | Description |
|-----|-------------|
| SERP API | Real‑time Google/Bing/Yandex/DuckDuckGo search results with rich options. |
| Universal Scraper | JS‑rendered HTML/PNG from any URL, bypassing antibot systems. |
| Web Scraper API | Task‑based scraping using pre‑built spiders from the Web Scraper Store. |

### 3. Data Layer (In Progress)

| Product | Description |
|---------|-------------|
| Datasets | Ready‑to‑use web datasets for AI training and analytics. |
| Integrations | RAG pipelines, vector databases, MCP toolchains, and more. |

---

## ⚙️ Official SDKs

We provide official, spec-compliant SDKs for all major languages. All SDKs support Proxy generation, SERP, Universal API, and Task management.

| Language | Package | Version | Status |
|----------|---------|---------|--------|
| Python | thordata-sdk | v1.0.1+ | 🟢 Stable |
| Node.js | thordata-js-sdk | v1.0.1+ | 🟢 Stable |
| Go | thordata-go-sdk | v1.0.1+ | 🟢 Stable |
| Java | thordata-java-sdk | v1.0.1+ | 🟢 Stable |

Each SDK includes built-in retry logic, connection pooling (where applicable), and strict type hints.

---

## 🤖 AI & LLM Integrations

Tools and examples that connect Thordata with AI agents, RAG pipelines, and model tool ecosystems.

### thordata-cookbook

A collection of end‑to‑end recipes:

- RAG data pipeline with Universal Scraper → HTML cleaning → Markdown
- Web QA Agent: question → SERP search → page scraping → LLM answer
- MCP tools: expose search_web, search_news, read_website, extract_links to LLMs
- GitHub repository intelligence and app‑store review analysis

### thordata-langchain-tools

LangChain tools powered by Thordata:

- **ThordataSerpTool** — real‑time web search via SERP API
- **ThordataScrapeTool** — universal single‑page scraping with optional JS rendering

### thordata-web-qa-agent

CLI Web Q&A agent: question → Thordata SERP → Universal Scraper → HTML cleaning → OpenAI answer.

---

## 🚀 Quick Start (Python)

Install the SDK:

```bash
pip install thordata-sdk
```

### 1. Initialize the client

```python
from thordata import ThordataClient

client = ThordataClient(
    scraper_token="YOUR_SCRAPER_TOKEN",
    public_token="YOUR_PUBLIC_TOKEN",
    public_key="YOUR_PUBLIC_KEY",
)
```

### 2. Send a request via the proxy network

```python
resp = client.get("http://httpbin.org/ip")
print(resp.json())  # → see your Thordata exit IP
```

### 3. Run a SERP search

```python
from thordata import Engine

results = client.serp_search(
    query="Thordata proxy network",
    engine=Engine.GOOGLE,
    num=5,
)

print("Organic results:", len(results.get("organic", [])))
```

### 4. Universal Scraper (HTML)

```python
html = client.universal_scrape(
    url="https://www.thordata.com",
    js_render=True,
    output_format="html",
)

print(html[:500])
```

---

## 🤝 Community & Support

| Resource | Link |
|----------|------|
| Dashboard | https://dashboard.thordata.com/ |
| Docs | https://doc.thordata.com |
| Support | support@thordata.com |

If you are building something interesting on top of Thordata (RAG pipelines, AI agents, dashboards), feel free to open an issue and share your project — we are happy to feature selected community examples.

---

<p align="center">
  <i>Thordata powers the proxy network and web data pipelines behind modern AI.</i>
</p>

<p align="center">
  <sub>Last updated: <b>2026‑01‑05</b></sub>
</p>
