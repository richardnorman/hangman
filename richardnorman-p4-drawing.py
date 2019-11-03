import stddraw

def draw_initial(word_to_guess):
    stddraw.setFontSize(36)
    stddraw.text(0.15,0.95,"Hangman")
    stddraw.text(0.5,0.3,word_to_guess)

def draw_hanging_man(guesses_remaining):
    #draw floor
    stddraw.line(0.2,0.4,0.8,0.4)
    stddraw.rectangle(0.3,0.4,0.4,0.04)
    if guesses_remaining <= 7:
        #head
        stddraw.circle(0.5,0.8,0.07)
        if guesses_remaining <= 6:
            #torso
            stddraw.line(0.5,0.73,0.5,0.55)
            if guesses_remaining <= 5:    
                #left arm
                stddraw.line(0.5,0.73, 0.425,0.655)
                if guesses_remaining <= 4:
                    #right arm
                    stddraw.line(0.5,0.73, 0.575,0.655)
                    if guesses_remaining <= 3:
                        #left leg
                        stddraw.line(0.5,0.55, 0.425,0.465)
                        if guesses_remaining <= 2:
                            #right leg
                            stddraw.line(0.5,0.55, 0.575,0.465)
                            if guesses_remaining <= 1:
                                #gallows
                                stddraw.line(0.7,0.404,0.7,0.9)
                                stddraw.line(0.7,0.9,0.5,0.9)
                                stddraw.line(0.5,0.9,0.5,0.87)
                                if guesses_remaining == 0:
                                    #face
                                    #left eye
                                    stddraw.line(0.465,0.82,0.485,0.8)
                                    stddraw.line(0.485,0.82,0.465,0.8)

                                    #right eye
                                    stddraw.line(0.515,0.82,0.535,0.8)
                                    stddraw.line(0.535,0.82,0.515,0.8)
                                    #mouth
                                    stddraw.line(0.475,0.775,0.525,0.775)

def draw_bad_guesses(bad_guesses):
    stddraw.text(0.5,0.05,"Bad guesses: " + " ".join(bad_guesses))

def draw_guesses_remaining(guesses_remaining):
    stddraw.text(0.5,0.15,"Remaining guesses: " + str(guesses_remaining))

def draw_results(guesses_remaining, word_to_guess):
    if guesses_remaining == 0:
        stddraw.setPenColor(stddraw.DARK_RED)
        stddraw.text(0.5,0.3,"You lost! Try playing again.")
    else:
        stddraw.setPenColor(stddraw.DARK_GREEN)
        stddraw.text(0.5,0.3,"Congrats! You won the game!")
    stddraw.text(0.5,0.225,"The word was: " + word_to_guess)
    stddraw.show()

def show_drawing():
    stddraw.show(0.0)

def clear_drawing():
    stddraw.clear()