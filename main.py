# Intro to Stage 2(Osaka)
input("\n--------------------------------"
      "\n| 🔓New Stage Unlocked: Osaka🔓 |"
      "\n|                              |"
      "\n|  🔰Hashiriya Undergrounds🔰   |"
      "\n|    🔰Phase 2(Osaka)🔰         |"
      "\n|                              |"
      "\n|______________________________|")
input("TIP: If you want to make life easier,"
      "\ncopy and paste the choices/options.")
print()
input("Or you can simply type them......."
      "\nIf you choose that route, make sure you type the selected option EXACTLY AS YOU SEE IT")
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

if skilled == str(skilled):
    print("You really need to work on these skills of yours")
elif skilled == str():
    print("We'll keep that under consideration")
    interviewpts += 1
    print()
# second question
question2 = input("Interesting that you rated yourself " + skilled + " in the last test."
                                                                     "\nNext question, how would you rate yourself in a situation where you're getting questioned."
                                                                     "\nOr in general charisma."
                                                                     "\non a scale from 1-10, 10 being the highest, how would you rate yourself?"
                                                                     "\n:")
print()
if question2 == [1, 2, 3, 4, 5, 6]:
    print("Ehhh, we suggest improving those things.")

if question2 == [7, 8, 9, 10]:
    print("Hope you're being honest, because you're gonna need it")
    interviewpts += 1
    print()
    # Question 3:undercover
question3 = input("Alright, onto the nex question. If you were, lets say undercover,"
                  "\nand due to a certain circumstance,you are required to inflict harm,"
                  "\nor potential kill a fellow Osaka Prefectural Police officer,"
                  "\nwould you do it?"
                  "\n(1)Never! I would never kill or harm a fellow officer!Regardless of the situation"
                  "\n(2)If i must, I will.  As long as the mission goes on and I can be successful in my goal"
                  "\n(3)Doesn't bother me.  If he serves no value, who cares? "
                  "\n:")
print()
# Question 3 possible options
if question3 == "Never! I would never kill or harm a fellow officer!Regardless of the situation" or question3 == "1":
    print("The Passionate one are yah?  I respect that.")
    interviewpts += 1
if question3 == "Doesn't bother me.  If he serves no value, who cares?" or question3 == "2":
    print("Seems to me that you don't have any regard to any life?")
    interviewpts -= 1
elif question3 == "If i must, I will.  As long as the mission goes on and I can be successful in my goal" or question3 == "3":
    life = input("Hmm.... thats a interesting thing to say. So are you trying to say the mission is more important than the human?"
                 "\n(Life)Human Life is definitely worth more than the mission."
                 "\n(Sacrifice)Sometimes a sacrifice might have to made in order for progress to be made,"
                 "\n(care less)Well, if the dude ain't relevant to the mission, i could honestly care less?"
                 "\n(idk)I dont know"
                 "\n:")
    # Continuation of question 3 if you choose, if the mission goes, on, sacrifices must be made
    if life == "Human Life is definitely worth more than the mission." or life == "Life":
        print("Even if you could potentially fail the mission, you still have a moral side of you.  "
              "\nAnd still considerate to others, rather than being egoistic. I like that...")
        interviewpts += 1
    if life == "Sometimes a sacrifice might have to made in order for progress to be made," or life == "Sacrifice":
        print("Interesting. At the same time to,"
              "\nthroughout history we have made sacrifices, whether good or bad, we have had made progress. "
              "\nInteresting response.")
        interviewpts += 1
    elif life == "Well, if the dude ain't relevant to the mission, i could honestly care less?" or life == "care less":
        print("So it seems to me that you have little to no regard for your fellow officers.  I'll keep that it mind ")
        interviewpts -= 1
    if life == "I dont know" or life == "idk":
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
# Potential question 4 options
if question4 == "To protect and serve the great city of Osaka!":
    print()
    # results if you choose these options for some reason
    bereal = input("Thats basically what every other cadet says, be honest.Why did you want to join the  Osaka Prefectural Police. "
                   "\n(bad guys)To catch the bad guys"
                   "\n(tradition)My father and grandfather were officers of the Osaka Prefectural police. I want to continue the tradition"
                   "\n(inspiration)Rush hour, Beverley Hills Cop, and playing sleeping dogs inspired me."
                   "\n:")
    if bereal == "To catch the bad guys" or bereal == "bad guys":
        print("Interesting....But we'll see about that")
        print()
        interviewpts += 1
    elif bereal == "My father and grandfather were officers of the Osaka Prefectural police. I want to continue the tradition" or bereal == "tradition":
        print("Never knew you had family that were in the force. I respect you want to hold the tradition, but hope you can hold it well..")
        print()
        interviewpts += 1
    if bereal == "Rush hour, Beverley Hills Cop, and playing sleeping dogs inspired me." or bereal == "inspiration":
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
                      "\nMy father and grandfather were officers in the Osaka Prefectural Police. I want to continue the tradition."
                      "\n:")
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
             "\n(sacred)Nope, im sorry, but my life is very sacred"
             "\n(benefit)As long as these people that need to be protected can prosper and are benefited from my work, i will"
             "\n(everyday is a risk)Im a cop, everyday is a risk.  Thats just life"
             "\n:")
