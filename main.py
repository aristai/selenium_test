from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify

@browser
def scrape_heading_task(driver: Driver, data):
    # Visit the Omkar Cloud website
    response = driver.get("https://mediaspace.illinois.edu/createdby/eyJpdiI6IlV3Q3NSWjZhSzlHNXRJTnhCYzdYRkE9PSIsInZhbHVlIjoiNk12Sk9MWkhCQmdKZm9lK29XcWNyUT09IiwibWFjIjoiY2U5ZWU0ZWY3MDM5NDg5YTk2YTIzYTNhOWRlOTM0YjhhYjRlMmQ4MDJjNWMyMjFjY2Y3YmZlOGI5ZTljZGI1OCJ9")
    
    import time
    time.sleep(10)
    # Retrieve the heading element's text
    heading = driver.get_text("h1")
    soup = soupify(response)
    with open('./scrape_heading_task.html', 'w') as f:
        f.write(soup.prettify())

    # Save the data as a JSON file in output/scrape_heading_task.json
    return {
        "heading": heading
    }
     
# Initiate the web scraping task
scrape_heading_task()