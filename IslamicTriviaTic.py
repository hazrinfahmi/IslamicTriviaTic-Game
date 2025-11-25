from tkinter import *
import random

x_score = 0
o_score = 0

questions = [
    {"question": "Muslims are prohibited from eating Beef? (True/False)","answer": "false"},
    {"question": "All Muslims are Arabs. (True/False)", "answer": "false"},
    {"question": "Islam is a violent religion that promotes terrorism. (True/False)", "answer": "false"},
    {"question": "There are 5 pillars of Islam. (True/False)", "answer": "true"},
    {"question": "Muslims can eat during Ramadhan. (True/False)", "answer": "false"},
    {"question": "Is prophet Muhammad the last prophet of Islam? (True/False)", "answer": "true"},
    {"question": "The Quran was the only holy book revealed by Allah during the month of Ramadan? (True/False)", "answer": "false"},
    {"question": "Is Muharram is the first month in Islam (True/False)", "answer": "true"},
    {"question": "Is Kaabah located in Makkah? (True/False)", "answer": "true"},
    {"question": "Al Fatihah is the first surah in the Quran? (True/False)", "answer": "true"},   
    ]

bonus_questions = [
    {"question": "Who was the Prophet's mother?", "answer": "Aminah"},
    {"question": "Where did the prophet first receive the message of Islam? ", "answer": "Cave Hira"},
    {"question": "What battle happen during Ramadhan?", "answer": "battle of badr"},
    {"question": "Who was the first prophet of Allah (s.w.t.)? ", "answer": "Prophet Adam"},
    {"question": "What is the meaning of Al-Fil ?", "answer": "elephant"},
    {"question": "How many fard rakahs do we pray in Salat al Asr?", "answer": "four"},
    {"question": " What is the name of the book sent down to Prophet Ibrahim (a.s.)?", "answer": "tawrat"},
    {"question": "Who was the last Prophet of Allah (s.w.t.)?", "answer": "prophet Muhammad"},
]
last_question_index = -1
last_question = None


def get_random_question():
    global last_question
    remaining_questions = [q for q in questions if q != last_question]
    question = random.choice(remaining_questions)
    last_question = question
    return question

def check_answer():
    global quiz_window
    user_answer = answer.get().lower()
    correct_answer = last_question["answer"].lower()

    if user_answer == correct_answer:
        quiz_window.destroy()
        tictactoewindow()
    else:
        show_sorry_window()

def show_sorry_window():
    sorry_window = Toplevel(root)
    sorry_window.title("Sorry")
    sorry_label = Label(sorry_window, text="Sorry, your answer is incorrect.")
    sorry_label.pack()

def quizWindow():
    global quiz_window
    quiz_window = Toplevel(root)
    quiz_window.title("Islamic Quiz")

    question_data = get_random_question()
    question_label = Label(quiz_window, text=question_data["question"])
    question_label.pack()

    global hint_label
    hint_label = Label(quiz_window, text="")
    hint_label.pack()

    global answer
    answer = StringVar()
    answer_entry = Entry(quiz_window, textvariable=answer)
    answer_entry.pack()

    submit_button = Button(quiz_window, text="Submit", command=check_answer)
    submit_button.pack()

    hint_button = Button(quiz_window, text="Hint", command=show_hint)
    hint_button.pack()

def check_answer_bonus():
    global x_score
    user_bonus_answer=bonusAnswer.get().strip().lower()
    correct_answer = bonus_question["answer"].lower()
    if user_bonus_answer == correct_answer:
        x_score += 1
        xScore.config(text=f"X = {x_score}")
        bonusQuiz.destroy()
    else:
        show_sorry_window()
        bonusQuiz.destroy()

def bonus():

    global bonusQuiz
    bonusQuiz = Toplevel(root)
    bonusQuiz.title("Bonus Quiz")

    global bonus_question
    bonus_question = random.choice(bonus_questions)

    bonus_label = Label(bonusQuiz, text = bonus_question["question"])
    bonus_label.pack()

    global bonusAnswer
    bonusAnswer = StringVar()
    bonusAnswer_entry = Entry(bonusQuiz, textvariable=bonusAnswer)
    bonusAnswer_entry.pack()

    bonus_submit_button = Button(bonusQuiz, text="Submit", command= check_answer_bonus)
    bonus_submit_button.pack()


def show_hint():
    
    first_letter_hint = last_question["answer"][0].upper()  # Get the first letter of the answer and convert it to uppercase
    hint_label.config(text=f"Hint: The first letter of the answer is '{first_letter_hint}'")

# Create the main window
root = Tk()
root.title("Islamic TriviaTic")

# Button to open the first top level window
global mainframe1
mainframe1 = Frame(root)
mainframe1.pack()

maintitleLabel = Label(mainframe1 , text="Islamic TriviaTic " , font=("Arial" , 26) , bg="orange", width= 16  )
maintitleLabel.grid(row=0 , column=0)
main_window_button = Button(root, text="START", command=quizWindow)
main_window_button.pack()

