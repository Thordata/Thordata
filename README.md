<div align="center">
  <h1>⚡ Thordata Ecosystem</h1>
  <p>
    <strong>The AI-Native Web Data Infrastructure.</strong><br>
    Connect LLMs, Agents, and RAG pipelines to the real-world web.
  </p>
  
  <p>
    <a href="https://www.thordata.com">🌐 Website</a> • 
    <a href="https://doc.thordata.com">📚 Documentation</a> • 
    <a href="https://dashboard.thordata.com">📊 Dashboard</a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Status-Active_Construction-yellow" alt="Status">
    <img src="https://img.shields.io/badge/Network-60M%2B_IPs-blue" alt="Network">
    <img src="https://img.shields.io/badge/Uptime-99.9%25-success" alt="Uptime">
    <img src="https://img.shields.io/badge/Focus-AI_&_Scraping-purple" alt="Focus">
  </p>
</div>

---

> **🚧 UNDER CONSTRUCTION**: We are currently performing a massive upgrade to our open-source ecosystem (Jan-Feb 2026). We are refactoring our SDKs to be strictly typed, adding MCP support, and releasing new AI agent templates. Stay tuned!

## 📖 About Thordata

Thordata is not just a proxy provider; we are the **data layer for the AI era**. We provide the infrastructure that allows developers, data scientists, and AI agents to access public web data reliably, anonymously, and at scale.

With a network of **60M+ Ethical Residential IPs** and advanced **Web Unlocking** technology, we handle the complexity of fingerprints, captchas, and retries so you can focus on the data.

---

## 🏗️ Repository Map

We organize our open-source projects into layers, from core infrastructure to high-level AI agents.

### 🔹 Layer 1: Core / Official SDKs
The fundamental building blocks for integrating Thordata into your stack.

| Repository | Language | Description | Status |
| :--- | :--- | :--- | :--- |
| [**thordata-python-sdk**](https://github.com/Thordata/thordata-python-sdk) | Python | 🐍 **Flagship SDK**. Async support, fully typed, Pandas integration. The standard for data pipelines. | 🟢 Stable |
| [**thordata-js-sdk**](https://github.com/Thordata/thordata-js-sdk) | Node.js | 📦 **TypeScript**. Built for serverless environments and Puppeteer/Playwright control. | 🟡 Refactoring |
| [**thordata-go-sdk**](https://github.com/Thordata/thordata-go-sdk) | Go | 🐹 **High Performance**. Designed for massive concurrency and enterprise-grade scrapers. | 🟡 Refactoring |
| [**thordata-java-sdk**](https://github.com/Thordata/thordata-java-sdk) | Java | ☕ **Enterprise**. Thread-safe, rigid implementation for legacy banking/enterprise systems. | 🟡 Refactoring |

### 🔹 Layer 2: Integrations (AI & LLM)
Native protocols to connect Thordata with the modern AI stack.

| Repository | Protocol | Description | Status |
| :--- | :--- | :--- | :--- |
| [**thordata-mcp-server**](https://github.com/Thordata/thordata-mcp-server) | **MCP** | 🤖 **Model Context Protocol** implementation. Connect Claude Desktop / OpenAI directly to Thordata tools. | 🔥 **NEW** |
| [**thordata-langchain-tools**](https://github.com/Thordata/thordata-langchain-tools) | LangChain | 🦜🔗 Official LangChain Tool definitions. Give your Agents "Browsing" capabilities. | 🟢 Stable |
| [**thordata-rag-pipeline**](https://github.com/Thordata/thordata-rag-pipeline) | Vector DB | 🧠 End-to-end pipeline: Scrape -> Clean -> Chunk -> Embed. Optimized for RAG. | 🚧 Beta |

### 🔹 Layer 3: Solutions / SEO (Specialized Scrapers)
Ready-to-use scraper templates for specific high-value targets. **Batteries included.**

| Repository | Target | Features |
| :--- | :--- | :--- |
| [**amazon-product-scraper-python**](https://github.com/Thordata/amazon-product-scraper-python) | E-commerce | Extracts Price, Rating, Reviews, Images. Handles ASINs and Search. |
| [**google-maps-scraper-python**](https://github.com/Thordata/google-maps-scraper-python) | Local SEO | Extracts Business Info, Reviews, Lat/Long, Operating Hours. |
| [**google-news-scraper-python**](https://github.com/Thordata/google-news-scraper-python) | Intelligence | Monitor keywords, brand mentions, and financial news in real-time. |
| [**social-media-scraper-suite**](https://github.com/Thordata) | Social | *Coming Soon*: Unified interface for Twitter(X), LinkedIn, and Reddit data. |

### 🔹 Layer 4: Agents & Apps
Full-blown applications and demos showcasing the power of Thordata.

| Repository | Type | Description |
| :--- | :--- | :--- |
| [**thordata-web-qa-agent**](https://github.com/Thordata/thordata-web-qa-agent) | Demo Agent | An AI Agent that searches the web to answer complex questions (Perplexity-style clone). |
| [**google-play-reviews-rag**](https://github.com/Thordata/google-play-reviews-rag) | Analytics | Sentiment analysis pipeline for App Store reviews using local LLMs. |

### 🔹 Layer 5: Examples
| Repository | Description |
| :--- | :--- |
| [**thordata-cookbook**](https://github.com/Thordata/thordata-cookbook) | 🍳 **"Copy-Paste" Recipes**. 50+ examples covering everything from Setting headers to Handling Captchas. |

---

## 🛠️ Product Capabilities Overview

### 1. Proxy Network (The Foundation)
Access the world's most stable proxy network.
*   **Residential Proxies**: 60M+ IPs, Real devices, Ethical compliance.
*   **Mobile Proxies**: 3G/4G/5G IPs for high-trust mobile app verification.
*   **ISP Proxies**: Static residential IPs for keeping sessions alive.
*   **Datacenter Proxies**: High speed, cost-effective bandwidth.

### 2. Web Unlocking (The Technology)
Stop worrying about being blocked.
*   **Web Unlocker API**: A simple API endpoint that automatically handles:
    *   Captcha Solving (ReCaptcha, hCaptcha, Cloudflare, etc.)
    *   TLS Fingerprint Spoofing
    *   JavaScript Rendering
    *   Automatic Retries & Rotation

### 3. Scraping Browser (The Interface)
Run your Puppeteer/Playwright/Selenium scripts on our cloud browsers.
*   **CDP (Chrome DevTools Protocol)** support.
*   Scale to thousands of concurrent browsers without managing infrastructure.

---

## 🤝 Contribution & License

This ecosystem is open for contributions!
*   All SDKs are licensed under **MIT**.
*   We welcome Pull Requests for bug fixes and new features.
*   Please check the `CONTRIBUTING.md` in each repository.

<br>
<div align="center">
  <sub>Powered by <a href="https://www.thordata.com">Thordata</a>. Empowering the AI revolution with Data.</sub>
</div>