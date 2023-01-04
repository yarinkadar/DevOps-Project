import os


def general_information():
    SCORES_FILE_NAME = "scores.txt"
    BAD_RETURN_CODE = 69
    return SCORES_FILE_NAME, BAD_RETURN_CODE

def screen_cleaner():
    os.system('cls')

