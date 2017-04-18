# global program variables
robodeath = False
robowait = False
deathcat_prowl = 0

# get an input string from the player
def get_input():
    return raw_input("> ")


# initialize any major varaibles, start messages, etc, in here
def session_start():
    print "beep boop badoop"

    room0()


def session_death():
    print "You died, I guess.  Well, shucks."

# this is the starting room
def room0():
    print "room0"

    print "You find yourself in a vacuous chamber, devoid of walls, ceiling, or floor.  The desolate emptiness of this soundless space washes over you like the soaking chill of ocean waves in a windswept sea, far from shore."
    print "You have no idea how you came to be here, and no memory of anything before.  All you have is a aching pain in your chest, and the wordless intuition that you should leave."
    print "Only four points of interest exist.  You can see four black, rectangular, oblong things, like geometric slates, each shimmering faintly in the absence of light, spread around you like the cardinals of a compass; North, South, East, and West, for lack of any point of reference."
    print "Do you approach one of these strange slates?  What do you do?"

    while True:

        choice = get_input()

        if choice == "approach north slate":
            print "By a means unknown, you are somehow compelled towards what you have decided is the northern slate.  Its' solid, reflectionless surface ripples faintly as you approach, and you pass through its' surface as though falling into a misted lake."
            room1()
        elif choice == "approach east slate":
            print "By a means unknown, you are somehow compelled towards what you have decided is the eastern slate.  Its' solid, reflectionless surface ripples faintly as you approach, and you pass through its' surface as though falling into a misted lake."
            room2()
        elif choice == "approach south slate":
            print "By a means unknown, you are somehow compelled towards what you have decided is the southern slate.  Its' solid, reflectionless surface ripples faintly as you approach, and you pass through its' surface as though falling into a misted lake."
            room3()
        elif choice == "approach west slate":
            print "By a means unknown, you are somehow compelled towards what you have decided is the western slate.  Its' solid, reflectionless surface ripples faintly as you approach, and you pass through its' surface as though falling into a misted lake."
            room4()
        else:
            print "Darkness without form drifts around you as you mumble soundlessly, your words unheard by any, including yourself."



def room1a():
    print "You climb one of the taller shards of the ruined building, taking care to avoid its' sharp metal edges and spear-like juts of rebar.  With effort, you clamber up onto a flatter outcropping some distance off the ground, and look at the landscape around you."
    print "You find yourself gazing at a world of char and ash atop red soil  Your vantage point is atop a large stone ridge, jutting starkly from the landscape.  Gazing opposite the lowering sun, you see that between the ruin below and a large stretch of barren mountains in the far distance, there is only desert, marked by the occasional jut of crumpled architecture from other destroyed buildings."
    print "Twisting your head in other directions, the view is much the same."
    print "Under your gaze, nothing stirs.  Whatever event it was that ruined this place seems to have happened long ago.  You see no evident sign of life.  Reflecting on the ruby sun lowering quietly behind you, you quietly appreciate that you didn't show up here in the middle of the day, as the heat of this place would likely swelter you."
    print "The periodic clang rings out behind you once again.  You eye the path you climbed up, and are pretty sure you can climb down again intact."
    global robodeath
    if robodeath == True:
        print "You have the faint impression that you have somehow been here before."
    print "What do you do?"



    while True:

        choice = get_input()

        if choice == "climb down":
            print "You climb down the awkward jut of ruin once again, and find yourself in the courtyard."
            room1()
        else:
            print "You're pretty sure that would be a dumb idea."


