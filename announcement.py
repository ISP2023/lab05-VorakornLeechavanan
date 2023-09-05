"""Exercise in externalizing data using python-decouple.

   Externalize at least 5 things that represent "data" likely to change.
   You may externalize more than 5 things is fine.

   Put the actual values in a file named .env 
   Use python-decouple to get the values from .env.
"""
from typing import List
from decouple import config

# .env
IS_ONLINE = config("IS_ONLINE")
MEETING_URL = config("MEETING_URL")
LOCATION = config("LOCATION")
MEETING_TIME = config("MEETING_TIME")
TOPICS = config("TOPICS")


def announce_class(is_online: bool):
    """Announce whether class is online, and print the location or Meet URL.
    """
    if is_online:
        print("Class will meet online.")
        print("The Google Meet URL is https://meet.google.com/nxg-ukhc-oow")
    else:
        print("Class will meet at Kasetsart University, CPE Room 202.")
    # The meeting time is the same in both cases
    print("Meeting time is 13:00-16:00\n")
    

def describe_topics(topics: List[str]):
    """Print the topics that will be covered in class."""
    print("Topics we will discuss are:")
    for topic in topics:
        print(" -", topic)


if __name__ == '__main__':
    # Does class meet online (True) or at KU (False)?
    announce_class(IS_ONLINE)
    # print a list of today's topics
    describe_topics(TOPICS)
