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
  <a href="https://dashboard.thordata.com">Dashboard</a> •
  <a href="https://pypi.org/project/thordata-sdk/">Python SDK (PyPI)</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/thordata-sdk/">
    <img src="https://img.shields.io/pypi/v/thordata-sdk?label=thordata-sdk&style=flat-square" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/thordata-sdk/">
    <img src="https://img.shields.io/pypi/pyversions/thordata-sdk?style=flat-square" alt="Python versions">
  </a>
  <a href="https://github.com/Thordata/thordata-python-sdk/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Thordata/thordata-python-sdk?style=flat-square" alt="License">
  </a>
</p>

---

## 🧩 Product Overview

Thordata provides a full‑stack web data platform:

### 1. Proxy Network (Core)

| Product              | Description                                         |
|----------------------|-----------------------------------------------------|
| Residential Proxy    | City‑level IP rotation for difficult targets.       |
| Mobile Proxy         | 4G/5G carrier IPs for mobile‑only experiences.      |
| Static ISP Proxy     | Static, ISP‑grade IPs with high trust.             |
| Datacenter Proxy     | High‑bandwidth IPs for bulk crawling.              |
| Datacenter ISP Proxy | Blended ISP + DC routes for performance & trust.   |

All proxies are exposed via a simple HTTP/HTTPS gateway.

### 2. Scraping APIs

| API                | Description                                                                  |
|--------------------|------------------------------------------------------------------------------|
| SERP API           | Real‑time Google/Bing/Yandex/DuckDuckGo search results with rich options.   |
| Universal Scraper  | JS‑rendered HTML/PNG from any URL, bypassing antibot systems.               |
| Web Scraper API    | Task‑based scraping using pre‑built spiders from the Web Scraper Store.     |

### 3. Data Layer (In Progress)

| Product      | Description                                                 |
|-------------|-------------------------------------------------------------|
| Datasets    | Ready‑to‑use web datasets for AI training and analytics.    |
| Integrations| RAG pipelines, vector databases, MCP toolchains, and more.  |

---

## ⚙️ SDKs & Core Clients

Official SDKs and low‑level clients for accessing Thordata products.

- **[thordata-python-sdk](https://github.com/Thordata/thordata-python-sdk)**  
  Modern Python SDK (published as `thordata-sdk`) with sync & async clients for:
  Residential / Datacenter / Mobile proxies, SERP API, Universal Scraper API,
  and Web Scraper task management.

> **Planned:**
> - **thordata-node-sdk** — Node.js SDK for proxies + SERP  
> - **thordata-go-sdk** — Go SDK for proxy & scraping workloads

---

## 🤖 AI & LLM Integrations

Tools and examples that connect Thordata with AI agents, RAG pipelines,
and model tool ecosystems.

- **[thordata-cookbook](https://github.com/Thordata/thordata-cookbook)**  
  A collection of end‑to‑end recipes:
  - RAG data pipeline with Universal Scraper → HTML cleaning → Markdown
  - Web QA Agent: question → SERP search → page scraping → LLM answer
  - MCP tools: expose `search_web`, `search_news`, `read_website`, `extract_links` to LLMs
  - GitHub repository intelligence and app‑store review analysis

- **[thordata-langchain-tools](https://github.com/Thordata/thordata-langchain-tools)**  
  LangChain tools powered by Thordata:
  - `ThordataSerpTool` — real‑time web search via SERP API  
  - `ThordataScrapeTool` — universal single‑page scraping with optional JS rendering

---

## 🌍 Proxy & Network Examples

Quick‑start examples for using Thordata's proxy network.

- **[thordata-proxy-examples](https://github.com/Thordata/thordata-proxy-examples)**  
  Minimal examples showing how to:
  - Send HTTP requests via Thordata Residential / Mobile / Datacenter proxies (Python + curl)
  - Configure basic geo‑targeting (country / city‑level)
  - Run concurrent IP checks and simple health monitoring

> **Planned:**
> - **thordata-proxy-docker** — dockerized local forward proxy using Thordata credentials

---

## 📰 Google & SERP Examples

SERP‑based examples focused on Google and news use cases.

- **[google-news-scraper](https://github.com/Thordata/google-news-scraper)**  
  Full‑featured CLI example for `engine=google_news`, supporting:
  - `q` (query), `hl` (language), `gl` (country)
  - `topic_token`, `publication_token`, `section_token`, `story_token`, `so`
  - CSV export of structured news results via Thordata SERP API

> **Planned:**
> - Generic Google web search examples (`engine=google`)  
> - Google Maps / Play / Shopping examples as separate repositories

---

## 📚 Tutorials & Notebooks

Hands‑on guides and notebooks to help you build data pipelines on top of Thordata.

Most of these live in **[thordata-cookbook](https://github.com/Thordata/thordata-cookbook)**:

- `notebooks/rag/rag_openai_research.ipynb` —  
  Prepare dynamic HTML content (e.g. OpenAI Research) for RAG by scraping,
  cleaning, and exporting to Markdown.

- `notebooks/devtools/github_repo_intel.ipynb` —  
  Use Web Scraper API spiders to collect GitHub repository metadata
  (stars, issues, contributors, languages) into a Pandas DataFrame.

- `notebooks/ai/web_qa_agent_with_thordata.ipynb` —  
  End‑to‑end "Web Q&A Agent":
  question → SERP search → Universal Scraper → HTML cleaning → LLM answer.

All notebooks support:

- **Live mode** — call Thordata APIs and cache results under `data/`  
- **Offline mode** — reuse cached HTML/JSON without consuming credits

---

## 🚀 Quick Start (Python)

### Install the SDK:

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
    # Pass engine‑specific params via **kwargs, e.g.:
    # type="news", location="United States"
)

print("Organic results:", len(results.get("organic", [])))
```

### 4. Universal Scraper (HTML)

```python
html = client.universal_scrape(
    url="https://www.thordata.com",
    js_render=True,
    output_format="HTML",
)
print(html[:500])
```

---

## 📚 Further Resources

For more advanced examples (Web Scraper tasks, async high‑concurrency,
RAG pipelines, MCP tools), see:

- **SDK examples** → thordata-python-sdk/examples
- **Cookbook scripts & notebooks** → thordata-cookbook

---

## 🤝 Community & Support

- **Dashboard:** https://www.thordata.com/
- **Docs:** https://doc.thordata.com
- **Python SDK:** https://github.com/Thordata/thordata-python-sdk
- **Cookbook:** https://github.com/Thordata/thordata-cookbook
- **Support:** support@thordata.com

If you are building something interesting on top of Thordata
(RAG pipelines, AI agents, dashboards), feel free to open an issue
and share your project — we are happy to feature selected community examples.

---

<p align="center">
  <i>Thordata powers the proxy network and web data pipelines behind modern AI.</i>
</p>

<p align="center">
  <sub>Last updated: <b>2025‑12‑01</b></sub>
</p>

---