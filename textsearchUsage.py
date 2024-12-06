import requests

def search_documents(search_text, status=None, priority=None, category=None):
    """
    Search documents with optional filters
    
    Args:
        search_text (str): Text to search for
        status (str, optional): Filter by status
        priority (str, optional): Filter by priority
        category (str, optional): Filter by category
    """
    # Base URL with search text
    url = f"http://localhost:5000/api/search?q={search_text}"
    
    # Add optional filters
    if status:
        url += f"&status={status}"
    if priority:
        url += f"&priority={priority}"
    if category:
        url += f"&category={category}"
        
    response = requests.get(url)
    return response.json()

def get_available_filters():
    """Get available filter values"""
    response = requests.get("http://localhost:5000/api/filters")
    return response.json()

# Example usage
if __name__ == "__main__":
    # Get available filters
    filters = get_available_filters()
    print("Available categories:", filters["categories"])
    
    # Simple text search
    results = search_documents("appendix")
    print("\nSimple search results:", results["count"])
    
    # Search with filters
    results = search_documents(
        search_text="methodology",
        status="Pending",
        priority="Critical"
    )
    print("\nFiltered search results:", results["count"])
    
    # Print first result details
    if results["results"]:
        first_result = results["results"][0]
        print("\nTop result:")
        print(f"Category: {first_result['Category']}")
        print(f"Comment: {first_result['Comment']}")
        print(f"Score: {first_result['score']}")