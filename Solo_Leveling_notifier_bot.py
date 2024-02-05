import time

import requests
from bs4 import BeautifulSoup
import re

initial_number = 5


def check_for_episode():
  print("Seaching for episodes...")
  global initial_number
  print("")
  response = requests.get("https://aniwatch.to/solo-leveling-18718")
  #   print(response.text)
  # Check if the request was successful (status code 200)

  soup = BeautifulSoup(response.text, 'html.parser')

  # Find the div with the specified class
  div_with_number = soup.find('div', class_='tick-item tick-sub')

  if div_with_number:
    # Extract the number from the div's text
    extracted_number = div_with_number.text.strip().split()[-1]
    print("Extracted number:", extracted_number)

    if int(extracted_number) > initial_number:
      initial_number += 1
      notify_user()
  else:
    print("No matching div found in the HTML string.")


def notify_user():
  webhook = "https://discord.com/api/webhooks/1204025314288730142/UN5U6jTClydUztegrhwImgFdKNGI0gmbubHThOkBi5r_AYyb8CX6PhpScnKTdkBVak5Z"

  message_content = "NEW Solo Leveling Episode: https://aniwatch.to/watch/solo-leveling-18718"
  # Create a dictionary with the message payload
  payload = {'content': message_content}

  # Send a POST request to the Discord webhook
  response = requests.post(webhook, json=payload)


while True:
  check_for_episode()
  time.sleep(60)
