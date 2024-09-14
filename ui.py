from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            font=("Courier", 20, "bold"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=image_true,highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)

        image_false = PhotoImage(file="images/false.png")
        self.button_true = Button(image=image_false,highlightthickness=0, command=self.false_pressed)
        self.button_true.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_quastion()

        self.window.mainloop()


    def get_next_quastion(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_quastion)