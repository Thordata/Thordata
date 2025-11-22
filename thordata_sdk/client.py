import requests
from requests.exceptions import RequestException

class ThordataClient:
    """
    Thordata 代理客户端。
    用于封装代理认证信息，并简化 GET/POST 请求的发送。
    """
    def __init__(self, auth_user: str, auth_pass: str, proxy_host: str = "gate.thordata.com", port: int = 22225):
        """
        初始化客户端。

        :param auth_user: 账户的用户名 (e.g., 'thordata-customer')
        :param auth_pass: 账户的密码
        :param proxy_host: Thordata 的代理网关地址
        :param port: 代理端口
        """
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        self.proxy_url = f"http://{auth_user}:{auth_pass}@{proxy_host}:{port}"
        
        # 定义代理字典，requests 库会使用它
        self.proxies = {
            "http": self.proxy_url,
            "https": self.proxy_url,
        }

    def get(self, url: str, **kwargs) -> requests.Response:
        """
        通过 Thordata 代理发送 GET 请求。

        :param url: 目标 URL
        :param kwargs: 传递给 requests.get() 的额外参数（如 headers, timeout 等）
        :return: requests.Response 对象
        """
        print(f"DEBUG: Requesting {url} via {self.proxy_host}")
        
        try:
            # 使用 session 保持连接效率更高，且自动注入代理设置
            with requests.Session() as session:
                session.proxies = self.proxies
                response = session.get(url, **kwargs)
                response.raise_for_status() # 遇到 4xx/5xx 错误时抛出异常
            
            return response

        except RequestException as e:
            print(f"ERROR: Request failed for {url}. Details: {e}")
            raise

    # 简单起见，我们暂时只实现 GET 方法，后续可以添加 POST 等。