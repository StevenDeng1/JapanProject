from selenium import webdriver
from selenium.webdriver.common.by import By
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

    accept_cookie = driver.find_element(By.XPATH, '/html/body/div[3]/button[1]')
    accept_cookie.click()

    # Fill in the parameters
    g_sec_choice = driver.find_element(By.XPATH, '//*[@id="div_id_GSm"]/fieldset/div[1]/label')
    g_sec_choice.click()

    substrate_choice = Select(driver.find_element(By.ID, 'id_s'))
    #substrate_choice.select_by_value()
    substrate_choice.select_by_value("A4_HUMAN")

    default_smd_input = driver.find_element(By.ID, "smdexample")
    default_smd_input.click()

    mutation = driver.find_element(By.ID, "id_chain_b")
    mutation.send_keys("K380P")

    time.sleep(2)

    start_md_button = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[6]/div/input[1]')
    start_md_button.click()

    # Wait for the simulation to finish
    time.sleep(3)

    job_description = driver.find_element(By.ID, 'id_description')
    job_description.send_keys('test job')

    user_email = driver.find_element(By.ID, 'id_user_email')
    user_email.send_keys('stdeng21@gmail.com')

    start_md_button_2 = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[19]/div/input')
    #start_md_button_2.click()
    # Close the browser

    time.sleep(20)

    driver.quit()


contact_gs_smd()