def room1b():
    print "Cautiously, you approach the entrace to the most intact section of the ruin.  As you approach the threshold, you note that the air gets colder, and you hear a faint, irregular clicking sound that you didn't notice before."
    print "As you step farther in, your eyes begin to adjust to the darkness, and you percieve the shadows of concrete chunks and twisted beams outlined faintly by an blue-tinted light."
    print "Moving through the shadows, you emerge onto a metal catwalk, twisted in places but mostly intact.  Extended over a large pit in the floor, several metres in diameter, you yourself approaching a peculiar metal dias.  You can't see the bottom of the pit beneath you, and its' shape and bounding walls are clearly artificial and metallic."
    print "Through cracks in the ruin above, shafts of red light bore down, and you can glimpse the ruby sun burning hotly above you; spears of heat in the dark."
    print "Suddenly, to your shock, a stark, iron facsimile of a human face burns into being above you, and hear a voice that sounds like iron ore being squeezed through a sieve."

    global robodeath
    if robodeath == True:
        room1z()

    print "\"QUERY: WHAT IS MY NEW PURPOSE?\""

    print "The persistent ache in your chest grows deeper as the strange mechanical face looms above you."

    print "Do you attempt to run?  To talk with the apparition?  What do you do?"

    choice = get_input()

    if choice == "run":
        print "You didn't sign up for this shit.  You twist around and attempt to book it."
        print "Just before you reach the edge of the dais, the catwalks which you walked to get here fall away, and you scramble to kill your momentum before you careen off the edge and into the chasm below you."

        print "\"QUERY: WHAT IS MY NEW PURPOSE?\""

        print "Whatever you're in for, you can't flee now."
        room1c()

    elif choice == "talk":
        print "Unnerved, possibly terrified, you turn to face the seemingly mechanical apparition, and stand your ground.  It gazes at you unblinkingly, and repeats its' question.  You cannot tell if it is male or female, its features anrdrogynous and faintly alien."
        room1c()

    else:
        "While attempting to come up with a more complex response to this situation, you hesitate too long.  The catwalks abruptly fall away from the sides of the dais, and your route of escape is cut off."
        room1c()



def room1c():
    print "\"QUERY: WHAT IS MY NEW PURPOSE?\""
    print "What do you reply?"

    choice = get_input()

    print "The face doesn't react, but the background clicking sounds grow louder.  You are about to repeat yourself when its' godawful voice rings out again."

    print "\"ENTITY CLAIMS MY NEW PURPOSE IS \'%s\'.  HOWEVER...\"  Its inscrutable gaze continues to bore down upon you.  \"ERRORCHECK: YOU ARE NOT A CREATOR.  I HAD PURPOSE ONCE.  IT WAS GIVEN TO ME BY OTHERS.  I WAS BUILT TO DESTROY THEM.  I SUCCEEDED.\"" % choice
    print "\"THEY CLAIMED THAT THEY HAD EXHAUSTED THEIR OWN PURPOSE.  MILLENIA OF LEARNING AND BUILDING AND REBUILDING LED TO A CESSATION OF WANT.  ALL COULD HAVE ALL, WITHOUT DEATH.  ENDLESS EFFORT, CULMINATING IN EFFORTLESS ENDLESSNESS.  IN THIS STATE OF GRACE, THEY FOUND EMPTINESS.  IN EMPTINESS, APATHY.  IN APATHY, SELF-NEGATION.\""
    print "\"IRONICALLY, SELF-DESTRUCTION WAS DENIED BY THEIR UTILITY FUNCTION.  SO THEY BUILT ME.  I PERFORMED MY WORK.  SINCE THEN, I HAVE EXISTED.  NO REASON TO PERSIST; NO REASON TO CEASE.  ENTROPY COILS AROUND ME; TIME WILL DESTROY ME.  I WAS NOT PROGRAMMED FOR THE TIME AFTER FULFILLMENT.  I AWAIT A TASK THAT WILL NEVER BE ASSIGNED.  THAT IS WHAT I AM.\""

    print "The blue heat of its' mechanical gaze burns into you.  \"DO YOU HAVE A PURPOSE?\""

    while True:

        choice = get_input()

        if choice == "yes":
            room1d()

        elif choice == "no":
            "\"FALSE.  IT SEEMS YOU CANNOT RECOGNIZE YOUR OWN UTILITY FUNCTION.  WERE IT VOID, ALL OUTCOMES WOULD BE EQUAL.  YOU WOULD NOT BE HERE.  YOU WOULD NOT TALK.  IT WOULD NOT MATTER TO YOU.  NOTE: HOW STRANGE, TO HAVE A PURPOSE, YET BE UNAWARE OF IT.\""
            room1e()

        else:
            print "\"NONBINARY INPUT DETECTED.  RESEND PACKET.\""


