
from openai import OpenAI
import requests
from requests.models import Response
import os
from enum import Enum

class OpenAPIProxyType(Enum):
    Completion = "completions"

class OpenAPIProxy:

    def_header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv("OPENAI_API_KEY")}"
        }
    
    proxy_urls = {
        OpenAPIProxyType.Completion: "https://api.openai.com/v1/chat/completions"
    }

    @classmethod
    def send_request(cls, 
                     app_object: dict, 
                     role_object: dict, 
                     content: dict,
                     proxy_type: OpenAPIProxyType = OpenAPIProxyType.Completion) -> Response:

        data = {}
        data.update(app_object)
        data.update(role_object)
        data.update(content)

        headers = cls.gen_headers(proxy_type)
        url = cls.proxy_urls.get(proxy_type)

        response: Response = requests.post(url=url, 
                                 headers=headers, 
                                 json=data)
        
        return response
        
    @classmethod
    def gen_headers(cls, proxy_type: OpenAPIProxyType):

        header = cls.def_header.copy()

        match (proxy_type):
            case OpenAPIProxyType.Completion:
                pass
            case _:
                raise RuntimeError("ProxyType error: " + proxy_type)
            
        return header