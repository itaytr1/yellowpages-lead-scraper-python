import requests
import json

# 👉 Get your API key here: [INSERT YOUR RAPIDAPI LINK HERE]
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY_HERE"

# The endpoint for the Premium Local Business Leads API
url = "https://premium-local-business-leads.p.rapidapi.com/api/v1/leads"

# Define your target audience
querystring = {
    "niche": "plumber",
    "location": "dallas tx",
    "limit": "20",       # Pull 20 leads
    "page": "1",         # Start on page 1
    "sort_by": "rating"  # Get the highest rated businesses first
}

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "premium-local-business-leads.p.rapidapi.com"
}

print(f"Fetching leads for {querystring['niche']}s in {querystring['location']}...")

try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status() # Check for HTTP errors
    
    data = response.json()
    
    print(f"\n✅ Success! Extracted {data['metadata']['results_returned']} businesses.")
    print("-" * 40)
    
    # Print the top lead as an example
    first_lead = data['data'][0]
    print(f"🏆 Top Lead: {first_lead['business_name']}")
    print(f"📞 Phone: {first_lead['phone']}")
    print(f"🌐 Website: {first_lead['website']}")
    print(f"⭐ Rating: {first_lead['trust_signals']['star_rating']} ({first_lead['trust_signals']['review_count']} reviews)")
    print(f"🏷️ Categories: {', '.join(first_lead['categories'])}")
    print("-" * 40)
    
    # Uncomment the line below to see the full raw JSON payload
    # print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"❌ Error connecting to the API: {e}")
