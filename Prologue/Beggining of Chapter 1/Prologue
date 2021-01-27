# Intro to Stage 2(Osaka)
print("New Stage Unlocked: Osaka")
print()
input("Welcome to Stage 2:Osaka")
input("TIP: If you want to make life easier,"
      "\ncopy and paste the choices/options. Or you can simply type them."
      "\nAll up to you ;)")
print()
print("Before we get start, you are required to fill out some info")
info = input("Is that okay?"
      "\nyes"
      "\nno"
      "\n:")
if info == "no":
    print("Understandable. Have a wonderful day")
    exit()
elif info == "yes":
    print("Okay, lets get started!")
# gender selection
firstname = input("What is your first name:")
lastname = input("What is your last name:")
print()
print()
gender = input("Select your gender:"
               "\nMan"
               "\nFemale"
               "\n:")
print()

input("Prologue(プロローグ)")
print()
# used to round up interview pts.  Determines if user will start the undercover case, immediately, or later on.
interviewpts = 0
total_q = 5
# first question
skilled = input("On a scale of of 1-10, 10 being very skilled, 1 being inexperienced,"
              "\nhow would you rate your driving skills"
                "\n1,2,3,4,5,6,7,8,9,10"
                "\n:")

if skilled == "1":
    print("You really need to work on these skills of yours")
    interviewpts -= 1
if skilled == "2":
    print("Work on those skills of yours")
    interviewpts -= 1
if skilled == "3":
    print("Work on this skills of yours")
    interviewpts -= 1
if skilled == "4":
    print("Gotta work on those skills buddy")
    interviewpts -= 1
if skilled == "5":
    print("Ehhh, we suggest improving those things.")
    interviewpts += 1
if skilled == "6":
    print("Hmm, thats fine.")
    interviewpts += 1
if skilled == "7":
    print("Ehh, that will do")
    interviewpts += 1
if skilled == "8":
    print("Pretty good, we will keep that under consideration..")
    interviewpts += 2
elif skilled == "9":
    print("Wow, thats impressive")
    interviewpts += 2
if skilled == "10":
    print("Thats pretty good!!!")
    interviewpts += 2
    print()
# second question
question2 = input("Interesting that you rated yourself "+skilled+" in the last test."
                  "\nNext question, how would you rate yourself in a situation where you're getting questioned."
                  "\nOr in general charisma."
                   "\non a scale from 1-10, 10 being the highest, how would you rate yourself?"
                   "\n:")
print()
if question2 == "1":
    print("You really need to work on these skills of yours")
    interviewpts -= 1
if question2 == "2":
    print("Work on those skills of yours")
    interviewpts -= 1
if question2 == "3":
    print("Work on this skills of yours")
    interviewpts -= 1
if question2 == "4":
    print("Gotta work on those skills buddy")
    interviewpts -= 1
if question2 == "5":
    print("Ehhh, we suggest improving those things.")
    interviewpts += 1
if question2 == "6":
    print("Hmm, thats fine.")
    interviewpts += 1
if question2 == "7":
    print("Ehh, that will do")
    interviewpts += 1
if question2 == "8":
    print("We will keep that under consideration..")
    interviewpts += 2
elif question2 == "9":
    print("Seems like you're one very charismatic person.  Hope you're a"+gender+" of your word")
    interviewpts += 2
if question2 == "10":
    print("Hope you're being honest, because you're gonna need it")
    interviewpts += 2
    print()
    # Question 3:undercover
question3 = input("Alright, onto the nex question. If you were, lets say undercover,"
                  "\nand due to a certain circumstance,you are required to inflict harm,"
                  "\nor potential kill a fellow Osaka Prefectural Police officer,"
                  "\nwould you do it?" 
                  "\nNever! I would never kill or harm a fellow officer!Regardless of the situation"
                  "\nIf i must, I will.  As long as the mission goes on and I can be successful in my goal"
                  "\nDoesn't bother me.  If he serves no value, who cares? "
                  "\n:")
