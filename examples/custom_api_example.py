import asyncio
from py_zerox import zerox

async def main():
    """
    Custom API Example - Using a custom OpenAI-compatible API endpoint
    """
    print("Custom Zerox - Custom API Example")
    print("=" * 40)
    
    # Example 1: Basic custom API usage
    print("\n1. Basic Custom API Usage:")
    try:
        result = await zerox(
            file_path="path/to/your/document.pdf",  # Replace with your PDF path
            model="gpt-4-vision-preview",  # Your model name
            api_url="https://one.api4gpt.com/v1/chat/completions",  # Your API endpoint
            api_key="your-api-key",  # Your API key
            max_tokens=400,  # Optional: max tokens
            output_dir="./output",  # Save result to file
        )
        
        print(f" Success! Processed {len(result.pages)} pages")
        print(f"  Completion time: {result.completion_time:.2f}ms")
        print(f" Tokens used: {result.input_tokens} input, {result.output_tokens} output")
        
        # Print first page content
        if result.pages:
            print(f"\n First page content preview:")
            print(result.pages[0].content[:200] + "...")
            
    except Exception as e:
        print(f" Error: {e}")
    
    # Example 2: Custom API with additional parameters
    print("\n2. Custom API with Additional Parameters:")
    try:
        result = await zerox(
            file_path="path/to/your/document.pdf",
            model="gpt-4-vision-preview",
            api_url="https://one.api4gpt.com/v1/chat/completions",
            api_key="your-api-key",
            max_tokens=800,  # Higher token limit
            temperature=0.7,  # Custom parameter
            concurrency=5,  # Process 5 pages at once
            maintain_format=True,  # Maintain consistent formatting
            custom_system_prompt="Please convert this document to markdown with special attention to tables and formatting.",
        )
        
        print(f" Success with custom parameters!")
        
    except Exception as e:
        print(f" Error: {e}")
    
    # Example 3: Processing specific pages only
    print("\n3. Processing Specific Pages:")
    try:
        result = await zerox(
            file_path="path/to/your/document.pdf",
            model="gpt-4-vision-preview",
            api_url="https://one.api4gpt.com/v1/chat/completions",
            api_key="your-api-key",
            select_pages=[1, 3, 5],  # Only process pages 1, 3, and 5
        )
        
        print(f" Success! Processed {len(result.pages)} selected pages")
        
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    print(" Starting Custom Zerox Examples...")
    print(" Make sure to replace 'path/to/your/document.pdf' with an actual PDF file path")
    print(" Make sure to replace 'your-api-key' with your actual API key")
    print()
    
    asyncio.run(main())