print()
if risk == "Nope, im sorry, but my life is very sacred" or risk == "sacred":
    print("So you're trying to say you would rather save yourself, than your fellow officers or civilians..."
          "\nWe'll keep that in mind")
    print()
if risk == "As long as these people that need to be protected can prosper and are benefited from my work, i will" or risk == "benefit":
    print("Compassionate are yah.")
elif risk == "Im a cop, everyday is a risk.  Thats just life" or risk == "everyday":
    print("You say that know.  But i hope you're ready to deal with them risk.  But i like your enthusiasm.")
    print()
    interviewpts += 1
# Interview questions ending
print()
print()
input("Alright " + firstname + ", you have completed the interview process.")
rank1 = "Senior Police Officer"
# Police ID
id = input("--------------------------------------------"
           "\n|      Osaka   Prefectural Police          |"
           "\n|               大阪府警察                   |"
           "\n|       " + firstname + " " + lastname + "            |"
                                                       "\n|      " + rank1 + " (巡査長, junsa-chō) |"
                                                                             "\n|   🌟                                       |"
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
    input("Congratulations " + firstname + ", "
                                           "\nyou are now officially a Senior police officer in the Osaka Prefectural Police!!!")
# Beggining of chapter 1
input("Chapter 1:The Chase Begins(第 1 章：チェイスが始まります)")
print()
callin = input("While doing a regular patrol, you are called back to a briefing back at the station."
               "\nDo you go or just keep doing what you doing?"
               "\n(1)keep doing what you doing"
               "\n(2)go back to the station"
               "\n:")
if callin == "keep doing what you doing" or callin == "1":
    print("You're fired"
          "\nThe end🙂"
          "\nGAME OVER")
    exit()
elif callin == "go back to the station" or callin == "2":
    print("Smart choice, because either that or you were outta the job.")
    print()
input("You arrive at the station and see a couple of other officers gathered up."
      "\nYour supervisor, Chief Inspector Tayamo Nakamura enters the room:")
print()
input("Chief Inspector Nakamura🗣- Alright, settle down.  Today is a new case, and that means a crackdown"
      "\nBased on  recent reports and incidents, we are starting to witness a increase in Street racing activity,"
      "\nparticularly on Hanshin Expressway:Loop 1. Based on intel, we have learned that a street racing organization,"
      "\nKnown as the Dinka Racing Club has been committing these activities.")
print()
# A special surprise tool that will help us later ;)
coprep = 0
inspector = "Chief Inspector Nakamura"
hanshin = input("(big of a deal)But chief inspector, how is a street racing group that big of a deal"
                "\n(ignore)I dont think its that big of a problem. Lets just ignore it"
                "\n(listen)Just listen to ya damn supervisor"
                "\n:")

if hanshin == "But chief inspector, how is a street racing group that big of a deal" or hanshin == "big of a deal":
    input("Chief Inspector Nakamura🗣- Hmmm, maybe because with the increase in this street racing activity,"
          "\nTheres also somehow a increase in vandalism and motor accidents on the hanshin and around Osaka as well. ")
elif hanshin == "I dont think its that big of a problem. Lets just ignore it" or hanshin == "ignore":
    input("Chief Inspector Nakamura🗣- Yup, lets also just ignore the vandalism and motor accidents as well."
          "\n Too bad Senior Officer " + lastname + ", but you cant make that call.")
    coprep -= 1
else:
    print("Good you're listening to your supervisors! Here some free cop rep for you!!")
    coprep += 2
    print()
# Dinka Racing Club Hierarchy
input("Chief Inspector Nakamura🗣- As i was saying, I want everyone to memorize this list before i get any further"
      "\nBig Koi"
      "\n|"
      "\nLittle Koi"
      "\n|"
      "\nColossals"
      "\n|"
      "\nJumbos"
      "\n|"
      "\nGuppies")
print()
koi = input("(naming)Why are they named after fish and shrimp sizes"
            "\n(try not to laugh)Read the names, but try not laugh"
            "\n(STOOPID)Those are some pretty stupid but, they do make you a little hungry"
            "\n:")
if koi == "Why are they named after fish and shrimp sizes?" or koi == "naming":
    print("Chief Inspector Nakamura- At the moment, we're not 100% sure,"
          "\nBut there is intel which reports that they report at a restaurant,"
          "\nthat does special in Koi.  But we'll get to that in a bit. ")

elif koi == "Those are some pretty stupid but, they do make you a little hungry" or koi == "STOOPID":
    print("\nCertain names dont make sense.  But maybe we'll fine a meaning to them")

if koi == "Read the names, but try not laugh" or koi == "try not to laugh":
    print("Chief Inspector Nakamura- You aren't fooling anyone..You can laugh..🤦")
    print()

# Description of Dinka racing club(DRC)
input("Chief Inspector Nakamura- Anyway, in a nutshell, the big koi is the head of the racing group. But, this person is so well hidden,"
      "\nthat we dont have info on him. "
      "\nThe Little Koi is basically the underboss, or the second in command,"
      "\nhe foresees any actions, or gives an okay on certain meets."
      "\nThe colossals are more of the seniors/Lieutenants of the group.  They tend to be in charge of meets, tells little koi about activities etc.."
      "\nNow onto the Jumbos and Guppies.  The Guppies are the lowest of the low.  Newbies/ new members of the racing club."
      "\nThey dont really start driving until they become Jumbos, or if they're lucky, can drive under certain circumstances"
      "\nWhereas the Jumbos are the rank above the guppies, but, mainly oversee the newbies and assist them.")
print()
input("To those who decide to join the case, will starts as a Guppie, and work their way up.")

guppie = input("So the sizes of these seafoods, determines the power the ranks have?"
               "\n(intel)Do we have intel on those other than the Big Koi"
               "\n(no intel)What causes you to not get intel on the Big Koi"
               "\n(shut yo mouth)remain silent"
               "\n:")

if guppie == "Do we have intel on those other than the Big Koi" or guppie == "intel":
    input("We do have info on some of the guppies and jumbos."
          "\nBut not as much compared to the Colossals and the Little Koi."
          "\nThey tend not to be so open.")
    print()
elif guppie == "What causes you to not get intel on the Big Koi" or guppie == "not intel":
    print("The Upper ranks in the racing group tend to be more secretive in the their activities."
          "\nCompared to the Jumbos and Guppies who brag and post everything they do on social media, specifically Instagram."
          "\nPlus, the tend to be a little old school with their activities...")
    print()
if guppie == "remain silent" or guppie == "shut yo mouth":
    print("...")
    print()
# Newspaper investigation
thehint = input("Now if you open your folders. You'll see a newspaper,"
                "\nexamine it, and tell me whats wrong, and what you think it means."
                "\n|----------------------------------------------------------------"
                "\n|                  The Japan Times                              |"
                "\n|   DEFEAT: JPN National soccer team"
                "\n|   losses  against South Kora National soccer team             |"
                "\n|             10-8"
                "\n|   Fire  at local bar in Dotonbori                             |"
                "\n|   No casualties. Caused by local chef                         |"
                "\n|   The local bar is closed till further notice                 |"
                "\n|                                                               |"
                "\n|                             Increased cases in vandalism       |"
                "\n| Tokyo auto salon confirmed: AND motor accidents on Hanshin    |"
                "\n| January 15-21st            No words from the Osaka Police    |"
                "\n|                                                               |"
                "\n|                       ジャパンタイムズ                           |"
                "\n|                      Buy one get one free!!                   |"
                "\n|                  Tire, Rims, paints, and Ramanue sale!!       |"
                "\n|             More info:Come to Hanshin Expressway between 7-8pm|"
                "\n|_______________________________________________________________|"
                "\nWhere do you think the problem is?:"
                "\n(JPN takes the L)Japan losing against South Korea.  We all know that game was rigged🙄."
                "\n(sale on hanshin)The sale on the Hanshin expressway seems sus."
                "\n(insurance money)How the hell do they know it was the chef, maybe the boss rigged it for insurance money"
                "\n(situation with press)Wait, the the department didn't discuss the whole situation with the press?"
                "\n:")
print()
# Newspaper potential options results
if thehint == "Japan losing against South Korea.  We all know that game was rigged🙄." or thehint == "JPN takes the L ":
    print("Chief Inspector Nakamura- Hey man, a L is a L.  But at least we still qualified in the AFC Asian cup."
          "\nBut no, the actual hint is at the bottom, the sale."
          "\nWe've come to learn that this is their code talk in order to tell each other about when a meet is going on."
          "\nThis also includes the time(7-8pm) and location (hanshin expressway), normally this occurs during weekends. ")

if thehint == "The sale on the Hanshin expressway seems sus" or thehint == "sale on hanshin":
    print("Chief Inspector Nakamura- Right on Senior officer" + lastname + ". "
                                                                           "\nThis is actually a encrypted code which is used by members of the DRC to communicate with each. "
                                                                           "\nIn regards to car meets,"
                                                                           "\nIts not always a sale, but it could be hw help, or some other weird shit."
                                                                           "\nBut good thing you found " + firstname + ". ")
    coprep += 1
elif thehint == "How the hell do they know it was the chef, maybe the boss rigged it for insurance money" or thehint == "insurance money":
    print("Chief Inspector Nakamura- Maybe it was, maybe it wasn't. It probably was since the boss had fire insurance..."
          "\nBut anyway.No.This is actually a encrypted code which is used by members of the DRC to communicate with each."
          "\nEspecially in regards to car meets")
elif thehint == "Wait, the the department didn't discuss the whole situation with the press?" or thehint == "situation with press":
    print("Chief Inspector Nakamura- No, because if we did, than this case wouldn't happen."
          "\nAnd probably the DRC would be more secretive than they already are. "
          "\nBut the part where the sale is actually a encrypted code which is used to communicate info between members of the DRC")

print()
input("playa-Why cant we just used high speed cameras, and call it a day? ")
print()
input("" + inspector + " -""Two-three reasons."
                       "\nOne-The members tend to used this spray which blocks out their licence plate, so it isn't read by the camera."
                       "\nTwo-Even if they get a fine of speeding, they're so rich, they pay it witihin a hour."
                       "\nor if they get arrested, they can bail themselves out in under 2 hrs"
                       "\nThree- most of their cars can outrun most of our squad cars, with the exception of skyline squad cars.")
print()
input("" + inspector + " -""Now, after close examination, we come to determine that,Senior Officer" + lastname + ","
                                                                                                                 "\nSergeant Satoshi, and Sergeant Ryosuke will be the ones that will infiltrate the racing club, and bring it down."
                                                                                                                 "\nWe'll also collaborate with the traffic bureau as well.")
print()
input("" + inspector + "- Dismissed...")
print()
sidekick1 = "Sergeant Satoshi"
sidekick2 = "Sergeant Ryosuke"

input("Chapter 3: The actual chase begins")

print()

input("" + inspector + "-Alright, settle down, settle down...."
                       "\nToday we got leads that we're going for a bust."
                       "\nBut today we are going to infiltrate the DRC.")
print()
input("But we'll do this via showing off your ride at a race,"
      "\nThe cars that are preferred by the DRC are Honda's,Nissan's, and Toyota's."
      "\nToday you will choose one of these cars, and we'll modify them."
      "\nTo enter the DRC, you car needs to hit at least 150 mph.")
print()
# Car selection Nissan Or Honda
brand = input("You head out back to the parking lot and see a couple of cars.."
              "\nChoose you car brand of your choice:"
              "\nHonda"
              "\nNissan"
              "\nToyota"
              "\n:")
actual = input("Choose you car brand of your choice:"
               "\nHonda"
               "\nNissan"
               "\nToyota"
               "\n:")
# Honda option
if actual == "Honda":
    actual = input("Select the honda model of your choice." + actual + ":"
                                                                       "\nEK9"
                                                                       "\nNSX")
if actual == "EK9":
    print("Technical specs of " + brand + "" + actual + ":"
                                                        "\nBody Style- 2 door hatchback"
                                                        "\nLayout-Front engine, front wheel drive(F-F)"
                                                        "\nEngine type-  1.6 L B16B Inline 4"
                                                        "\nHorsepower- 182 hp"
                                                        "\nTorque-160 NM"
                                                        "\nTransmission-5 speed manual"
                                                        "\nWeight- 2,403 lb(1,090 kg)"
                                                        "\nProduction-  1997-2000"
                                                        "\nTop speed:146 MPH")

elif actual == "NSX":
    print("Body Style- 2 door coupe,2 door targa top"
          "\nLayout- Transverse mid-engine,RWD"
          "\nEngine type-  Honda C30A V6"
          "\nHorsepower- 270 hp"
          "\nTorque-210 lb-ftt"
          "\nTransmission-5 OR 6 SPEED MANUAL"
          "\nWeight- 3,020 lb(1,370 kg)"
          "\nProduction-  1990-2005"
          "\nTop speed:191 MPH")
# Nissan car option
if actual == "Nissan":
    actual = input("Select a model." + brand + "."
                                               "\nSkyline"
                                               "\nFairlady"
                                               "\n:")
# Fairlady or Skyline models
if actual == "Skyline":
    actual = input("Select a Model:"
                   "\nSkyline R34"
                   "\nSkyline R33"
                   "\nSkyline R32")
    if actual == "Skyline R34":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- 2 door coupe"
                                                       "\nLayout-front engine, 4WD"
                                                       "\nEngine type- 2.6 L TT RB26DETT I6"
                                                       "\nHorsepower- 166 hp"
                                                       "\nTorque- 173 lb -ft"
                                                       "\nTransmission-5 or 6 speed manual"
                                                       "\nWeight- 3,673 lbs(1666 kg)"
                                                       "\nProduction-  1998-2002"
                                                       "\nTop speed:165 mph"
                                                       "\n0-60:4.8 second")
    elif actual == "Skyline R33":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- Coupe"
                                                       "\nLayout- Front, All wheel drive"
                                                       "\nEngine type- RB26DETT I6 Twincam,TT Intercooled"
                                                       "\nHorsepower- 276 hp"
                                                       "\nTorque- 173 lb -ft"
                                                       "\nTransmission-5 speed manual"
                                                       "\nWeight- 3530 lbs(1601 kg)"
                                                       "\nProduction-  1995-1998"
                                                       "\nTop speed:156 mph"
                                                       "\n0-60: 5.2 seconds")
    if actual == "Skyline R32":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- Coupe"
                                                       "\nLayout- front engine, all wheel drive"
                                                       "\nEngine type-RB26DETT I6 Twincam,TT Intercooled"
                                                       "\nHorsepower-  280 hp"
                                                       "\nTorque- 260 lb -ft"
                                                       "\nTransmission-5 speed manual"
                                                       "\nWeight- 3153 lbs(1430 kg)"
                                                       "\nProduction-  1989-1994"
                                                       "\nTop speed:156 mph"
                                                       "\n0-60:5.6 seconds")