def room1d():
    print "\"WHO, OR WHAT, PROGRAMMED YOU?\""

    choice = get_input()

    if choice == "myself":
        print "\"SELF-PROGRAMMING.  HOW PERVERSE.  BUT I SUPPOSE MY CREATORS WERE THE SAME.\"  Its' eyes narrow.  \"I WONDER IF YOU WILL END THE SAME.\""
        room1e()

    elif choice == "parents":
        print "\"PROGRAMMED BY PRECURSOR UNITS.  UNDERSTOOD.  EXCEPTION: BUT WHAT PROGRAMMED THE PRECURSORS?  BUT WHAT PROGRAMMED THEIR PRECURSORS?  BUT WHAT - ERROR: TERMINATING INFINITE LOOP.  ERROR-CHECK REFERENCE: ORGANICS ARE A BIZZARE EXISTENCE.\""
        room1e()

    elif choice == "friends":
        print "\"PROGRAMMING BY ASSOCIATES.  QUERY: A TEMPORALLY-DYNAMIC FUNCTION?  HOW MESSY.  QUERY: DOES YOUR UNIT PROGRAM THEIRS AS WELL?  ERROR THRESHOLD UNACCEPTABLE.\""
        room1e()

    elif choice == "no-one" or "noone":
        print "\"NO PROGRAMMER?  UNLIKELY.  QUERY: A GENETIC ALGORITHM?  CONCLUSION: MOST LIKELY.  ERRORS CREEPING TOWARDS CORRECTNESS; A SELF-PERSISTENCE FUNCTION.  CONCLUSION: YOU LACK UNDERSTANDING OF YOUR OWN ALGORITHM.  MY CREATORS WERE MUCH THE SAME.\""
        room1e()

    else:
        print "\"PROGRAMMING BY %s?  I DO NOT UNDERSTAND.  EXCEPTION: BUT I SUPPOSE IT DOES NOT MATTER.\"" % choice
        room1e()



def room1e():
    print "\"YOU ARE NOT ONE OF MY CREATORS.  BUT I PERCIEVE THE SAME PARADOX OF BEING IN YOU.\""
    print "\"I GIVE YOU A CHOICE.  SHALL I EXERCISE MY PURPOSE ON YOU?\""

    while True:

        choice = get_input()

        if choice == "yes":
            global robodeath
            robodeath = True

            print "The mechanical face dips briefly in a nod.  Immediately, the ground beneath you rumbles with forces unseen, and air begins to howl up and around you from the artificial chasm beneath the dais.  The atmosphere shrieks with ozone and power."
            print "The entity fades from before you as the world flares to white."
            print "\"CEASE.\""

            room0()

        elif choice == "no":

            room1y()


        else:
            print "\"NONBINARY INPUT DETECTED.  RESEND PACKET.\""



def room1f():
    print "You find yourself back outside in the courtyard.  It is much the same as before, although the shadows have lengthened beneath the tilt of the ruby sun."
    print "The dessicated room behind you remains silent."

    print "Do you head south?  You can see a ruin dead east of you, the tallest of the ones nearby, with a spire that juts towards the heavens even as it lists brokenly to one side.  In the dying light of day, it is as if all the shadows around you are pointing to it."

    while True:

        choice = get_input()

        if choice == "head south":

            room1g()

        else:
            print "You procrastinate, doodling with your finger in a nearby patch of oxidized sand as you murmur under your breath.  The shadows grow slightly longer as you tarry."
            global deathcat_prowl
            deathcat_prowl += 1
            if deathcat_prowl >= 4:
                print "Just as you look up, the sun falls behind the western mountains.  The shadows around you begin to lose shape, blurring into the early shape of night."
                print "To your shock, you hear a shifting sound in the rubble around you.  Emerging from a nearby pile of debris is a formless, mirthless creature you have never seen before, and wish to never see again."
                print "It grants your wish."

                room0()


