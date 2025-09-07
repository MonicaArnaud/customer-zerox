import asyncio
from pyzerox import zerox

async def main():
    # 使用自定义API的示例
    result = await zerox(
        file_path="path/to/your/document.pdf",
        model="gpt-4-vision-preview",  # 你的模型名称
        api_url="https://one.api4gpt.com/v1/chat/completions",  # 你的API端点
        api_key="your-api-key",  # 你的API密钥
        max_tokens=400,  # 可选：最大token数
        # 其他可选参数...
    )
    
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
