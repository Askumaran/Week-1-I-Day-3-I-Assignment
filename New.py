from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright automation script...")
print(f"Script started at: {datetime.now()}")

#Daily Cricket Score Update Bot
#chromium --> Cricket Score site --> Extract the report --> Screenshot --> final text file
with sync_playwright() as p:
    print("Launching the Chromium browser...")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Navigating to the Cribuzz website...")
    page.goto("https://www.cricbuzz.com/live-cricket-scores/171070/ind-vs-pak-gold-medal-match-asian-games-2026")
    page.wait_for_load_state("networkidle")    
    page.screenshot(path="Cricket Score.png")

    print("Extracting the Cricket Score...")
    cricket_score = page.inner_text("div.current-score-card")
    print(f"Current Cricket Score Update: {cricket_score}")

    print("Saving the Cricket Score Update to a text file...")
    with open("Cricket Score Update.txt", "w") as file:
        file.write(f"Cricket Score Update for IND vs PAK today {datetime.now()}:\n")
    file.write(cricket_score)
    print("Closing the browser...")
    browser.close()
    print(f"Script completed at: {datetime.now()}")