print()
# Question 3 possible options
if question3 == "Never! I would never kill or harm a fellow officer!Regardless of the situation":
    print("The Passionate one are yah?  I respect that.")
    interviewpts += 1
if question3 == "Doesn't bother me.  If he serves no value, who cares?":
    print("Seems to me that you don't have any regard to any life?")
    interviewpts -= 1
elif question3 == "If i must, I will.  As long as the mission goes on and I can be successful in my goal":
    life = input("Hmm.... thats a interesting thing to say. So are you trying to say the mission is more important than the human?"
                 "\nHuman Life is definetely worth more than the mission."
                 "\nSometimes a sacrifice might have to made in order for progress to be made,"
                 "\nWell, if the dude ain't relevant to the mission, i could honestly care less?"
                 "\nI dont know"
                 "\n:")
    # Continuation of question 3 if you choose, if the mission goes, on, sacrifices must be made
    if life == "Human Life is definetely worth more than the mission.":
        print("Even if you could potentially fail the mission, you still have a moral side of you.  "
              "\nAnd still considerate to others, rather than being egoistic. I like that...")
        interviewpts += 1
    if life == "Sometimes a sacrifice might have to made in order for progress to be made,":
        print("Interesting. At the same time to,"
              "\nthroughout history we have made sacrifices, whether good or bad, we have had made progress. "
              "\nIntresting response.")
        interviewpts += 1
    elif life == "Well, if the dude ain't relevant to the mission, i could honestly care less?":
        print("So it seems to me that you have little to no regard for your fellow officers.  I'll keep that it mind ")
        interviewpts -= 1
    if life == "I dont know":
        print("Honestly, that isn't a valid question.  But since this question is taking longer than expected, onto the next question")
        interviewpts -= 1
        print()
        print()
    # life questions^
# start of question 4
question4 = input("What is the reason why do you want Osaka Prefectural police?:"
                  "\nTo protect and serve the great city of Osaka!"
                  "\nTo catch the bad guys"
                  "\nMy father and grandfather were officers of the Osaka Prefectural police. "
                  "\nRush hour, Beverley Hills Cop, and playing sleeping dogs inspired me."
                  "\n:")
print()
# Potiental question 4 options
if question4 == "To protect and serve the great city of Osaka!":
    print()
    # results if you choose these options for some reason
    bereal = input("Thats basically what every other cadet says, be honest.Why did you want to join the  Osaka Prefectural Police. "
                   "\nTo catch the bad guys"
                  "\nMy father and grandfather were officers of the Osaka Prefectural police. I want to continue the tradition"
                  "\nRush hour, Beverley Hills Cop, and playing sleeping dogs inspired me."
                   "\n:")
    if bereal == "To catch the bad guys":
        print("Intresting....But we'll see about that")
        print()
        interviewpts += 1
    elif bereal == "My father and grandfather were officers of the Osaka Prefectural police. I want to continue the tradition":
        print("Never knew you had family that were in the force. I respect you want to hold the tradition, but hope you can hold it well..")
        print()
        interviewpts += 1
    if bereal == "Rush hour, Beverley Hills Cop, and playing sleeping dogs inspired me.":
        print("So a movie and a game inspired you to join the force. Hmmm.....")
        print()
        interviewpts -= 1
# Question 4 continued
if question4 == "To catch the bad guys":
    print("Interesting....But we'll see about that")
    print()
    interviewpts += 0
elif question4 == "My father and grandfather were officers of the Osaka Prefectural police. I want to continue the tradition":
    print("Never knew you had family that were in the force. I respect you want to hold the condition, but hope you can hold it well..")
    print()
    interviewpts += 1
if question4 == "Rush hour, Beverley Hills Cop, and playing sleeping dogs inspired me.":
    question4 = input("I ain't gonna lie, Rush was a pretty good movie.  Sleeping dogs was a pretty good game as well."
          "\nBut are you sure..... theres more than just a movie in the game:"
          "\nI am actually being honest, they were my inspiration"
          "\nUmmm.. Im not sure.. I just like police cars..."
          "\nMy father and grandfather were officers in the Osaka Prefectural Police. I want to continue the tradition.")
    print()
