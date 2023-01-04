from Utils import general_information

SCORES_FILE_NAME, BAD_RETURN_CODE = general_information()


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        file = open(SCORES_FILE_NAME, "r")
        the_score = file.read()
        new_points = points_of_winning + int(the_score)
        file = open(SCORES_FILE_NAME, "w")
        file.write(str(new_points))
        print(f"your score is {the_score}")
        file.close()
    except:
        print("Created a new score file")
        file = open(SCORES_FILE_NAME, "w")
        file.write(str(points_of_winning))
        file.close()



#
# file = open(SCORES_FILE_NAME, "r")
# print(file.read())
# file.close()