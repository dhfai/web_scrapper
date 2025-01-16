# import requests
# from bs4 import BeautifulSoup
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
# model = genai.GenerativeModel("gemini-1.5-flash")

# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     text = soup.get_text()


#     prompt = {
#         "task": "job_listing_extraction",
#         "language": "indonesian",
#         "data": {
#             "text": text,
#             "website_url": url
#         },
#         "parameters": {
#             "entities": ["judul_pekerjaan", "deskripsi_pekerjaan", "tag_keahlian", "budget", "jangka_waktu", "persyaratan_pelamar"]
#         }
#     }

#     ai_response = model.generate_content(str(prompt))

#     print(ai_response.text)
#     return ai_response.text

# url = 'https://projects.co.id/public/browse_projects/listing'
# scraped_data = scrape_website(url)






