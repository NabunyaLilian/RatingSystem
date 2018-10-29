import sys
import json
class Scores:

    initial_score = 0
    epic_scores=[{}]
    def rate_a_bootcamper(self, excellence, passion, integrity, collaboration):
        global initial_score
        global epic_scores
        epic_scores=[{}]
        initial_score = excellence + passion + integrity + collaboration

        final_student_score = initial_score / 4
        epic_scores.append([{
            "excellence" :"excellence",
            "passion": "passion",
            "integrity":"integrity",
            "collaboration":"collaboration"
        }])
        print("This is the final score for the student", final_student_score)

    def view_scores(self):        
       return epic_scores
