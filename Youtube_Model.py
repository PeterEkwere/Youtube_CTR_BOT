#!/usr/bin/python3
"""
    This Module Contains the entry point for the Youtube Bot
    Author: Peter Ekwere
"""
#import selenium
import time
#from selenium import webdriver
import concurrent.futures
import csv
from csv import reader
import json
from login_gmail_selenium.util.profiles.google_profile import GoogleProfile
from login_gmail_selenium.util.profiles.profile import Profile
from login_gmail_selenium.util.helper import enter_text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import multiprocessing as mp
import time
import random
from threading import Thread
from itertools import cycle, repeat
import random
from selenium_stealth import stealth
from time import sleep
from urllib.parse import urlparse, parse_qs, unquote
import re

# Add some random delays to mimic human behavior
def random_delay():
    time.sleep(random.uniform(1, 3))

#driver = None
            
                    
class Youtube:
    """ The Youtube class will handle every method regarding Youtube
    """

    nigerian_websites = [
        'nairaland.com',
        'jumia.com.ng',
        'konga.com',
        'guardian.ng',
        'vanguardngr.com',
        'punchng.com',
        'dailypost.ng',
        'thisdaylive.com',
        'premiumtimesng.com',
        'bbc.com/pidgin',
        'pulse.ng',
        'thenationonlineng.net',
        'channelstv.com',
        'techpoint.ng',
        'allafrica.com/nigeria',
        'nigeriabusinessinfo.com',
        'ng.trustpilot.com',
        'myjobmag.com',
        'jobberman.com',
        'hotels.ng',
        'legit.ng',
        'ng.indeed.com',
        'naij.com',
        'bellanaija.com',
        "lindaikejisblog.com",
        "bellanaija.com",
        "sisiyemmie.com",
        "ogbongeblog.com",
        "9jafoodie.com",
        "naijanews.com",
        "mcebiscoo.com",
        "notjustok.com",
        "gistlover.com",
        "thenewsguru.com",
        "creebhills.com",
        "mpmania.com",
        "akelicious.net",
        "vanguardngr.com",
        "wothappen.com",
        "dailyreportng.com",
        "naijabulletin",
        "9newsng.com",
        "jadore-fashion.com",
        "newsonlineng.com",
        "amebo9ja.com",
        "legit9ja.com",
        "newsblenda.com",
        "africanentertainment.com",
        "naijanowell.com",
        "mathewtegha.com",
        "wothappen.com",
        "cybernaira.com",
        "vegannigerian.com",
        "goldennewsng.com",
        'ebay.com',
    'alibaba.com',
    'aliexpress.com',
    'walmart.com',
    'target.com',
    'bestbuy.com',
    'costco.com',
    'homedepot.com',
    'lowes.com',
    'macys.com',
    'nordstrom.com',
    'zappos.com',
    'etsy.com',
    'shopify.com',
    'wayfair.com',
    'overstock.com',
    'newegg.com',
    'tigerdirect.com',
    'bhphotovideo.com',
    'adorama.com',
    
    # News & Media
    'cnn.com',
    'bbc.com',
    'foxnews.com',
    'nytimes.com',
    'washingtonpost.com',
    'theguardian.com',
    'reuters.com',
    'ap.org',
    'bloomberg.com',
    'wsj.com',
    'usatoday.com',
    'abc.go.com',
    'nbc.com',
    'cbs.com',
    'espn.com',
    'skysports.com',
    'goal.com',
    'bleacherreport.com',
    'tmz.com',
    'people.com',
    
    # Entertainment & Streaming
    'hulu.com',
    'disneyplus.com',
    'primevideo.com',
    'hbo.com',
    'paramount.com',
    'peacocktv.com',
    'crunchyroll.com',
    'funimation.com',
    'twitch.tv',
    'vimeo.com',
    'dailymotion.com',
    'imdb.com',
    'rottentomatoes.com',
    'metacritic.com',
    'gamespot.com',
    'ign.com',
    'polygon.com',
    'kotaku.com',
    'techcrunch.com',
    'theverge.com',
    
    # Education & Learning
    'wikipedia.org',
    'coursera.org',
    'edx.org',
    'udemy.com',
    'khanacademy.org',
    'skillshare.com',
    'pluralsight.com',
    'lynda.com',
    'masterclass.com',
    'duolingo.com',
    'babbel.com',
    'rosettastone.com',
    'brilliant.org',
    'codecademy.com',
    'freecodecamp.org',
    'w3schools.com',
    'stackoverflow.com',
    'github.com',
    'gitlab.com',
    'bitbucket.org',
    
    # Travel & Hospitality
    'booking.com',
    'expedia.com',
    'hotels.com',
    'trivago.com',
    'kayak.com',
    'priceline.com',
    'orbitz.com',
    'airbnb.com',
    'vrbo.com',
    'tripadvisor.com',
    'skyscanner.com',
    'momondo.com',
    'agoda.com',
    'travelocity.com',
    'cheaptickets.com',
    'hipmunk.com',
    'hotwire.com',
    'lastminute.com',
    'opodo.com',
    'tui.com',
    
    # Finance & Banking
    'paypal.com',
    'chase.com',
    'bankofamerica.com',
    'wellsfargo.com',
    'citibank.com',
    'americanexpress.com',
    'discover.com',
    'capitalone.com',
    'usbank.com',
    'pnc.com',
    'ally.com',
    'schwab.com',
    'fidelity.com',
    'vanguard.com',
    'etrade.com',
    'robinhood.com',
    'coinbase.com',
    'binance.com',
    'kraken.com',
    'gemini.com',
    
    # Health & Fitness
    'webmd.com',
    'mayoclinic.org',
    'healthline.com',
    'medicinenet.com',
    'drugs.com',
    'nih.gov',
    'cdc.gov',
    'who.int',
    'myfitnesspal.com',
    'fitbit.com',
    'nike.com',
    'adidas.com',
    'underarmour.com',
    'lululemon.com',
    'peloton.com',
    'classpass.com',
    'mindbodyonline.com',
    'headspace.com',
    'calm.com',
    'meditation.com',
    
    # Food & Dining
    'ubereats.com',
    'doordash.com',
    'grubhub.com',
    'postmates.com',
    'seamless.com',
    'yelp.com',
    'zomato.com',
    'opentable.com',
    'allrecipes.com',
    'foodnetwork.com',
    'epicurious.com',
    'bonappetit.com',
    'delish.com',
    'tasty.co',
    'hellofresh.com',
    'blueapron.com',
    'mealpal.com',
    'instacart.com',
    'peapod.com',
    'freshdirect.com',
    
    # Automotive
    'cars.com',
    'autotrader.com',
    'edmunds.com',
    'kbb.com',
    'carmax.com',
    'cargurus.com',
    'carfax.com',
    'vroom.com',
    'carvana.com',
    'tesla.com',
    'ford.com',
    'gm.com',
    'toyota.com',
    'honda.com',
    'nissan.com',
    'bmw.com',
    'mercedes-benz.com',
    'audi.com',
    'volkswagen.com',
    'hyundai.com',
    
    # Real Estate
    'zillow.com',
    'realtor.com',
    'redfin.com',
    'trulia.com',
    'apartments.com',
    'rent.com',
    'padmapper.com',
    'hotpads.com',
    'rentals.com',
    'forrent.com',
    'realpage.com',
    'loopnet.com',
    'crexi.com',
    'showcase.com',
    'mls.com',
    'century21.com',
    'coldwellbanker.com',
    'remax.com',
    'kw.com',
    'compass.com',
    
    # Job & Career
    'indeed.com',
    'glassdoor.com',
    'monster.com',
    'careerbuilder.com',
    'ziprecruiter.com',
    'simplyhired.com',
    'dice.com',
    'flexjobs.com',
    'upwork.com',
    'freelancer.com',
    'fiverr.com',
    '99designs.com',
    'toptal.com',
    'guru.com',
    'peopleperhour.com',
    'workana.com',
    'contra.com',
    'angellist.com',
    'crunchbase.com',
    'pitchbook.com',
    
    # Fashion & Beauty
    'zara.com',
    'hm.com',
    'uniqlo.com',
    'gap.com',
    'oldnavy.com',
    'bananarepublic.com',
    'jcrew.com',
    'anthropologie.com',
    'urbanoutfitters.com',
    'freepeople.com',
    'forever21.com',
    'fashionnova.com',
    'boohoo.com',
    'asos.com',
    'net-a-porter.com',
    'ssense.com',
    'farfetch.com',
    'mytheresa.com',
    'sephora.com',
    'ulta.com',
    
    # Sports & Recreation
    'mlb.com',
    'nfl.com',
    'nba.com',
    'nhl.com',
    'fifa.com',
    'uefa.com',
    'premierleague.com',
    'laliga.com',
    'bundesliga.com',
    'seriea.com',
    'olympics.com',
    'usopen.org',
    'wimbledon.com',
    'masters.com',
    'pgatour.com',
    'formula1.com',
    'nascar.com',
    'ufc.com',
    'wwe.com',
    'espnfc.com',
    
    # Government & Public Services
    'irs.gov',
    'ssa.gov',
    'usps.com',
    'dmv.org',
    'whitehouse.gov',
    'congress.gov',
    'senate.gov',
    'house.gov',
    'supremecourt.gov',
    'fbi.gov',
    'cia.gov',
    'nasa.gov',
    'noaa.gov',
    'weather.gov',
    'sec.gov',
    'ftc.gov',
    'fcc.gov',
    'dol.gov',
    'hhs.gov',
    'epa.gov',

    
    # European Sites
    'bbc.co.uk',
    'dailymail.co.uk',
    'theguardian.co.uk',
    'telegraph.co.uk',
    'independent.co.uk',
    'mirror.co.uk',
    'sky.com',
    'itv.com',
    'channel4.com',
    'amazon.co.uk',
    'argos.co.uk',
    'johnlewis.com',
    'tesco.com',
    'sainsburys.co.uk',
    'asda.com',
    'morrisons.com',
    'currys.co.uk',
    'pcworld.co.uk',
    'rightmove.co.uk',
    'zoopla.co.uk',
    ]



    GOOGLE_SEARCH_XPATH = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea"

    def pick_random_websites(self, websites):
        num_pick = random.randint(2, 3)
        if num_pick > len(websites):
            raise ValueError("num_pick must be less than or equal to the number of websites.")
        return random.sample(websites, num_pick)
        
    
    def launch_profile(self, email, password, backup_email):
        if email != "" and password != "":
            profile = GoogleProfile(email, password, backup_email)
            driver = profile.retrieve_driver()
            profile.start()
        else:
            raise(f"Error: No Email or Password was Passed for {email} with password: {password}")
        return driver


    def extract_video_id(self, url):
        """Extracts YouTube video ID from various URL formats including Shorts"""
        if not url:
            return None
            
        # Handle URL encoding
        decoded_url = unquote(url)
        
        # Regular expression pattern for YouTube video IDs
        patterns = [
            r"youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})",  # Standard watch URL
            r"youtu\.be/([a-zA-Z0-9_-]{11})",               # Short URL
            r"youtube\.com/embed/([a-zA-Z0-9_-]{11})",      # Embed URL
            r"youtube\.com/shorts/([a-zA-Z0-9_-]{11})",     # Shorts URL
            r"youtube\.com/live/([a-zA-Z0-9_-]{11})",       # Live stream URL
            r"v=([a-zA-Z0-9_-]{11})",                       # Fallback for v parameter
            r"/([a-zA-Z0-9_-]{11})"                         # Fallback for 11-character ID
        ]
        
        for pattern in patterns:
            match = re.search(pattern, decoded_url)
            if match:
                return match.group(1)
                
        # Parse URL and extract video ID as fallback
        try:
            parsed = urlparse(decoded_url)
            if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
                # Handle shorts URLs
                if parsed.path.startswith('/shorts/'):
                    return parsed.path.split('/')[2]
                
                # Handle standard watch URLs
                if parsed.path == '/watch' and 'v' in parse_qs(parsed.query):
                    return parse_qs(parsed.query)['v'][0]
                
                # Handle embed URLs
                if parsed.path.startswith('/embed/'):
                    return parsed.path.split('/')[2]
                
                # Handle youtu.be short URLs
                if parsed.netloc == 'youtu.be':
                    return parsed.path[1:]
        except:
            pass
            
        return None


    def scroll(self, driver, target_element=None):
        """Enhanced human-like scrolling with realistic pauses and momentum"""
        script = """
        let callback = arguments[arguments.length - 1];
        let targetElement = arguments.length > 1 ? arguments[0] : null;
        let currentPos = window.pageYOffset;
        let totalHeight = document.body.scrollHeight || document.documentElement.scrollHeight;
        
        // Longer scroll duration (5-25 seconds) for more natural reading pace
        const scrollDuration = (5 + Math.random() * 20) * 1000;
        
        // Random direction: 1 for down, -1 for up
        const scrollDirection = Math.random() > 0.5 ? 1 : -1;
        
        // Calculate scroll distance based on direction
        let scrollDistance;
        if (scrollDirection === 1) {
            // Scrolling down (shorter distances more common)
            scrollDistance = Math.min(
                window.innerHeight * (0.5 + Math.random() * 2.5), 
                totalHeight - currentPos
            );
        } else {
            // Scrolling up (typically shorter distances)
            scrollDistance = Math.min(
                window.innerHeight * (0.3 + Math.random() * 1.7), 
                currentPos
            );
        }
        
        // Handle target element safely
        let targetY = currentPos + (scrollDirection * scrollDistance);
        if (targetElement && typeof targetElement.getBoundingClientRect === 'function') {
            const rect = targetElement.getBoundingClientRect();
            targetY = Math.max(0, rect.top + currentPos - window.innerHeight/3);
        }
        
        // Ensure target is within page bounds
        targetY = Math.max(0, Math.min(targetY, totalHeight));
        
        // Physics parameters for natural movement
        let velocity = 0;
        const friction = 0.92;  // Increased friction for slower movement
        const acceleration = 0.6;  // Reduced acceleration
        let lastTime = performance.now();
        const startTime = performance.now();
        
        // Track reading pauses
        let pauseCount = 0;
        const maxPauses = 2 + Math.floor(Math.random() * 4);  // 2-5 pauses
        
        function smoothScroll() {
            const now = performance.now();
            const deltaTime = Math.min(50, now - lastTime);  // More lenient timing
            const elapsed = now - startTime;
            lastTime = now;
            
            // Random reading pauses during scroll (more frequent)
            if (pauseCount < maxPauses && Math.random() < 0.15 && elapsed > 2000) {
                pauseCount++;
                // Longer pauses (1.5-6 seconds)
                const readingPause = (1500 + Math.random() * 4500);
                setTimeout(smoothScroll, readingPause);
                return;
            }
            
            // Final pause after scrolling completes
            if (elapsed > scrollDuration) {
                // Longer final reading pause (3-12 seconds)
                const readingPause = (3000 + Math.random() * 9000);
                setTimeout(() => callback(), readingPause);
                return;
            }
            
            // Calculate distance to target
            const distance = targetY - currentPos;
            const direction = Math.sign(distance);
            const absDistance = Math.abs(distance);
            
            // Natural stopping condition
            if (absDistance < 5) {
                // Extended final pause (3-10 seconds)
                const readingPause = (3000 + Math.random() * 7000);
                setTimeout(() => callback(), readingPause);
                return;
            }
            
            // Dynamic acceleration with slower buildup
            const timeProgress = elapsed / scrollDuration;
            const easingFactor = 1 - Math.pow(1 - timeProgress, 3);  // Cubic easing
            const dynamicAccel = acceleration * Math.min(1, absDistance / 500) * easingFactor;
            
            // Apply momentum with human-like variability
            velocity = (velocity * friction) + (direction * dynamicAccel * deltaTime);
            
            // Add natural jitter (10-30% velocity variation)
            velocity *= (0.8 + Math.random() * 0.4);
            
            currentPos += velocity;
            currentPos = Math.max(0, Math.min(currentPos, totalHeight));
            window.scrollTo(0, Math.round(currentPos));
            
            // Human-like behavior patterns
            const rand = Math.random();
            if (rand < 0.07) {  // 7% chance of micro-pause
                // Longer micro-pauses (300-1200ms)
                setTimeout(smoothScroll, 300 + Math.random() * 900);
            } else if (rand < 0.13) {  // 6% chance of hesitation
                velocity *= (0.3 + Math.random() * 0.3);  // Slow down more
                // Longer hesitation delays (400-1500ms)
                setTimeout(smoothScroll, 400 + Math.random() * 1100);
            } else if (rand < 0.16) {  // 3% chance of backtrack
                velocity = -velocity * (0.4 + Math.random() * 0.3);  // Stronger backtrack
                // Longer backtrack pauses (500-1800ms)
                setTimeout(smoothScroll, 500 + Math.random() * 1300);
            } else {
                // Natural scroll with variable frame timing
                setTimeout(smoothScroll, 30 + Math.random() * 70);
            }
        }
        
        // Longer initial hesitation (1-3 seconds)
        setTimeout(smoothScroll, 1000 + Math.random() * 2000);
        """
        
        # Execute with or without target element
        try:
            if target_element:
                driver.execute_async_script(script, target_element)
            else:
                driver.execute_async_script(script)
        except JavascriptException as e:
            print(f"Scroll error: {str(e)}")


    def find_correct_link(self, driver, website, results):
        """
        # This function takes the website we are searching for and the list of search results,
        # and finds the correct link for the website among the results.
        """
        target_domain = website.replace("www.", "").strip().lower()

        found_match = False
        for i, result in enumerate(results[:10], 1):
            try:
                url = result.get_attribute("href")
                if not url:
                    continue

                selector = driver.execute_script("""
                                    function getSelector(el) {
                                        if (!el) return '';
                                        const path = [];
                                        while (el && el.nodeType === Node.ELEMENT_NODE) {
                                            let selector = el.nodeName.toLowerCase();
                                            
                                            if (el.id) {
                                                selector += `#${el.id}`;
                                                path.unshift(selector);
                                                break;
                                            }
                                            else if (el.name) {
                                                selector += `[name="${el.name}"]`;
                                                path.unshift(selector);
                                                break;
                                            }
                                            else if (el.title) {
                                                selector += `[title="${el.title}"]`;
                                                path.unshift(selector);
                                                break;
                                            }
                                            else if (el.ariaLabel) {
                                                selector += `[aria-label="${el.ariaLabel}"]`;
                                                path.unshift(selector);
                                                break;
                                            }
                                            else {
                                                let sib = el, nth = 1;
                                                while (sib = sib.previousElementSibling) {
                                                    if (sib.nodeName.toLowerCase() === selector) nth++;
                                                }
                                                if (nth !== 1) selector += `:nth-of-type(${nth})`;
                                                path.unshift(selector);
                                            }
                                            el = el.parentNode;
                                        }
                                        return path.join(' > ');
                                    }
                                    return getSelector(arguments[0]);
                                """, result)
                    
                # Parse URL to get domain
                parsed = urlparse(url)
                result_domain = parsed.netloc.replace("www.", "").lower()
                
                # Check if domain matches exactly
                if result_domain == target_domain:
                    print(f"\nExact match found for {website}:")
                    print(f"URL: {url}")
                    print(f"Selector: {selector}")
                    found_match = True
                    break  # Stop after first exact match
            
            except Exception as e:
                print(f"Error processing result #{i}: {str(e)}")
                continue

        if not found_match:
            print(f"No exact match found for domain: {website}")

        return url, selector
    
    def warmup_accounts(self, email, password, backup_email):
        """
        Warms up accounts to evade bot detection with improved network resilience
        """
        random_websites = self.pick_random_websites(self.nigerian_websites)
        driver = self.launch_profile(email, password, backup_email)
        print("Warming up Google accounts - network-optimized version")
        
        # Navigate to Google with extended timeout
        driver.uc_open_with_tab("https://google.com/ncr")
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
        except TimeoutException:
            print("Google didn't load in 30s. Refreshing...")
            driver.refresh()
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )

        for i, website in enumerate(random_websites):
            print(f"{email} accessing {website} [{i+1}/{len(random_websites)}]")
            
            # SEARCH PHASE (with recovery)
            try:
                # Always use same search method
                search_success = enter_text(
                    driver, 
                    'q', 
                    website, 
                    button=True, 
                    by=By.NAME, 
                    timeout=25  # Extended timeout for slow networks
                )
                if not search_success:
                    print(f"Search failed for {website}. Skipping...")
                    continue
            except Exception as e:
                print(f"Critical search error: {str(e)}. Re-initializing Google...")
                driver.get("https://www.google.com")
                continue

            # RESULTS HANDLING
            try:
                # Wait for results with extended timeout
                WebDriverWait(driver, 25).until(
                    EC.visibility_of_element_located((By.ID, "search"))
                )
                
                # Get results with freshness check
                results = WebDriverWait(driver, 15).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[jsname="UWckNb"]'))
                )
                
                # Find target link
                url, selector = self.find_correct_link(driver, website, results)
                result = driver.find_element(By.CSS_SELECTOR, selector)

                # Scroll and click
                self.scroll(driver, result)
                result.click()
                
                # Verify site loaded
                WebDriverWait(driver, 30).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
                
                # Browse target site
                self.scroll(driver)
                wait_time = random.uniform(3, 7)
                time.sleep(wait_time)
                
            except Exception as e:
                print(f"Results processing failed: {str(e)}. Continuing...")
                driver.back()
                continue
            
            # RETURN TO GOOGLE (with verification)
            try:
                driver.back()
                # Wait for Google to reload
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )
                print(f"Returned to Google after {wait_time:.1f}s on site")
            except Exception as e:
                print(f"Return failed: {str(e)}. Reloading Google...")
                driver.get("https://www.google.com")
            
            # Randomized break between actions
            sleep_duration = random.uniform(2, 5)
            print(f"Cycle complete. Sleeping {sleep_duration:.1f}s...")
            time.sleep(sleep_duration)
        
        return driver



    def youtube_ctr(self, email, password, backup_email, video_keyword, video_url=None):
        """
        Perform YouTube CTR operations after account warmup
        :param driver: WebDriver instance from warmup_accounts
        :param video_keyword: Keyword to search on YouTube
        :param video_url: Optional specific video URL to target
        """
        driver = self.warmup_accounts(email, password, backup_email)
        try:
            # Step 1: Search for YouTube on Google
            youtube_text = random.choice(["Youtube.com", "youtube.com", "youTube.com", "yOutube.com"])
            search_box = driver.find_element(By.ID, "APjFqb")
            search_box.clear()
            enter_text(driver, '#APjFqb', youtube_text, button=True)
            
            # Step 2: Wait for official YouTube search result
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search"))
            )

            # Get all search result links
            results = driver.find_elements(By.CSS_SELECTOR, 'a[jsname="UWckNb"]')
            
            # find the  selector for the correct link for the webstite we searched
            url, selector = self.find_correct_link(driver, youtube_text, results)
            
            # Find the element again
            result = driver.find_element(By.CSS_SELECTOR, selector)

            # scroll to link position on the page
            self.scroll(driver, result)

            # click the link to simulate human interaction
            result.click()
            
            # Wait for YouTube to fully load
            WebDriverWait(driver, 30).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            print("YouTube page loaded successfully")
            
            # Step 3: Search on YouTube
            try:
                # Wait for YouTube search box to be visible (with extended timeout)
                WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search_query']"))
                )
                print("YouTube search box found")
                
                # Human-like typing in YouTube search
                search_success = enter_text(
                    driver, 
                    "input[name='search_query']", 
                    video_keyword, 
                    button=True,  # Press enter after typing
                    timeout=30
                )
                
                if not search_success:
                    print("YouTube search failed. Trying alternative method...")
                    # Fallback: Directly submit the form
                    search_box = driver.find_element(By.CSS_SELECTOR, "input[name='search_query']")
                    search_box.send_keys(Keys.ENTER)
                
                # Wait for search results to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
                )
                print("YouTube search results loaded")
                
                # Add random scrolling through results
                self.scroll(driver)
                time.sleep(random.uniform(0.5, 1.5))


                self.handle_youtube_search_results(driver, video_url)
                
            except Exception as e:
                print(f"Error during YouTube search: {str(e)}")
                # Take screenshot for debugging
                driver.save_screenshot("youtube_search_error.png")
                raise
            


            time.sleep(1000)
        except Exception as e:
            print(f"An error occurred in youtube_ctr: {e}")
            pass


    def handle_youtube_search_results(self, driver, target_video_url=None):
        """Refactored logic for interacting with YouTube search results"""
        try:
            print("Starting handle_youtube_search_results...")
            if not target_video_url:
                print("No target video URL provided. Skipping video search.")
                return

            print(f"Target video URL: {target_video_url}")
            target_video_id = self.extract_video_id(target_video_url)
            if not target_video_id:
                print(f"Invalid YouTube URL: {target_video_url}")
                return
            print(f"Extracted target video ID: {target_video_id}")

            found = False
            found_video = None
            scroll_attempts = 0
            max_scroll_attempts = 5
            video_elements = []

            # Try to find the target video, downplaying some videos each time
            while not found and scroll_attempts < max_scroll_attempts:
                print(f"Search attempt {scroll_attempts+1}/{max_scroll_attempts}")
                found, video_elements, found_video = self.find_target_video(driver, target_video_id)
                print(f"Found: {found}, Number of video elements: {len(video_elements)}")
                # Downplay some videos in the current view
                print("Downplaying some videos in current view...")
                self.downplay_videos(driver, video_elements)
                print("Done downplaying videos.")
                if found:
                    print("Target video found in search results.")
                    break
                print("Target video not found, scrolling to load more videos...")
                self.scroll_to_bottom(driver)
                scroll_attempts += 1
                time.sleep(random.uniform(2.0, 4.0))

            if not found:
                print(f"Target video not found after {max_scroll_attempts} scroll attempts. Scrolling to top and checking recently uploaded...")
                self.scroll_to_top(driver)
                self.check_recently_uploaded(driver)
                # Try to find the target video again after filtering
                found, video_elements, found_video = self.find_target_video(driver, target_video_id)
                print(f"After checking recently uploaded, found: {found}")

            if found and found_video is not None:
                print("Clicking on the found target video...")
                try:
                    self.scroll(driver, found_video)
                    time.sleep(random.uniform(1.0, 2.0))
                    print(f"About to click found video: displayed={found_video.is_displayed()}, enabled={found_video.is_enabled()}")
                    try:
                        found_video.click()
                        print("Clicked on target video using .click()")
                    except Exception as click_e:
                        print(f"Standard click failed: {click_e}. Trying JavaScript click...")
                        try:
                            driver.execute_script("arguments[0].click();", found_video)
                            print("Clicked on target video using JavaScript click.")
                        except Exception as js_click_e:
                            print(f"JavaScript click also failed: {js_click_e}")
                            raise js_click_e
                    time.sleep(random.uniform(1.5, 3.5))
                    print("Waiting for video to load...")
                    try:
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "video.html5-main-video"))
                        )
                        print("Video player loaded")
                    except Exception as e:
                        print("Video player did not load in time, trying to reload or skip...")
                    print("Video loaded. Ready for further actions.")
                except Exception as e:
                    print(f"Error clicking on found target video: {e}")
            else:
                print("Target video not found after all attempts.")
        except Exception as e:
            print(f"An error occurred in handle_youtube_search_results: {e}")
            # driver.save_screenshot("youtube_search_results_error.png")


    def downplay_videos(self, driver, video_elements):
        """
        Downplay a random number of videos between 1 and 3, skipping Shorts
        """
        long_video_elements = []
        try:
            num_videos_to_downplay = random.randint(1, 3)
            if len(video_elements) < num_videos_to_downplay:
                videos_to_downplay = video_elements
            else:
                for video in video_elements:
                    video_link_elem = video.find_element(By.CSS_SELECTOR, 'a#video-title')
                    video_link = video_link_elem.get_attribute('href')
                    if video_link and '/shorts/' in video_link:
                        print(f"Skipping Shorts video: {video_link}")
                        continue
                    else:
                        long_video_elements.append(video)


                videos_to_downplay = random.sample(long_video_elements, num_videos_to_downplay)
            for video in videos_to_downplay:
                try:
                    # Try to get the video link
                    video_link_elem = video.find_element(By.CSS_SELECTOR, 'a#video-title')
                    video_link = video_link_elem.get_attribute('href')
                    print(f"watching video: {video_link}")
                    # Scroll to video
                    self.scroll(driver, video)
                    print("Scrolling to video")
                    # Add human-like hesitation
                    time.sleep(random.uniform(1.5, 3.5))
                    # Click on video
                    print(f"About to click video element: displayed={video.is_displayed()}, enabled={video.is_enabled()}")
                    try:
                        video.click()
                        print("Clicked on video using .click()")
                    except Exception as click_e:
                        print(f"Standard click failed: {click_e}. Trying JavaScript click...")
                        try:
                            driver.execute_script("arguments[0].click();", video)
                            print("Clicked on video using JavaScript click.")
                        except Exception as js_click_e:
                            print(f"JavaScript click also failed: {js_click_e}")
                            raise js_click_e
                    time.sleep(random.uniform(1.5, 3.5))
                    print("Waiting for video to load...")
                    # Wait for the video player to appear (up to 20 seconds)
                    try:
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "video.html5-main-video"))
                        )
                        print("Video player loaded")
                    except Exception as e:
                        print("Video player did not load in time, trying to reload or skip...")
                        # Optionally: driver.refresh() or continue
                    print("Video loaded")
                    # Perform negative action
                    print("Performing negative action")
                    self.perform_negative_action(driver)
                    # Close tab or go back
                    self.go_back(driver)
                    print("Closed tab or went back")
                except Exception as e:
                    print(f"Error processing video in downplay_videos: {e}")
                    continue
        except Exception as e:
            print(f"Error in downplay_videos: {e}")
            pass


    def check_recently_uploaded(self, driver):
        """
        check if recently uploaded is available
        """
        # Click "Recently uploaded" filter
        try:
            # Wait for the filter bar to be visible
            # WebDriverWait(driver, 15).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR, "yt-chip-cloud-chip-renderer"))
            # )
            time.sleep(3)
            # Find all filter chips
            filters = driver.find_elements(By.CSS_SELECTOR, "yt-chip-cloud-chip-renderer")
            #print(f"Filters: {filters}")
            for filter_chip in filters:
                #print(f"Filter chip: {filter_chip}")
                try:
                    # Check if this is the "Recently uploaded" filter
                    chip_text = filter_chip.text.strip()
                    #print(f"Chip text: {chip_text}")
                    if "recently uploaded" in chip_text.lower():
                        #print("Found 'Recently uploaded' filter")
                        
                        # Scroll to filter
                        self.scroll(driver, filter_chip)
                        
                        # Add human-like hesitation
                        time.sleep(random.uniform(1.0, 2.5))
                        
                        # Click the filter
                        filter_chip.click()
                        # print("Clicked 'Recently uploaded' filter")
                        
                        # Wait for results to reload
                        WebDriverWait(driver, 15).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
                        )
                        time.sleep(random.uniform(2.0, 4.0))
                        
                except Exception as e:
                    print(f"Error checking filter: {str(e)}")
                    continue
        except Exception as e:
            print(f"Error checking filter: {str(e)}")


    def find_target_video(self, driver, target_video_id):
        """
        Find target video and return (found, video_elements)
        """
        found = False
        video_elements = driver.find_elements(
                By.CSS_SELECTOR, 'ytd-video-renderer:not([hidden])'
            )
        found_video = ""
        
        for video in video_elements:
            try:
                # Get video link
                video_link = video.find_element(
                    By.CSS_SELECTOR, 'a#video-title'
                ).get_attribute('href')
                
                current_video_id = self.extract_video_id(video_link)
                
                if current_video_id == target_video_id:
                    print(f"Found target video: {video_link}")
                    found = True
                    found_video = video
                    
                    # Scroll to video
                    # self.scroll(driver, video)
                    
                    # Add human-like hesitation
                    time.sleep(random.uniform(1.5, 3.5))
                    
                    # # Click on video
                    # video_link_element = video.find_element(
                    #     By.CSS_SELECTOR, 'a#video-title'
                    # )
                    # video_link_element.click()
                    # print("Clicked on target video")
                    
                    # Break out of loops
                    break
            
            except Exception as e:
                # Skip if any element is stale or not found
                return False, video_elements
        
        return found, video_elements, video


    def scroll_to_top(self, driver):
        """
        Scroll to the top of the page
        """
        scroll_script = """
            // Human-like scrolling to top with variable speed
            const start = window.scrollY;
            const end = 0;
            const distance = start;  // Since we're going to top
            const duration = 1000 + Math.random() * 1000;  // 1-2 seconds
            const startTime = Date.now();
            
            function scrollStep() {
                const currentTime = Date.now();
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                
                // Ease-in-out curve for natural acceleration/deceleration
                const ease = progress < 0.5 
                    ? 2 * progress * progress 
                    : -1 + (4 - 2 * progress) * progress;
                    
                window.scrollTo(0, start - distance * ease);
                
                if (progress < 1) {
                    // Random delay between steps (human-like variation)
                    setTimeout(scrollStep, 20 + Math.random() * 40);
                }
            }
            scrollStep();
        """
        driver.execute_script(scroll_script)


    def scroll_to_bottom(self, driver):
        """
        Scroll to the bottom of the page
        """
        scroll_script = """
                    // Human-like scrolling with variable speed
                    const start = window.scrollY;
                    const end = document.documentElement.scrollHeight;
                    const distance = end - start;
                    const duration = 1500 + Math.random() * 1000;  // 1.5-2.5 seconds
                    const startTime = Date.now();
                    
                    function scrollStep() {
                        const currentTime = Date.now();
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        
                        // Ease-in-out curve for natural acceleration/deceleration
                        const ease = progress < 0.5 
                            ? 2 * progress * progress 
                            : -1 + (4 - 2 * progress) * progress;
                            
                        window.scrollTo(0, start + distance * ease);
                        
                        if (progress < 1) {
                            // Random delay between steps (human-like variation)
                            setTimeout(scrollStep, 30 + Math.random() * 50);
                        }
                    }
                    scrollStep();
                """
        driver.execute_script(scroll_script)



    def perform_negative_action(self, driver):
        """
        Perform 1-3 random negative interactions on competitor video, with human-like delays
        """
        actions = ["dislike", "scroll_comments", "captions_on"]
        num_actions = random.randint(2, 3)
        chosen_actions = random.sample(actions, num_actions)
        print(f"Chosen actions: {chosen_actions}")
        for action in chosen_actions:
            time.sleep(random.uniform(1.0, 2.5))  # Human-like pause before action
            if action == "dislike":
                print("Performing dislike action")
                try:
                    print("Clicking dislike button")
                    dislike_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dislike this video']"))
                    )
                    time.sleep(random.uniform(0.5, 1.2))  # Pause before click
                    dislike_button.click()
                    print("Clicked dislike button")
                    time.sleep(random.uniform(0.7, 1.5))  # Pause after click
                except Exception as e:
                    print(f"Error clicking dislike button: {e}")
            elif action == "scroll_comments":
                print("Scrolling to comment section")
                try:
                    comment_section = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments"))
                    )
                    print("Comment section found")
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", comment_section)
                    print("Scrolled to comment section")
                    time.sleep(random.uniform(1.0, 2.0))
                except Exception as e:
                    print(f"Error scrolling to comment section: {e}")
            elif action == "captions_on":
                print("Clicking captions button")
                try:
                    captions_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-subtitles-button"))
                    )
                    time.sleep(random.uniform(0.5, 1.2))  # Pause before click
                    captions_button.click()
                    print("Toggled captions/subtitles")
                    time.sleep(random.uniform(0.7, 1.5))  # Pause after click
                except Exception as e:
                    print(f"Error toggling captions: {e}")

    def go_back(self, driver, search_keyword="Jordan ones"):
        """
        Go back to the search results page after negative action. If not on results, try to re-search the keyword.
        """
        try:
            print("Attempting to go back to search results...")
            driver.back()
            time.sleep(random.uniform(1.5, 3.0))
            # Check if we're back on the search results page
            for attempt in range(3):
                try:
                    # Look for the search results container
                    driver.find_element(By.CSS_SELECTOR, "#contents ytd-video-renderer")
                    print("Back on search results page.")
                    return
                except Exception:
                    print(f"Not on search results page, attempt {attempt+1}/3. Going back again...")
                    driver.back()
                    time.sleep(random.uniform(1.5, 3.0))
            # If still not on results, try to re-search if keyword is provided
            if search_keyword:
                print(f"Re-searching for keyword: {search_keyword}")
                try:
                    search_box = driver.find_element(By.CSS_SELECTOR, "input[name='search_query']")
                    search_box.clear()
                    for char in search_keyword:
                        search_box.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.15))
                    search_box.send_keys(Keys.ENTER)
                    time.sleep(random.uniform(2.0, 3.0))
                except Exception as e:
                    print(f"Error re-searching keyword: {e}")
        except Exception as e:
            print(f"Error navigating back: {e}")



    def positive_engagement_engine(self, driver):
        """
        Perform positive engagement actions on target video
        """
        # Pseudocode:
        # Phase 1: Watch min(60%, random(60%-80%)) of video
        # 
        # Random Positive Action 1:
        #   if random() < 0.85: click_like()
        #   if random() < 0.40: rewind_and_rewatch_segment()
        #   if random() < 0.30: subscribe_to_channel()
        #
        # Phase 2: Watch random(20%-40%) of remaining video
        #
        # Random Positive Action 2:
        #   if random() < 0.70: post_unique_comment()
        #   if random() < 0.25: save_to_watch_later()
        #   if random() < 0.15: turn_on_notifications()
        #
        # If <30s remaining: watch_to_end()
        pass

    def post_unique_comment(self, driver, comment=None):
        """
        Post a comment with human-like typing
        """
        # Pseudocode:
        # scroll_to_comments()
        # click_comment_box()
        # enter_text_with_typing(comment or generate_unique_comment())
        # random_delay()
        # click_post_button()
        pass
        
        
    
    
    # def like_comment(self, comment_url, email, password, backup_email):
    #     """ This is the method that will handle liking comments on youtube

    #     Args:
    #         comment_url (list): This is the links to the video where the comment exist
    #         email (str): This is a bot email
    #         password (str): This is a bot password
    #     """
    #     #global driver
    #     driver = self.warmup_accounts(email, password, backup_email)
    #     print("Finished Warming up Google Account")
        
    #     if comment_url:
    #         for url in comment_url:
    #             for attempt in range(2):  # Try up to 2 times before continuing
    #                 try:
    #                     #driver = self.launch_profile(email, password, backup_email)
    #                     print("Getting URL")
    #                     print(f"URL {attempt} TRY IS {url}")
    #                     driver.get(url)
    #                     # Opening YouTube and navigating to video
    #                     print("About to Sleep For 15 Seconds")
    #                     time.sleep(15)
    #                     # Navigating to comments section
    #                     print("Finished Sleeping for 15 seconds for youtube page to load")
    #                     comments_section = WebDriverWait(driver, 15).until(
    #                         EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer"))
    #                                                         #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments"))
    #                         )
    #                     # Scrolling down
    #                     print("Scrolling To comments Section")
    #                     #time.sleep(5)
    #                     driver.execute_script("arguments[0].scrollIntoView(true)", comments_section)                 
    #                     print("About to sleep for 3 Seconds")
    #                     time.sleep(3)
    #                     print("Finished sleeping for 3 Seconds Now Extracting First Comment")
                        
    #                     # Find the first comment
    #                     first_comment = comments_section.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-view-model/div[3]")

    #                     print("Extracting First like Button")
    #                     # Getting like button for comment
    #                     like_button = first_comment.find_element(By.ID, "like-button")
    #                     print("About to click like button")     
    #                     like_button.click()
    #                     print("Finished Clicking like Button")
                        
    #                     #time.sleep(5)  # Adjust timeout as needed
    #                     try:
    #                         popup = WebDriverWait(driver, 10).until(
    #                             EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div")) 
    #                                                         #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer"))
    #                                                         #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments"))
    #                         )
    #                         create_youtube_account_button = popup.find_element(By.ID,"create-channel-button")
    #                     except Exception as e:
    #                         popup = None
    #                         pass
    #                     if popup:
    #                         print(f"POPUP EXIST")
    #                         if create_youtube_account_button:
    #                             print(f"popup button found")
    #                             time.sleep(5)
    #                             # Click the "create-channel-button" within the popup
    #                             create_youtube_account_button.click()
    #                             print("POPUP Button Clicked about to sleep for 5 seconds")
    #                             time.sleep(3)
    #                             print("Finished sleeping Now About to refresh page ")
    #                             driver.refresh()
    #                             print("Finished refreshing now sleeping for 5 seconds ")
    #                             time.sleep(6)
    #                             print("Finished sleeping Now About to scroll to comment again")
    #                             driver.execute_script("arguments[0].scrollIntoView(true)", first_comment)
    #                             time.sleep(3)
    #                             print("Finished sleeping for 2 sec Now About to click like button again ")
    #                             like_button.click()
    #                             print("Finished Clicking like Button")
    #                     break  # Exit the loop if successful
    #                 except Exception as e:
    #                     print(f"Attempt {attempt+1} for url: {url}: Exception occurred -  with email {email}")
    #                     pass  # Retry on the next attempt
    #             else:  # If all attempts fail, silently continue
    #                 print(f"Failed to access url with email: {email} after 2 attempts.")



    #         # Close the browser
    #         #print("Sleeping For 5 Seconds")
    #         #time.sleep(5)
    #         print("Now Quiting after Finished Task")

    #         try:
    #             driver.close()
    #         except Exception as e:
    #             print(f"Error closing window: {e}")
    #         time.sleep(2)
    #         driver.quit()
    #     else:
    #         raise(f"Error: No Incorrect URL WAS PASSED: {comment_url}")
        
        
    
    def extract_urls(self, url_file):
        """
        Extracts a list of URLs from the specified file.

        Args:
            url_file (str): Path to the file containing URLs.

        Returns:
            list: A list of URLs extracted from the file.
        """
        with open('urls.json', 'r') as infile:
            urls = json.load(infile)
        
        urls_list = []
        for url in urls:
            try:
                url_parts = url.split("?")
                if len(url_parts) > 1:
                    link = url_parts[1]
                else:
                    raise (f"Error: Splitting url is {url} This Url Might Not be a valid Youtube Comment Link") 
                if link:
                    comment_link = f"https://www.youtube.com/watch?app=desktop&{link}"
                    urls_list.append(comment_link)
                else:
                    raise "Error with youtube link"
            except Exception as e:
                print(f"Error Extracting URL {e}")
        return urls_list
            

    def extract_accounts(self, account_file):
        """
        Extracts a list of email, password, and backup email tuples from the specified file.

        Args:
            account_file (str): Path to the file containing account information.

        Returns:
            list: A list of tuples containing (email, password, backup_email).
        """
        with open('accounts.json', 'r') as f:
            retrieved_email_data = json.load(f)
        return retrieved_email_data


    def process_account(self, account, urls):
        email = account.get("email", None)
        password = account.get("password", None)
        backup_email = account.get("backup_email", None)
        
        if email and password:
            try:
                print("Please Hold")
                #driver = self.warmup_accounts(email, password, backup_email)
                #print("Finished warming up accounts proceeding to like comments")
                #self.like_comment(urls, email, password, backup_email)
                self.youtube_ctr(email, password, backup_email, "jordan ones", video_url="https://youtube.com/shorts/0cSozOGYr8M?si=ua6GEKg7iud_WjRi")
            except Exception as e:
                print(e)



if __name__=="__main__":
    print("DO NOT RUN THIS DIRECTLY")
    pass
    