if question4 == "I am actually being honest, they were my inspiration":
    print("well i'll be dammed.")
    print()
    interviewpts += 0
elif question4 == "mmm.. Im not sure.. I just like police cars...":
    print("Although our cars tend to be more nicer.  There is more to than just police cars.")
    print()
    interviewpts -= 1
if question4 == "My father and grandfather were officers in the Osaka Prefectural Police. I want to continue the tradition.":
    print("Never knew you had family that were in the force. I respect you want to hold the condition, but hope you can hold it well..")
    print()
    interviewpts += 1
# Last interview question
input("Since we are taking a little too much time. Lets go to our last and final question.")

risk = input("Last and final question, will you risk your life in order to protect those that need to be protected?"
             "\n"
             "\nNope, im sorry, but my life is very sacred"
             "\nAs long as these people that need to be protected can prosper and are benefited from my work, i will"
             "\nIm a cop, everyday is a risk.  Thats just life"
             "\nI dont know..."
             "\n:")
print()
if risk == "Nope, im sorry, but my life is very sacred":
    print("So you're trying to say you would rather save yourself, than your fellow officers or civillians...We'll keep that in mind")
    print()
if risk == "As long as these people that need to be protected can prosper and are benefited from my work, i will":
    print("Compassionate are yah.")
elif risk == "Im a cop, everyday is a risk.  Thats just life":
    print("You say that know.  But i hope you're ready to deal with them risk.  But i like your enthusiam.")
    print()
    interviewpts += 1
if risk == "I dont know...":
    risk = input("That isn't a valid response."
                 "\nLet me ask the question again, will you risk your life in order to protect those that need to be protected?"
                 "\nNope, im sorry, but my life is very sacred"
                 "\nAs long as these people that need to be protected can prosper and are benefited from my work, i will"
                 "\nIm a cop, everyday is a risk.  Thats just life ")
if risk == "Nope, im sorry, but my life is very sacred":
    print("So you're trying to say you would rather save yourself, than your fellow officers or civillians...We'll keep that in mind")
    print()
    interviewpts -= 1
elif risk == "As long as these people that need to be protected can prosper and are benefited from my work, i will":
    print("Compassionate are yah.")
    print()
    interviewpts += 1
if risk == "Im a cop, everyday is a risk.  Thats just life":
    print("Damn right it is.  But I just hope that you can face these risks.")
    print()
    interviewpts += 1
# Interview questions ending
print()
print()
input("Alright "+firstname+", you have completed the interview process.")

id = input("--------------------------------------------|"
"\n|      Osaka   Prefectural Police           |"
"\n|               大阪府警察                    |"
"\n|       "+firstname+" "+lastname+"         |"
"\n| Senior police officer (巡査長, junsa-chō)  |"
"\n|   🌟                                      |"
"\n|     大阪府警察                              |"
"\n|    Osaka-fu-keisatsu                      |"
"\n|   Criminal Affairs Bureau((刑事局)         |"
"\n|___________________________________________|"
"\nConfirm ID card?"
"\nyes"
"\nno"
"\n:")

if id == "no":
    id = input("What is it that you want to change?"
               "\nbranch"
               "\nrank"
               "\n:")
    if id == "rank":
        print("I mean you just got promoted.  If you want to rank up, you'll have to earn it. ")
    elif id == "branch":
        print("In that case, you'll have to talk to your supervisor.")
if id == "yes":
    input("Congratulations "+firstname+", you are now offically a Senior police officer in the Osaka Prefectural Police!!!")
total = (interviewpts / total_q) * 100
print("Interview pts score:", str(interviewpts) + '%')

input("Chapter 1:The Chase Begins(第 1 章：チェイスが始まります)")