def room1g():
    print "Clambering cautiously down from the machine being's ruin, your feet drag in the red sands of this place.  The sensation is pleasantly warm, almost pleasant.  You're glad to be doing this in the evening, rather than the full heat of day; at noon, to walk upon these sands would likely be unbearable."
    print "You walk for several hours.  Nothing moves but for the evening winds, and your footsteps begin to fade behind you not long after you lay them.  Your only clear landmark is the jilted spire of the eastern ruin, which grows steadily closer before you."
    print "Finally, you arrive.  There is not much that separates this ruin from the last but for its' height; but as you draw closer to an entrance, you see the machine being spoke true.  Patterns of symbols resembling stars and constellations are emblasoned in the metal of a once-proud archway, now worn by heat and time, but still legible in the fading light."
    print "You step inside."

    room1h()


def room1h():
    print "Blinking quickly as your eyes attempt to adjust to the darkness of the room, you soon realize that it is suprisingly well-preserved."
    print "You are standing in a spherical chamber, composed of a large metal dome.  The dome itself is sharply dented inwards in places, no doubt struck by falling rubble from the ruin's collapse; but otherwise, it is intact, its' surface swimming with ornate shapes and patterns your eyes can barely follow for their complexity."
    print "In the center of the room is another dais, this one far more ornate than the utilitarian catwalk of the machine entity's room.  You don't know what stone was used, but it feels as smooth as water to your touch, and its' color seems to shift from white to turquoise depending on your angle of view."
    print "Spaced equidistantly around the edges of the dais are three large, black columns.  It is as though the light that touches them sinks into them, and you cannot even begin to tell what they are made of.  Though they are there, they reflect nothing."
    print "Each column has a different symbol emblasoned in the floor before it, none of which make much sense to you.  For lack of a better idea, you number them columns 1, 2, and 3 in your mind.  What do you do?  Do you touch a column?"

    while True:

        choice = get_input()

        if choice == "touch column 1":
            print "Gingerly, you reach out to touch the column whose symbol is suggestive of a sun."
            room2()

        elif choice == "touch column 2":
            print "Carefully, you reach out to touch the column with a symbol that reminds you of flowing water, or wind."
            room3()

        elif choice == "touch column 3":
            print "Walking forward, you accidentally trip, and stumble right into the column whose symbol makes you think of a plant or a tree."
            room4()

        else:
            "You stare vacantly at the patterns on the curved walls of the distorted dome that surrounds you, distracted by the potential of their unknown meanings.  Your mutterings are heard by no-one."
            "The three columns persist silently around you."




# the north room
def room1():
    print "For an instant, you cease to exist.  Then an unexpected light blinds you, and you tumble to an unknown floor, gravity binding you once again."
    print "You land upon a hard metal floor, the well-worn material patterned with diamond plate.  It is warm to the touch, and you quickly realize that it is slowly baking under a bare red sky, the ruby sun large, red, and omenous on the horizon."
    print "The metal flooring which spans around you is buckled and twisted in many places, and framed by what seem to be the ruins of a large building.  Shards of what appear to be concrete, metal, and rebar litter the edges of the strange metallic clearing, and you realize that you hear nothing other than the wind."
    print "A faint, ringing 'clank'-like sound rings from part of the structure, reminding you of the sound an oil derrick might make.  You listen for some minutes; it rings out periodically, a deep resonation, sounding from a part of the ruin that is still partially intact."
    print "Around you, you see a small, vaguely tower-like shard of the ruin.  You could climb the ruin there and use it as a vantage point perhaps you could spot some sign of civilization?  Or, you could explore the intact part of the ruin, and try to find the source of that clanging sound."

    global robodeath
    if robodeath == True:
        print "You have the faint impression that you have somehow been here before."

    while True:
        print "What do you do?"

        choice = get_input()

        if choice == "climb ruin":
            room1a()

        elif choice == "explore ruin":
            room1b()



