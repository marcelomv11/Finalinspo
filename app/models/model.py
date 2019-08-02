import random

Ambitious = [ "Shoutout to the girls who put in major work. Who are up early ass hell for school/work. Girls that study. Grind. Who persevere & prioritize self worth/lov. Who rise above & hold it down even when they're falling apart, to the girls whopush harder.", "I used to think going to sleep late was cool. Till I realized wakin up early was the real boss shit.", "if you look at people in your circle and don't get inspired, then you don't have a circle, you have a cage", "shout out to everyone making progress that no one recognize", "Don't limit your challlenges. Challenge your limits!", "Yes it is going to be hard but it's going to be worth it!", "I need to go way harder. I'm not satisfied"
    ]
Angry = [ "Speak when you are angry and you'll make the best speech you'll ever REGRET!!!", "Never let your emotions overpower your intelligence!!!", "Don't do something permanentely stupid just because you're temporarily upset!!", "Anger dosen't solve anything. It builds nothing, but it can destroy everything.", "You will not be punished for your anger, you will be punished by your anger."]

Sad = [ "Be strong because things will get better. It maybe stormy now but it never rains forever! ;)", "You are not allowed to let sadness ruin you. ;)", "It's not about forcing sadness it's about not leting sadness win. ;)", "Breathe it's only a bad day not a bad life. ;)", "I was sad but then I went beast mode! ;)", ]

Happy = [ "Being happy NEVER goes out of style. :)", "Happiness is letting go of what you think your life is supposed to be. :)", "It's fun to be happy. :)", "People look at you as a role model when you happy. :)","Happiness never decreases by being shared. :)" ]

Woke = [ "It's not the world that's cruel. It's the people in it.", "Life is not a problem to be solved, but a reality to be experienced.", "Dead people receive more flowers than the living ones because regret is stronger than gratitude.", "Listen to your possibilites not your insecurities", "OUTSIDERS know all your business from INSIDERS. ", "Be forgiving, Be understanding, But don't be a fool.", "Once you've matured you realize SILENCE is more powerful then proving a point." ]

Scared = [ "Sometimes what you are most afraid of doing is the very thing that will set you free", "Don't be afraid to fail. Be afraid not to try", "It is okay to be scared because that means you are about to do something very very brave" ]

Surprised = ["Time changes everything except somethig within us which is always surprised by change", "Face what you think you believe and you will be surprised", "To be surprised, to wonder, is to begin to understand"]

Disgust = ["The greatest pleasures are only narrowly separated from disgust", "Disgust and resolve are two of the greatest things that lead to change", "Disgust is the most appropriate response to most situations"]

Confused = ["If I look confused it is because I am thinkning", "Right now, I'm stuck between what if, what might, what could have, and what never will and all I want to known is what actuallly is", "I don't think people understand how stressful how stressful it is to explain what's going on in your head when you don't even understand it yourself."]

Heartbroken = ["I am happy, hurting and healing at the same time. Don't ask how I'm doing it because I don't know, but i'm doing it and I'm so proud of myself", "The more chances you give someone to hurt you the less respect they'll start to have for you","A broken heart is just the growing pains necessary so that you can love more completely when the real thing comes along. They'll take advantage of your forgiveness. They won't be afraid to lose you because they think you will never walk away. Never let a person get comfortable with disrespecting you","Friendly reminder: Do not check up on the toxic person you left, don't check their socials, don't hit them up to see how they're doing. Your peace of mind is too important to get wrapped up up in it."]

random.shuffle(Ambitious)
random.shuffle(Sad)
random.shuffle(Angry)
random.shuffle(Happy)
random.shuffle(Woke)
random.shuffle(Scared)
random.shuffle(Surprised)
random.shuffle(Disgust)
random.shuffle(Confused)
random.shuffle(Heartbroken)




    


# random.shuffle(Ambitious)

# random.shuffle(Sad)
# random.shuffle(Angry)
# random.shuffle(Happy)
# random.shuffle(Woke)
# random.shuffle(Scared)


# def submit_emotion(mood):
#     if mood == "Happy":
#         return "Happy quote"
    


