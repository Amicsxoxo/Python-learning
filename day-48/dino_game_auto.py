import time
from PIL import Image
import io
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser and open the game
driver = webdriver.Chrome()
driver.get("chrome://dino") # Note: You may need an internet-disconnected tab or a clone site

print("Game loading... Ready your test.")
time.sleep(3) 

# Locate the game canvas
game_canvas = driver.find_element(By.CLASS_NAME, "runner-canvas")

# Define a detection point relative to the canvas
# Adjust these coordinates based on your screen resolution
pixel_x = 150  # Distance in front of the Dino
pixel_y = 120  # Height of the obstacle scan line

while True:
    # 1. Capture the canvas screenshot in memory
    canvas_png = game_canvas.screenshot_as_png
    image = Image.open(io.BytesIO(canvas_png)).convert("RGB")
    
    # 2. Get the color of the target pixel
    pixel_color = image.getpixel((pixel_x, pixel_y))
    
    # 3. Detect changes (e.g., standard background is light gray/white)
    # If the pixel is dark, an obstacle or night mode transition is detected
    if pixel_color[0] < 100:  
        print(f"Color Change Detected! Triggering Action. RGB: {pixel_color}")
        
        # Example Action: Make the dino jump
        # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)
        
    time.sleep(0.01) # Short delay to prevent extreme CPU usage
