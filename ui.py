from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text="Some text",
                                                   width=280,
                                                   fill="black",
                                                   font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        self.button_true = Button()
        self.true_image = PhotoImage(file="images/true.png")
        self.button_true.config(highlightthickness=0, image=self.true_image, command=self.true_answer)
        self.button_true.grid(column=0, row=2, pady=20, padx=20)

        self.button_false = Button()
        self.false_image = PhotoImage(file="images/false.png")
        self.button_false.config(highlightthickness=0, image=self.false_image, command=self.false_answer)
        self.button_false.grid(column=1, row=2, pady=20, padx=20)

        self.label_score = Label()
        self.label_score.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white', font=("Arial", 14))
        self.label_score.grid(column=1, row=0, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.label_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=f"Quiz is over!\nYour final score is {self.quiz.score} of 10")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
