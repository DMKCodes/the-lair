"""

This module started as a bunch of dictionaries, but I changed them to lists and tuples as I learned more about data types.  I'm not sure why I never changed the file name, but here we are.

These "dictionaries" contain the bulk of the game text, or storytelling, a player will see during the game.  They are iterated over with loops and incrementing variables to present the right strings of text at the right moments.

Most of these are tuples as there is no reason for their contents to be mutable.  A couple are lists because I needed to use the pop and append methods to reorder the contents dynamically.

"""

room_descriptions = (
    "You enter a room with a smooth, natural stone floor.  Etched into one wall is the memorial, 'Doug died here.  Damn this place.'  Nearby, a skeleton sits slumped in a chair.",
    "The walls of this room were once painted blue, though most of the paint has faded or flaked away.  The floor is inlaid with brightly-colored tiles.",
    "A fetid stench assaults your senses as you enter the room.  It was once some sort of indoor garden, or perhaps a laboratory.  Flora in varying stages of decay litters the floor and the walls are crisscrossed with moss and vines.",
    "This must have been a training grounds.  The far wall is chalked with archery targets, and splintered wooden training dummies stare blankly from their posts.",
    "Fighting occurred here.  Recently, you suspect.  The chamber's low ceiling is spattered with blood, and deep gouges - like those carved by immense talons - etch the walls and floor.  In one corner, you find a curious pile of red feathers.",
    "You enter some kind of ritual chamber.  A raised dais sits alone in the center of the room, carved with faintly-glowing runes in a language you can't comprehend.",
    "This room sees frequent use, you can tell.  Dozens of round pegs poke from the wall nearest you.  From a few of them hang sets of black robes, feathered cloaks, and unusual masks with protruding, metal beaks.",
    "A bathing chamber meets you next.  Several stone basins, each large enough to accommodate several bathers, are set into the floor.  You eagerly twist the spigots, suddenly - painfully - aware of your thirst, but all that emerges is a thick, brownish sludge.",
    "This room is unremarkable, save for a threadbare tapestry hung on one wall.  The dye is almost entirely faded, but you can make out a ring of dark figures knelt in prayer around an immense, winged creature.",
    "You come upon another row of cells, each identical to the one in which you awoke.  One cell is covered in crudely drawn, profane symbols.  From the stench and appearance, it seems blood and feces were used to make the drawings, and not too recently.",
    "You step carefully into the room, avoiding shards of smashed ceramic jars.  It is otherwise unremarkable.",
    "The walls of this room glitter with a rainbow of colors.  On closer inspection, you can see that the stone is filled with flakes of mica, each catching and reflecting the light of a guttering torch.",
    "Rats scatter as you enter the room.  You can see they were feasting on the recent remains of another captive.  You think to catch and cook one, but decide against it.  You're not that desperate... yet.",
    "You enter what must have been a torture chamber.  Thick manacles dangle from metal spikes along one wall.  The butchered body of a goblin dangles from a hook in the center of the room.  Its chest bears a series of foreign symbols, carved crudely into the skin with a blade.",
    "A series of floor-to-ceiling bookshelves line the walls of this room.  A brief, unenthusiastic search yields a faded scroll, but it crumbles to dust between your fingers.",
    "The wide chamber is unusually clean, void of any dirt, dust, or debris.  In one corner is a huge pile of fabric - mostly blankets and clothing - with a hollow in its center.  It reminds you of a nest.",
    "Behind the splintered remains of a large table, you find two corpses locked in an eternal embrace.  The wall beside them is etched with rows of small grooves, perhaps a count of days... or years.",
    "You enter a crypt.  Rectangular recesses line the walls, most of them filled with skeletons, arms folded in the repose of death.  A sheaf of parchment on a small desk is filled with scribblings of what appear to be names and dates, though you cannot understand the language.",
    "Salted meats hang from the ceiling of this room, and the walls are lined with shelves of pungent spices.  You eat greedily and fill your pack, choosing not to question the origin of the gamey meat.",
    "This chamber appears to be completely empty. The walls are made of natural stone chiselled flat and straight. The floor and ceiling are both set with alternating black and red tiles.",
    "The walls of this chamber are roughly hewn. In the centre of the room is a wide pool with creeper vines growing around the edges. The water in the pool is still and murky.",
    "This wood-panelled chamber is dominated by an eight-foot iron drinking fountain, decorated with carvings of feathered creatures. The liquid in the fountain appears to be water. On the bottom of the pool you can see a scattering of tarnished coins.",
    "The entry way to this chamber radiates waves of heat. Inside you see a smoldering brick furnace with a narrow chimney set into the ceiling. Ingots of iron, steel and other metals line a side table to your right.",
    "This chamber is lit only by your smoking torch. From the doorway, you can see rows of unoccupied wooden bunks laid with straw and dirty blankets.  The far wall of the room is not visible beyond your torchlight.",
    "This dark stone chamber filled with wooden tables, chairs and bunks filled with straw. The air here is unpleasant and reeks of stale sweat.",
    "This room was once a feasting hall.  A huge, rectangular stone table dominates the center, its surface scattered with tiny bones, broken plates, and tarnished cutlery.",
    "You enter a low tunnel, dropping to your hands and knees to crawl forward.  The ground here is scattered with small bones that crunch into dust beneath your weight.  You finally straighten in a small room on the other side."
)

