"""
key_loader.py
统一加载 API Key。

Web 端大模型调用应优先使用登录用户在“系统设置”中保存的 Key。
此模块仅保留环境变量读取能力，供命令行脚本或本地调试使用。
"""

import os
from typing import Optional


def get_api_key(provider: str) -> Optional[str]:
    """
    根据 provider 从环境变量获取 API Key。

    provider:
        - deepseek
        - dashscope
    """
    provider = (provider or "").strip().lower()

    if provider == "deepseek":
        return os.getenv("DEEPSEEK_API_KEY") or None

    if provider == "dashscope":
        return os.getenv("DASHSCOPE_API_KEY") or None

    return None