def find_quote(mood): 
    if mood.capitalize() == "Ambitious":
        random.shuffle(Ambitious)
        one_quote = Ambitious[0]
        return one_quote
    elif mood.capitalize() == "Sad":
        random.shuffle(Sad)
        one_quote = Sad[0]
        return one_quote
    elif mood.capitalize() == "Happy":
        random.shuffle(Happy)
        one_quote = Happy[0]
        return one_quote
    elif mood.capitalize() == "Angry":
        random.shuffle(Angry)
        one_quote = Angry[0]
        return one_quote
    elif mood.capitalize() == "Woke":
        random.shuffle(Woke)
        one_quote = Woke[0]
        return one_quote
    elif mood.capitalize() == "Scared":
        random.shuffle(Scared)
        one_quote = Scared[0]
        return one_quote
    elif mood.capitalize() == "Surprised":
        random.shuffle(Surprised)
        one_quote = Surprised[0]
        return one_quote
    elif mood.capitalize() == "Disgust":
        random.shuffle(Disgust)
        one_quote = Disgust[0]
        return one_quote
    elif mood.capitalize() == "Confused":
        random.shuffle(Confused)
        one_quote = Confused[0]
        return one_quote
    elif mood.capitalize() == "Heartbroken":
        random.shuffle(Heartbroken)
        one_quote = Heartbroken[0]
        return one_quote
        
        
    else:
        return "Sorry Try Again!"
    return find_quote(mood)


def color(mood):
    if mood.capitalize() == "Happy":
        mood_color = "yellow lighten-4"
        return mood_color
    elif mood.capitalize() == "Sad":
        mood_color = "blue lighten-5"
        return mood_color
    elif mood.capitalize() == "Angry":
        mood_color = "green lighten-4"
        return mood_color
    elif mood.capitalize() == "Ambitious":
        mood_color = "pink lighten-4"
        return mood_color
    if mood.capitalize() == "Woke":
        mood_color = "red lighten-4"
        return mood_color
    if mood.capitalize() == "Scared":
        mood_color = "purple lighten-4"
        return mood_color
    if mood.capitalize() == "Surprised":
        mood_color = "yellow lighten-4"
        return mood_color
    if mood.capitalize() == "Disgust":
        mood_color = "blue lighten-4"
        return mood_color
    if mood.capitalize() == "Confused":
        mood_color = " lime accent-2"
        return mood_color
    if mood.capitalize() == "Heartbroken":
        mood_color = " red lighten-4"
        return mood_color
        
        
        
    
    
    

def find_pointsq1(answer):
    if answer == "q1-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q1-a2":
        pointcounter = 0
        return pointcounter
    if answer == "q1-a3":
        pointcounter = 2
        return pointcounter
    if answer == "q1-a4":
        pointcounter = 1
        return pointcounter  


def find_pointsq2(answer):
    if answer == "q2-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q2-a2":
        pointcounter = 2
        return pointcounter
    if answer == "q2-a3":
        pointcounter = 2
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter
        
def find_pointsq3(answer):
    if answer == "q3-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q3-a2":
        pointcounter = 2
        return pointcounter
    if answer == "q3-a3":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 0
        return pointcounter

def find_pointsq4(answer):
    if answer == "q4-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q4-a2":
        pointcounter = 0
        return pointcounter
    if answer == "q4-a3":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 0
        return pointcounter
 
def find_pointsq5(answer):
    if answer == "q5-a1":
        pointcounter = 1
        return pointcounter
    if answer == "q5-a2":
        pointcounter = 2
        return pointcounter
    if answer == "q5-a3":
        pointcounter = 0
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter  
 
def find_pointsq6(answer):
    if answer == "q6-a1":
        pointcounter = 1
        return pointcounter
    if answer == "q6-a2":
        pointcounter = 2
        return pointcounter
    if answer == "q6-a3":
        pointcounter = 0
        return pointcounter
    else:
        pointcounter = 0
        return pointcounter   

def find_pointsq7(answer):
    if answer == "q7-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q7-a2":
        pointcounter = 0
        return pointcounter
    if answer == "q7-a3":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter   
  
def find_pointsq8(answer):
    if answer == "q8-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q8-a2":
        pointcounter = 2
        return pointcounter
    if answer == "q8-a3":
        pointcounter = 0
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter  

def find_pointsq9(answer):
    if answer == "q9-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q9-a2":
        pointcounter = 1
        return pointcounter
    if answer == "q9-a3":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter  

def find_pointsq10(answer):
    if answer == "q10-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q10-a2":
        pointcounter = 0
        return pointcounter
    if answer == "q10-a3":
        pointcounter = 2
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter  

from app import app
from flask import render_template, request
from app.models import model, formopener

def depression_suggestion(total_points):
    if total_points >= 15: 
        return ("Your quality of life may not be the happiest. Try appreciating the little things in life and enjoying the gift of life")
      
    elif total_points > 8 and total_points <= 14:
        return("Your quality of life is neither too content nor too glum. There is some possiblity that you can have a more postive outlook on life.")
    else:
        return("You are a very happy person. Keep radiating your positivity out into the world!")
    