room_intros = (
    "A shadow approaches, growing larger in the flickering torchlight.",
    "You can't see any enemies, but something about this room seems strange...",
    "This seems like a safe enough place for a break.",
    (
        "A mysterious man in a hooded cloak approaches.  His palms are raised in a gesture of peace, but his face lurks in impenetrable shadow.  On his shoulder, curiously, perches a rooster, which eyes you with an unsettling - and decidedly unroosterlike - intellect.\n",
        "'Fear not, traveler.  We are trapped here, same as you.  We intend you no harm.'\n",
        "To your astonishment, it is the rooster speaking, not the man.  You chafe against the sharp rasp of its voice. \n",
        "'I am Björn,' the rooster continues.  'I am a merchant by trade, doing my part to help other captives escape this cursed place.  Come, view my wares and see what might aid you in your battle for freedom.'\n",
        "Still speechless, you watch as the rooster clenches its talons on the man's shoulder.  As if activated, the man's arms grasp the folds of his cloak and swing wide, revealing an array of items.\n"
    ),
    (
        "At the far end of the room, you hear a ruffling of feathers.\n",
        "'We truly have to stop meeting like this,' Björn clucks sardonically, emerging from the shadows.\n",
        "Predictably, the rooster's human companion swings wide his cloak, and you see that its contents have changed.\n"
    ),
    "Your search uncovers a large chest.  You break the lock and investigate its contents."
)

rooms = [
    "Fight",
    "Event",
    "Camp",
    "Trade",
    "Treasure"
]

companions = [
    "puppy",
    "owlet",
    "kitten",
    "dragonling",
    "frog",
    "chomps down with its sharp teeth,",
    "pecks with its sharp beak,",
    "swipes with its sharp claws,",
    "sneezes, launching a fist-sized ball of flame,",
    "spits a stream of acidic venom,"
]

awaken_text = (
    "You slowly regain consciousness.  Your vision is blurry and the back of your head throbs with pain.  You reach up to touch the wound, and your fingers come back sticky with blood.  All your belongings are missing.  You're naked, save for a pair of ragged, dirt-stained breeches.  Where are you?  How did you get here... ?",
    "You realize you're in a dungeon.  The room you're in is tiny, no wider than your armspan.  The walls are rough-hewn stone, void of windows or ornamentation.  If not for the distant flicker of torchlight through the thick bars of the cell, you would be in total darkness.",
    "You turn and, with a strangled cry, come face to face with your 'cellmate' - a skeleton, slumped against the wall, its yellowed skull locked forever in a macabre grin.",
    "Once the shock has worn off, you struggle to your feet.  Your bones ache.  In the torchlight, you can see your arms and torso are covered in angry red welts and purple bruises.  The situation seems hopeless.",
    "But you will not succumb to despair.  You stagger over to inspect the skeleton.  To your fortune, the ill-fated prisoner had not been similarly stripped of their belongings.  Your search yields a rusted dagger, a mysterious Glimmering Trinket, and a handful of coins.  Uttering a quick oath to your god, you extricate the skeleton from its time-worn leather armor and slip it on.  If nothing else, at least now you can put up a fight.",
    "You approach the door of the cell and, to your surprise, it swings open with a screech of metal.  A long corridor extends before you, lit periodically by low-burning torches.  At the far end is another door.  You listen, but if there are any guards afoot, they're not making their presence known.  You grab a torch with one hand and clench your dagger in the other.  Gathering your courage, you venture into the dungeon..."
)

madman_text_one = (
    "You come upon a man sitting in a chair.  He is shirtless, filthy, and skeletally thin, with a mane of wild gray hair.  He looks up at you, and you see madness in his eyes.",
    "You try to talk to him.  'Are you okay, friend'?",
    "'Not okay!  Not real!  SQUAWK!  You're not real... am I real?  Heeheehee.  No escape, not real, not okay...'",
    "The man seems to look straight through you.  There is no getting through to him.",  "Disconcerted, you leave him to his insane ramblings."
)

madman_text_two = (
    "You are greeted by a familiar face.  The crazy, gray-haired man approaches you warily.  This time, there seems to be a hint of clarity in his gaze.",
    "'So you are real,' the man says.  'Can't be sure in this place.  I've found if you act crazy enough, the cultists tend to leave you alone.'",
    "'Cultists?'",
    "'You know, the ones with the masks.  This place is crawling with them.  They worship The Great Beaked One, whoever - or whatever - that might be.'",
    "'Do you know how to get out of here?' you ask.",
    "'Been trying for YEARS,' the man says.  'Never once sniffed the exit.  I forgot the feel of fresh air a long, long time ago.  But I'm surviving well enough I suppose.  Pilfer a loaf of bread rarely enough, the cultists tend not to notice.  Stay quiet, know when to hide, you'll be all right.'",
    "'I mean to escape this prison,' you say flatly.",
    "The man cackles.  'That's what they all say.  Who knows, maybe you'll be the first to pull it off.'  He leans in conspiratorially.  'Just in case you are real, I'll let you in on a little secret.'",
    "I've worked out a bit of that language they cooked up, the one you must have seen scrawled all over this place.  The cultists, that is.  There's a phrase, a-- a spell! they say can weaken this Great Beaked One of theirs.  GALLUS... SQUAWK... GALLIFORMES, heehee!'  His speech ends in a screeching, birdlike voice.",
    "'Gallus... what now?'",
    "'Not real, not real, not real.'  The man's eyes cloud over again and he ambles off, seemingly unaware of your existence.  With a resigned shrug, you decide to move on.",
)

