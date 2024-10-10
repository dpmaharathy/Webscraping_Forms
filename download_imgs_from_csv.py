import csv
import requests
import os
import re

# Function to create a valid filename
def create_valid_filename(title, image_url):
    # Remove invalid characters for Windows filenames
    filename = re.sub(r'[<>:"/\\|?*]', '_', title)
    # Extract the file extension from the URL, ignoring query parameters
    extension = os.path.splitext(image_url.split('?')[0])[-1]
    return filename + extension

# Create a directory to save the downloaded images
output_dir = 'income_tax_forms'
os.makedirs(output_dir, exist_ok=True)

# Open the CSV file and read the image URLs
csv_file_path = r'C:\Users\HP\Downloads\Forms_Scraping\income_tax_forms.csv'
with open(csv_file_path, encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        title = row['Title']
        source = row['Source']
        image_url = row['High Resolution Image']

        # Get the image content
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for request errors

            # Create a valid filename from the title and image URL
            filename = create_valid_filename(title, image_url)
            file_path = os.path.join(output_dir, filename)

            # Write the image content to a file
            with open(file_path, 'wb') as image_file:
                image_file.write(response.content)

            print(f"Downloaded {title} from {source} to {file_path}")

        except requests.RequestException as e:
            print(f"Failed to download {title} from {source}: {e}")

        except Exception as e:
            print(f"An unexpected error occurred while processing {title} from {source}: {e}")
