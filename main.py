import json

def extract_information(json_data, selected_fields, result_file):
    manga_list = json_data.get("data", [])  
    
    if not manga_list:
        print("No manga information found in the JSON data.")
        return

    with open(result_file, 'w', encoding='utf-8') as result_file:
        for idx, manga_info in enumerate(manga_list, start=1):
            attributes = manga_info.get("attributes", {})
            title = attributes.get("title", {}).get("en", "")
            alt_titles = [alt_title.get("ja-ro", "") for alt_title in attributes.get("altTitles", [])]
            description = attributes.get("description", {}).get("en", "")
            links = attributes.get("links", {}).get("raw", "")
            original_language = attributes.get("originalLanguage", "")
            status = attributes.get("status", "")
            year = attributes.get("year", "")
            content_rating = attributes.get("contentRating", "")
            tags = [tag["attributes"]["name"]["en"] for tag in attributes.get("tags", [])]

            author_info = next((rel for rel in manga_info.get("relationships", []) if rel["type"] == "author"), None)
            author_name = author_info["attributes"]["name"] if author_info else ""

            print(f"\nManga Information #{idx}:")
            result_file.write(f"\nManga Information #{idx}:\n")

            for field in selected_fields:
                if field == "Title":
                    print(f"Title: {title}")
                    result_file.write(f"Title: {title}\n")
                elif field == "Description":
                    print(f"Description: {description}")
                    result_file.write(f"Description: {description}\n")
                elif field == "Original Language":
                    print(f"Original Language: {original_language}")
                    result_file.write(f"Original Language: {original_language}\n")
                elif field == "Links":
                    print(f"Links: {''.join(links)}")
                    result_file.write(f"Links: {''.join(links)}\n")
                elif field == "Status":
                    print(f"Status: {status}")
                    result_file.write(f"Status: {status}\n")
                elif field == "Year":
                    print(f"Year: {year}")
                    result_file.write(f"Year: {year}\n")
                elif field == "Content Rating":
                    print(f"Content Rating: {content_rating}")
                    result_file.write(f"Content Rating: {content_rating}\n")
                elif field == "Tags":
                    print(f"Tags: {', '.join(tags)}")
                    result_file.write(f"Tags: {', '.join(tags)}\n")
                elif field == "Author":
                    print(f"Author: {author_name}")
                    result_file.write(f"Author: {author_name}\n")
                elif field == "All":
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                    print(f"Original Language: {original_language}")
                    print(f"Links: {''.join(links)}")
                    print(f"Status: {status}")
                    print(f"Year: {year}")
                    print(f"Content Rating: {content_rating}")
                    print(f"Tags: {', '.join(tags)}")
                    print(f"Author: {author_name}")
                    result_file.write(f"Title: {title}\n")
                    result_file.write(f"Description: {description}\n")
                    result_file.write(f"Original Language: {original_language}\n")
                    result_file.write(f"Links: {''.join(links)}\n")
                    result_file.write(f"Status: {status}\n")
                    result_file.write(f"Year: {year}\n")
                    result_file.write(f"Content Rating: {content_rating}\n")
                    result_file.write(f"Tags: {', '.join(tags)}\n")
                    result_file.write(f"Author: {author_name}\n")

def main():
    file_path = 'library.json'
    result_file = 'result.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Display menu
        print("What do you want to extract:")
        print("0. All")
        print("1. Title")
        print("2. Description")
        print("3. Original Language")
        print("4. Links")
        print("5. Status")
        print("6. Year")
        print("7. Content Rating")
        print("8. Tags")
        print("9. Author")


        # Get user input for selected fields
        selected_fields_input = input("Input (comma-separated numbers): ")
        selected_field_numbers = [int(number.strip()) for number in selected_fields_input.split(",")]

        # Convert selected numbers to field names
        field_names = ["All", "Title", "Description", "Original Language", "Links",
                       "Status", "Year", "Content Rating", "Tags", "Author"]
        selected_fields = [field_names[num] for num in selected_field_numbers]

        # Extract information
        extract_information(json_data, selected_fields, result_file)
        print("\nExtraction completed. Results saved to result.txt!")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_path}'.")

if __name__ == "__main__":
    main()