madman_text_three = "For a moment, you think you can hear a familiar, rambling voice. 'SQUAWK, gallus, heeheehee, not real, not real, GALLIFORMES, heehee...'  Then it's gone."

boss_text = (
    "You enter a cavernous chamber of carved stone, far larger than any you've traveled through thus far.  It reminds you of a church or temple - from in front of your feet, an ornate rug spans the length and breadth of a central aisle, perhaps eight feet across and many times longer than that.  Flanking the aisle, crowding row after row of stone benches, are hundreds of silent figures, each clad in the familiar dark robes, feathered cloaks, and beaked masks.",
    "You expect to be swarmed instantly.  Every muscle in your body, every instinct in your battle-honed mind, screams at you to run.  But there is no movement among the gathered cultists, not so much as a whisper of sound, and you notice that their attention is fixed toward the far end of the chamber.  Only then do you notice Björn.",
    "The rooster's faceless companion sits on a magnificent throne, fashioned from obsidian and studded with dozens of gems - glittering rubies, emeralds, sapphires, and diamonds, each at least the size of your fist and immaculate in cut and quality.  In the man's lap nestles Björn.  And behind the throne, you see with a shock, is an open door.  You can see... daylight! filtering into the chamber.",
    "'You should not be here,' Björn rasps, dragging your attention away from the dungeon's exit.  'None escape from Björn's Lair.'",
    "'NONE ESCAPE!'  The cacophony of the cultists' voices shouting in unison catches you off guard, and you rock back on your heels.  All at once, the puzzle pieces come together, revealing the horrible truth of your captivity - the warning signs, encountered at every turn and which your beleaguered mind had been unable, or unwilling, to work out, now making sense.  It was Björn all along.",
    "But you have grown stronger through your trials in this accursed place, you know.  You cannot allow Björn's cultists to keep you from escaping.  Not with your salvation finally within reach.  And Björn... well, despite the trickery he must have employed to enthrall his congregation of followers, he is but a mere talking rooster, and poses little threat.  Emboldened, you stride forward and draw your weapon.",
    "'I do,' you say simply.  Your words are met with the metallic *schwing* of the cultists' weapons leaving their scabbards.  If you must fight your way through them all, you decide, so be it.",
    "'No!' Björn screeches.  'Stand down.  This one is mine.'  The faceless man starts to rise to his feet, holding the rooster high.  You barely suppress a bark of laughter at the image of engaging in mortal combat with a rooster.  But your good humor vanishes as Björn begins to change.",
    "With audible cracks of bone and sinew splintering and expanding, the rooster grows before your astonished eyes.  Ten times bigger... twenty... fifty... a hundred.  The cultists nearest to its tree-trunk-like legs, now sporting vicious, hooked talons each as long as you are tall, scramble to make room as the transformed creature continues to grow.  In mere moments, a monstrous, rooster-like beast stands before the throne, its jaundiced, bloodshot eyes promising your doom.",
    "You think to run, to return to the dungeon and hide, to remain there in perpetuity as Björn's macabre plaything, like a fieldmouse, scurrying into the nearest hole as the shadow of a great hawk falls over you.  But if you do, you know, Björn's cultists will continue to kidnap and imprison innocent folk.  The corpses you uncovered in your gruesome journey through the lair will continue to multiply.  Wives will become widows, children will be orphaned, and Björn's perverse power will continue to grow.",
    "No.  Fleeing is not an option.",
    "You present your weapon and steady your resolve.  'Come then, foul beast, and meet your hellish maker.'",
    "With a thunderous SQUAWK and a beating of wings that buffets a score of cultists from their feet, your final fight ensues."
)

boss_text_incantation = (
    "As the beast nears, you suddenly remember the wild, gray-haired man's words.  A spell that can weaken the beast...",
    "But what were the words..."
)

boss_text_incantation_opts = (
    "(1) Gannis ganniformes",
    "(2) Gallus galliformes",
    "(3) Gabbis gammiformes",
)

outro_text = "You emerge blinking furiously into the sunlight of the surface.  As your eyes adjust, you can see that you stand on a narrow platform carved from the face of a steep cliff.  A lush valley extends before you, dotted with small villages.  To your left, precarious stairs lead down the hundreds of feet to the valley floor.  You pause to savor the brisk wind on your skin, drawing greedy lungfuls of clean air.  Then you begin the long journey home."