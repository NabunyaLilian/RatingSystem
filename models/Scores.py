import sys
import json
class Scores:

    initial_score = 0
    

    def rate_a_bootcamper(self, excellence, passion, integrity, collaboration):
        global initial_score

        excellence, passion, integrity, collaboration = 0, 0, 0, 0
        initial_score = excellence + passion + integrity + collaboration

        final_student_score = initial_score / 4

        print("This is the final score for the student", final_student_score)

    def view_scores(self):

        pass

    def edit_scores(self):
        pass