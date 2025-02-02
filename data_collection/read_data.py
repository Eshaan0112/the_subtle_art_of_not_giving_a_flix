import requests
import pandas as pd
import time

def fetch_books(query, max_books=1000, max_results=40):
    """Query google API to fetch books

    Args:
        query ([type]): [description]
        max_books (int, optional): [description]. Defaults to 1000.
        max_results (int, optional): [description]. Defaults to 40.

    Returns:
        [type]: [description]
    """
    books_data = []
    start_index = 0
    total_fetched = 0

    while total_fetched < max_books:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&startIndex={start_index}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error fetching data for query '{query}'")
            break

        books = response.json().get("items", [])
        if not books:
            break

        for book in books:
            volume_info = book.get("volumeInfo", {})
            books_data.append({
                "Title": volume_info.get("title", "N/A"),
                "Authors": ", ".join(volume_info.get("authors", ["N/A"])),
                "Published Date": volume_info.get("publishedDate", "N/A"),
                "Categories": ", ".join(volume_info.get("categories", ["N/A"])),
                "Average Rating": volume_info.get("averageRating", "N/A"),
                "Ratings Count": volume_info.get("ratingsCount", "N/A"),
                "Description": volume_info.get("description", "N/A"),
                "Page Count": volume_info.get("pageCount", "N/A"),
                "Language": volume_info.get("language", "N/A"),
                "Thumbnail": volume_info.get("imageLinks", {}).get("thumbnail", "N/A"),
            })

        total_fetched += len(books)
        start_index += max_results
        time.sleep(1)  # avoid API rate limits

    return books_data


if __name__=="__main__":
    # Define diverse search queries
    queries = ["fiction", "non-fiction", "science", "history", "fantasy", "technology", "romance", "mystery", "self-help"]
    books_dataset = []

    # Fetch books for each query
    for query in queries:
        print(f"Genre being queried:{query}")
        books_dataset.extend(fetch_books(query, max_books=1000))  

    # Convert to DataFrame and save
    df_books = pd.DataFrame(books_dataset)
    df_books.to_csv("books_dataset.csv", index=False)

    print(f"Total Books Fetched: {len(df_books)}")
    print(df_books.head())