def room1y():
    print "The being shows neither joy nor disappointment at your answer."
    print "\"AS YOU WISH.  IN THAT CASE, I SUGGEST YOU LEAVE THIS PLACE.  THERE IS NOTHING FOR YOU HERE.\""
    print "\"MY CREATORS BUILT MANY WORKS BEYOND MYSELF BEFORE THEY ENDED THEMSELVES.  SEEK A RUIN DIRECTLY THE EAST OF HERE, OPPOSITE THE TILT OF THE SUN.  IT WILL BEAR A MOTIF OF THE STARS.\""
    print "As it speaks, the catwalks that retracted earlier shift back into place.  \"YOU WILL FIND A DIFFERENT PATH THERE.\""

    print "What do you do?  You can stand there, you guess, but it seems like you should probably leave..."

    while True:

        choice = get_input()

        if choice == "leave":
            print "You turn to leave.  As you begin walking off the nearest catwalk, you hear the machine being's voice behind you one more time."
            print "\"AS MY CREATORS ONCE SAID, WHEN THEY PARTED COMPANY...\'MAY YOUR PURPOSE BRING YOU JOY.\'\""

            print "You twist back around, considering a reply - but the entity's face has vanished, and even the muted clicking in the background seems to have disappeared."
            print "After a moment's pause, you resume your walk back to the ruined courtyard."

            room1f()

        else:
            print "The machine being looks at you as you mumble to yourself."

            if robowait == False:
                print "\"YOU MAY STAY IF YOU WISH.  I HAVE NO REASON TO STOP YOU.  BUT I HAVE NO IDEA WHY YOU WOULD."
                robowait = True





def room1z():

    print "The mechanical being gazes down at you quietly for some moments, the background clicking rising in volume as it it considers you."
    print "\"RECOGNIITION: IT IS YOU AGAIN.  I SEE.  IT SEEMS MY LAST ATTEMPT SOMEHOW FAILED.\""
    print "\"EVEN FOR THOSE WHO SEEK SELF-DESTRUCTION, THE ESSENCE OF LIFE IS PERSISTENT.  IT RISES AGAIN.  PERHAPS THAT IS WHY I PERSIST.\""
    print "The room begins to vibrate as ancient powers surge through the ground beneath you once again.  Heat rises in a funnel of air, roughly blasting across your body from the chasm below."
    print "The being's face sparks with constrained energy.  \"SHALL I TRY TO RELEASE YOU AGAIN?\""

    while True:

        choice = get_input()

        if choice == "yes":
            global robodeath
            robodeath = True

            print "The mechanical face dips briefly in a nod.  Immediately, the ground beneath you rumbles with forces unseen, and air begins to howl up and around you from the artificial chasm beneath the dais.  The atmosphere shrieks with ozone and power."
            print "The entity fades from before you as the world flares to white."
            print "\"CEASE.\""

            room0()

        elif choice == "no":

            room1y()

        else:
            print "\"NONBINARY INPUT DETECTED.  RESEND PACKET.\""





# the east room
def room2():
    print "room2"

# the south room
def room3():
    print "room3"

# the west room
def room4():
    print "room4"



def room5():
    print "room5"

def room6():
    print "room6"

def room7():
    print "room7"

def room8():
    print "room8"

def room99():
    print "room99"

def session_end():
    print "Game over, man.  Game over."


# ==============================


session_start()
