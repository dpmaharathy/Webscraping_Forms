import os
import serpapi
import csv
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

endOfPage = False
pageNr = 0

# Open the CSV file once before the loop starts
with open('Insurance_claim_forms.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Source', 'High Resolution Image'])

    while not endOfPage:
        results = client.search({
            'engine': 'google_images',
            'tbm': 'isch',
            'q': 'Insurance Claim Form',
            'gl': 'us',
            'ijn': pageNr,
            'tbs': 'isz:l',
        })
        
        if results['search_information']['image_results_state'] == 'Fully empty':
            endOfPage = True
            print('End of page')
            break

        for result in results['images_results']:
            # Extract the high-resolution image URL
            high_res_image = result.get('original', '')
            csv_writer.writerow([result['title'], result['source'], high_res_image])
        
        pageNr += 1
        # print('First result: ', results['images_results'][0]['title'])
