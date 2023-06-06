from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def contact_gs_smd():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Open the GS-SMD website
    driver.get("https://gs-smd.biomodellab.eu/md/")

    # Wait for the page to load
    time.sleep(2)

    # Fill in the parameters
    input_box = driver.find_element_by_id("id_prot_pdb_code")
    input_box.send_keys("protein_code")

    input_box = driver.find_element_by_id("id_box_shape")
    input_box.send_keys("box_shape")

    select_box = Select(driver.find_element_by_id("id_box_size"))
    select_box.select_by_visible_text("box_size")

    # Submit the form
    submit_button = driver.find_element_by_css_selector("input[type='submit']")
    submit_button.click()

    # Wait for the simulation to finish
    time.sleep(10)

    # Close the browser
    driver.quit()
