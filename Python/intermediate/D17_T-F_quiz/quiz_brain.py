class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list
    
    def next_question(self):
        # while not all questions have been asked
        while self.question_num < len(self.question_list):
            response = input(f"Question {self.question_num + 1}: {self.question_list[self.question_num].question} (True/False): ").capitalize()
            
            # giving feedback & adding point if correct
            if response == self.question_list[self.question_num].answer:
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect.\n")
            
            # increment for next loop
            self.question_num += 1
            
            # the tutorial used a beginner's alternative to recursion,
            # but it was needlessly convoluted
            self.next_question()