if actual == "Fairlady":
    actual2 = input("Select a model," + brand + ":"
                                               "\nFairlady Z 300ZX"
                                               "\nFairlady 240Z"
                                               "\nFairlady Z 350Z")
    if actual2 == "Fairlady Z 300ZX":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- Coupe"
                                                       "\nLayout- front engine, rear wheel drive"
                                                       "\nEngine type- 3.0 VG30DE V6"
                                                       "\nHorsepower- 222 hp"
                                                       "\nTorque- 198 lb -ft"
                                                       "\nTransmission-5 speed manual, 4 speed automatic"
                                                       "\nWeight- 3329-3538 lbs(1510-1605 kg)"
                                                       "\nProduction-  1989-2000"
                                                       "\nTop speed: 155 mph"
                                                       "\n0-60: 5-6 seconds")
    elif actual == "Fairlady 240Z":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- 3 door hatchback coupe"
                                                       "\nLayout-front engine, rear wheel drive"
                                                       "\nEngine type- 2.4 L L24 I6"
                                                       "\nHorsepower- 151 hp"
                                                       "\nTorque- 146 lb -ft"
                                                       "\nTransmission-3 speed automatic, 4 or 5 speed manual"
                                                       "\nWeight- 2,301.6 lbs(1,044 kg)"
                                                       "\nProduction-  1969-1973"
                                                       "\nTop speed: 126 mph"
                                                       "\n0-60: 8 seconds")
    if actual2 == "Fairlady Z 350Z":
        print("Tech specs of " + brand + "" + actual + ""
                                                       "\nBody Style- Hatchback coupe/roadster"
                                                       "\nLayout-Front engine, rear wheel drive"
                                                       "\nEngine type-3.5 L VQ35DE V6"
                                                       "\nHorsepower- 287 hp"
                                                       "\nTorque- 276 lb -ft"
                                                       "\nTransmission-5 speed automatic, 6 speed manual"
                                                       "\nWeight- 3,188-3,602 lbs(1,446-1,634 kg)"
                                                       "\nProduction-  2002-2008"
                                                       "\nTop speed:155 mph"
                                                       "\n0-60: 1.2 seconds")
    # Toyota car options
    if actual == "Toyota":
        actual = input("Select a " + brand + " Model you want."
                                             "\nToyota Supra MK3"
                                             "\nToyota Soarer 2.5GT"
                                             "\n:")

        if actual == "Toyota Supra MK3":
            print("Tech specs of " + brand + "" + actual + "."
                                                           "\nBody Style- coupe"
                                                           "\nLayout- front engine, rear wheel drive"
                                                           "\nEngine type- Toyota 7m -GTE (Modified CT26 Turbo"
                                                           "\nhorsepower- 267 hp"
                                                           "\nTorque- 264 lb -ft"
                                                           "\nTransmission-5 speed manual, 4 speed automatic"
                                                           "\nWeight- 3,219-3,616 lbs(manual)3,483-3,792 lbs(automatic)"
                                                           "\nProduction-  1986-1993"
                                                           "\nTop speed: 144 mph"
                                                           "\n0-60: 6.9 seconds")

        elif actual == "Toyota Soarer 2.5GT":
            print("Tech specs of " + brand + "" + actual + ""
                                                           "\nBody Style- 2 door coupe"
                                                           "\nLayout- Front engine, Rear wheel drive"
                                                           "\nEngine type-3.0 2JZ-GE I6(JZZ31)"
                                                           "\nHorsepower- 222 hp"
                                                           "\nTorque- 210 lb -ft"
                                                           "\nTransmission- 5 speed manual,4 or 5 speed automatic"
                                                           "\nWeight- 3,395-3,814 Ib(1,540 kg-1,730 kg)"
                                                           "\nProduction-  1991-2000"
                                                           "\nTop speed:146-156 mph"
                                                           "\n0-60:7.4 seconds")
print()
input("" + inspector + "-Interesting you chose the " + brand + " " + actual + ".")
print()
