import json

def extract_information(json_data, selected_fields):
    manga_list = json_data.get("data", [])  
    
    if not manga_list:
        print("No manga information found in the JSON data.")
        return
    
    for idx, manga_info in enumerate(manga_list, start=1):
        attributes = manga_info.get("attributes", {})
        title = attributes.get("title", {}).get("en", "")
        alt_titles = [alt_title.get("ja-ro", "") for alt_title in attributes.get("altTitles", [])]
        description = attributes.get("description", {}).get("en", "")
        is_locked = attributes.get("isLocked", False)
        links = attributes.get("links", {}).get("raw", "")
        original_language = attributes.get("originalLanguage", "")
        status = attributes.get("status", "")
        year = attributes.get("year", "")
        content_rating = attributes.get("contentRating", "")
        tags = [tag["attributes"]["name"]["en"] for tag in attributes.get("tags", [])]

        author_info = next((rel for rel in manga_info.get("relationships", []) if rel["type"] == "author"), None)
        author_name = author_info["attributes"]["name"] if author_info else ""

        print(f"\nManga Information #{idx}:")

        for field in selected_fields:
            if field == "Title":
                print(f"Title: {title}")
            elif field == "Description":
                print(f"Description: {description}")
            elif field == "Is Locked":
                print(f"Is Locked: {is_locked}")
            elif field == "Original Language":
                print(f"Original Language: {original_language}")
            elif field == "Links":
                print(f"Links: {''.join(links)}")
            elif field == "Status":
                print(f"Status: {status}")
            elif field == "Year":
                print(f"Year: {year}")
            elif field == "Content Rating":
                print(f"Content Rating: {content_rating}")
            elif field == "Tags":
                print(f"Tags: {', '.join(tags)}")
            elif field == "Author":
                print(f"Author: {author_name}")
            elif field == "All":
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Is Locked: {is_locked}")
                print(f"Original Language: {original_language}")
                print(f"Links: {''.join(links)}")
                print(f"Status: {status}")
                print(f"Year: {year}")
                print(f"Content Rating: {content_rating}")
                print(f"Tags: {', '.join(tags)}")
                print(f"Author: {author_name}")

def main():
    file_path = 'library.json'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Display menu
        print("What do you want to extract:")
        print("0. All")
        print("1. Title")
        print("2. Description")
        print("3. Is Locked")
        print("4. Original Language")
        print("5. Links")
        print("6. Status")
        print("7. Year")
        print("8. Content Rating")
        print("9. Tags")
        print("10. Author")

        # Get user input for selected fields
        selected_fields_input = input("Input (comma-separated numbers): ")
        selected_field_numbers = [int(number.strip()) for number in selected_fields_input.split(",")]

        # Convert selected numbers to field names
        field_names = ["All", "Title", "Description", "Is Locked", "Original Language", "Links",
                       "Status", "Year", "Content Rating", "Tags", "Author"]
        selected_fields = [field_names[num] for num in selected_field_numbers]

        # Extract information
        extract_information(json_data, selected_fields)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_path}'.")

if __name__ == "__main__":
    main()