def tictactoewindow():
    global x_score, o_score

    global tictactoe_window
    tictactoe_window = Toplevel(root)
    tictactoe_window.title("Islamic TriviaTic")

    global frame1
    frame1 = Frame(tictactoe_window)
    frame1.pack()
    titleLabel = Label(frame1 , text="Islamic TriviaTic " , font=("Arial" , 26) , bg="orange", width= 16  )
    titleLabel.grid(row=0 , column=0)

    global scoreFrame
    scoreFrame = Frame(tictactoe_window )
    scoreFrame.pack()

    global frame2
    frame2 = Frame(tictactoe_window , bg="white")
    frame2.pack()

    global optionFrame
    optionFrame = Frame(tictactoe_window , bg="white")
    optionFrame.pack()

    global x_score, xScore
    xScore = Label(scoreFrame , text=f"X = {x_score}" , font=("Arial" , 26) , bg="yellow", width=7 )
    xScore.grid(row=1 , column=0, padx=(0, 10))
    xScore.config(highlightthickness=1, highlightbackground="black")
    
    global o_score, oScore
    oScore = Label(scoreFrame , text=f"O = {o_score}"  , font=("Arial" , 26) , bg="yellow" , width=7)
    oScore.grid(row=1 , column=1, padx=(10, 0))
    oScore.config(highlightthickness=1, highlightbackground="black")

    # Tic Tac Toe Board 

    #  First row 
    
    global button1
    button1 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="white" , relief=RAISED , borderwidth=5)
    button1.grid(row = 2 , column=0)
    button1.bind("<Button-1>" , play)

    global button2
    button2 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button2.grid(row = 2 , column=1)
    button2.bind("<Button-1>" , play)
    
    global button3
    button3 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button3.grid(row = 2 , column=2)
    button3.bind("<Button-1>" , play)

    #  second row 

    global button4
    button4 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button4.grid(row = 3 , column=0)
    button4.bind("<Button-1>" , play)

    global button5
    button5 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button5.grid(row = 3 , column=1)
    button5.bind("<Button-1>" , play)

    global button6
    button6 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button6.grid(row = 3 , column=2)
    button6.bind("<Button-1>" , play)

    #  third row 

    global button7
    button7 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="white" , relief=RAISED , borderwidth=5)
    button7.grid(row = 4 , column=0)
    button7.bind("<Button-1>" , play)

    global button8
    button8 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="white" , relief=RAISED , borderwidth=5 )
    button8.grid(row = 4 , column=1)
    button8.bind("<Button-1>" , play)

    global button9
    button9 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="white" , relief=RAISED , borderwidth=5)
    button9.grid(row = 4 , column=2)
    button9.bind("<Button-1>" , play)

    restartButton = Button(optionFrame , text="Restart Game" , width=13  , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED  , command=restartGame )
    restartButton.grid(row=5 , column=0 )

    bonusButton = Button(optionFrame , text="Bonus Point" , width=13  , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , command=bonus )
    bonusButton.grid(row=5 , column=1 )

    global buttons
    buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8, button9]
    

    global board
    board = { 1:" " , 2:" " , 3:" ",
              4:" " , 5:" " , 6:" ",
              7:" " , 8:" " , 9:" " }
    global turn
    turn = "x"
    global game_end
    game_end = False
    global mode
    mode = "singlePlayer"


def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]

def checkForWin(player):
    # rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True

    # columns
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    
    # diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    

    return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    
    return True

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "
        button.config(bg="white")

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1, text="Islamic TriviaTic", font=("Arial", 26), bg="orange", width=16)
    titleLabel.grid(row=0, column=0)

    tictactoe_window.destroy()
    quizWindow()

def minimax(board , isMaximizing):
    
    if checkForWin("o"):
        return 1 
    
    if checkForWin("x"):
        return -1
    
    if checkForDraw():
        return 0
    
    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board , False) # minimax
                board[key] = " "
                if score > bestScore : 
                    bestScore = score 
        
        return bestScore
    
    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board , True) # minimax
                board[key] = " "
                if score < bestScore : 
                    bestScore = score 
        
        return bestScore

def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board , False) # minimax
            board[key] = " "
            if score > bestScore : 
                bestScore = score 
                bestMove = key

    board[bestMove] = "o"

# Function to play
def play(event):
    global turn,game_end, x_score, o_score
    if game_end:
        return
    
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n" :
        clicked = 1
    else :
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "x" :
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16 )
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                x_score += 1
                xScore.config(text=f"X = {x_score}")
                game_end = True
                
                change_button_color(board, turn)
                
            turn = "o"

            updateBoard()

            if mode == "singlePlayer":

                playComputer()

                if checkForWin(turn):
                    winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16   )
                    winningLabel.grid(row = 0 , column=0 , columnspan=3)
                    o_score += 1
                    oScore.config(text=f"O = {o_score}")
                    game_end = True
                    
                    change_button_color(board, turn)
                    
                turn = "x"

                updateBoard()

           
            
        else:
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game" , bg="orange", font=("Arial" , 26),width=16)
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True
            turn = "x"

        
        if checkForDraw():
            drawLabel = Label(frame1 , text=f"Game Draw" , bg="orange", font=("Arial" , 26), width = 16)
            drawLabel.grid(row = 0 , column=0 , columnspan=3)

def change_button_color(board, player):
    for row in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
        if all(board[i] == player for i in row):
            for i in row:
                buttons[i-1].config(bg="red")





root.mainloop()

