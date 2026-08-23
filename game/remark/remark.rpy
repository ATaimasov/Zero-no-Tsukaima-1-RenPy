# ============================================================
# БОНУСНАЯ ГЛАВА
# РЕМАРКА
# ============================================================

# ------------------------------------------------------------
# ИЗОБРАЖЕНИЯ
# ------------------------------------------------------------

image cr1 = "../remark/cr1.webp"
image cr2 = "../remark/cr2.webp"
image cr3 = "../remark/cr3.webp"
image cr4 = "../remark/cr4.webp"
image cr5 = "../remark/cr5.webp"

image dead_face = "../remark/pics/dead_face.webp"
image oh_my = "../remark/pics/oh_my.webp"
image press_button = "../remark/pics/press_button.webp"
image rage = "../remark/pics/rage.webp"
image rainbow = "../remark/pics/rainbow.webp"

image halkeginia_online = "../remark/pics/halkeginia_online.webp"
image halkeginia_online_mini = "../remark/pics/halkeginia_online_mini.webp"

image think = "../remark/pics/think.webp"

image louise_gm = "../remark/pics/louise_gm.webp"
image enjoy = "../remark/pics/enjoy.webp"
image hacker = "../remark/pics/hacker.webp"
image zaputalsa = "../remark/pics/zaputalsa.webp"
image models = "../remark/pics/models.webp"
image models_koikatsu = "../remark/pics/models_koikatsu.webp"
image tiff = "../remark/pics/tiff.webp"
image durka = "../remark/pics/durka.webp"
image slonyara = "../remark/pics/slonyara.webp"
image sobranie = "../remark/pics/sobranie.webp"
image mnimost = "../remark/pics/mnimost.webp"
image mnimost2 = "../remark/pics/mnimost2.webp"
image nu_naher = "../remark/pics/nu_naher.webp"
image patrik = "../remark/pics/patrik.webp"
image epic = "../remark/pics/epic.webp"
image respect = "../remark/pics/respect.webp"
image gorin = "../remark/pics/gorin.webp"
image python = "../remark/pics/python.webp"
image yyy = "../remark/pics/yyy.webp"
image bund = "../remark/pics/bund.webp"
image small = "../remark/pics/small.webp"
image okak = "../remark/pics/okak.webp"
image dich = "../remark/pics/dich.webp"
image drawing = "../remark/pics/drawing.webp"
image drawing2 = "../remark/pics/drawing2.webp"
image pending = "../remark/pics/pending.webp"
image dog = "../remark/pics/dog.webp"
image pizdech = "../remark/pics/pizdech.webp"
image tinkoff = "../remark/pics/tinkoff.webp"
image bonk = "../remark/pics/bonk.webp"
image js = "../remark/pics/js.webp"
image monkey = "../remark/pics/monkey.webp"


image alex = "../remark/pics/alex.webp"
image nobory = "../remark/pics/nobory.webp"

image l_run00 = "../remark/pics/l_run00.webp"
image l_run01 = "../remark/pics/l_run01.webp"
image l_run02 = "../remark/pics/l_run02.webp"
image l_run03 = "../remark/pics/l_run03.webp"
image l_run04 = "../remark/pics/l_run04.webp"
image l_run = Animation(
    "l_run00", 0.2,
    "l_run01", 0.2,
    "l_run02", 0.2,
    "l_run03", 0.2,
    "l_run04", 0.2,
)

image pepit0 = "../remark/pics/pepit0.webp"
image pepit1 = "../remark/pics/pepit1.webp"
image pepit2 = "../remark/pics/pepit2.webp"
image pepit3 = "../remark/pics/pepit3.webp"
image pepit4 = "../remark/pics/pepit4.webp"
image pepit5 = "../remark/pics/pepit5.webp"
image pepit = Animation(
    "pepit0", 0.2,
    "pepit1", 0.2,
    "pepit2", 0.2,
    "pepit3", 0.2,
    "pepit4", 0.2,
    "pepit5", 0.2,
)

# ------------------------------------------------------------
# ЗВУКИ
# ------------------------------------------------------------

label show_hacker:
    show hacker at Position(xpos=1000, ypos=500)
    play sound hacker loop
    return
label hide_hacker:
    hide hacker
    stop sound fadeout 0.5
    return

define audio.keyboard = "remark/sfx/keyboard.mp3"
define audio.dramatik = "remark/sfx/dramatik.mp3"
define audio.oh_my = "remark/sfx/oh_my.mp3"
define audio.wink = "remark/sfx/wink.ogg"
define audio.glass = "remark/sfx/glass.mp3"
define audio.blyat = "remark/sfx/blyat.mp3"
define audio.nu_naher = "remark/sfx/nu_naher.ogg"
define audio.thats_me = "remark/sfx/thats_me.ogg"
define audio.win = "remark/sfx/win.mp3"
define audio.win2 = "remark/sfx/win2.mp3"
define audio.teeth = "remark/sfx/teeth.mp3"
define audio.bonk = "remark/sfx/bonk.mp3"
define audio.nux = "remark/sfx/nux.mp3"
define audio.oh_shit = "remark/sfx/oh_shit.mp3"
define audio.suspence = "remark/sfx/suspence.mp3"
define audio.suspence2 = "remark/sfx/suspence2.mp3"
define audio.bruh = "remark/sfx/bruh.mp3"
define audio.ou_eee = "remark/sfx/ou_eee.mp3"
define audio.danger = "remark/sfx/danger.mp3"
define audio.huh = "remark/sfx/huh.mp3"
define audio.epic_sax = "remark/sfx/epic_sax.mp3"
define audio.wasted = "remark/sfx/wasted.mp3"
define audio.think = "remark/sfx/think.mp3"
define audio.hacker = "remark/sfx/hacker.mp3"
define audio.nostalgy = "remark/sfx/nostalgy.ogg"
define audio.cheer = "remark/sfx/cheer.mp3"
define audio.cheer3 = "remark/sfx/cheer3.mp3"
define audio.cheer0 = "remark/sfx/cheer0.mp3"
define audio.error = "remark/sfx/error.mp3"

# free cheers!!!
define audio.cheer2 = "remark/sfx/cheer2.mp3"

# ------------------------------------------------------------
# ПЕРСОНАЖИ
# ------------------------------------------------------------

define tms = Character(None, color="#00000000")
define th_tms = Character(None, color="#00000000",  what_italic=True,
    what_color="#641e2a",
    window_style='thought_window')


screen japanese_film_overlay():

    add Solid("#6b4a2a") alpha 0.12

    add Solid("#000000") alpha 0.08

    # горизонтальные полосы плёнки
    for y in range(0, 1080, 6):
        add Solid("#000000") xpos 0 ypos y xsize config.screen_width ysize 1 alpha 0.08


# ============================================================
# ВХОД В БОНУСНУЮ ГЛАВУ
# ============================================================

label remark:
    stop music fadeout 1.0
    play sound keyboard loop
    scene black
    centered "{size=+14}{color=#ffffff}...{/color}{/size}"
    pause(1)
    

    $ fade_fx("cr1", bg_position="default")

    # ФОН: тёмная комната / рабочее место

    pause(1.0)

    th_tms "Tired...{#r}"

    th_tms "How long have I been sitting here already?{#r}"

    th_tms "Good question.{#r}"

    pause(0.5)

    # ИЗОБРАЖЕНИЕ: уставший переводчик за компьютером
    $ dissolve_fx("cr2", bg_position="default")

    tms "You know...{#r}"

    tms "I never actually planned to do this.{#r}"

    tms "I wasn't planning to translate an old Japanese game.{#r}"

    tms "I wasn't planning to dig through PlayStation 2 files.{#r}"

    tms "I wasn't planning to unpack thousands of audio files.{#r}"

    tms "And I certainly wasn't planning to spend sleepless nights doing a tedious line-by-line translation.{#r}"

    th_tms "Hello, four hours of sleep{#r}"
    "(；´д｀)ゞ"

    show dead_face at Position(xpos=1000, ypos=500) with dissolve

    tms "..."

    hide dead_face with dissolve
    pause(0.7)

    # ИЗОБРАЖЕНИЕ: рабочий стол / куча файлов / ночная работа
    # ЗВУК: клавиатура

    tms "But somehow, that's how it turned out.{#r}"

    pause(0.5)

    tms "So I decided to leave a little remark here.{#r}"

    tms "From me.{#r}"

    tms "The creator of the remaster.{#r}"

    tms "The translator.{#r}"

    tms "{i}Timeasoff{/i}"

    th_tms "As they say, time is like being switched off.{#r}"
    th_tms "Or even like switching off the time of your ass...{#r}"

    tms "About how this project came to be in the first place.{#r}"

    tms "Why I initially wanted to make a completely different game.{#r}"

    tms "How I came up with the idea for the remaster.{#r}"

    tms "How I extracted resources from the original PS2 game.{#r}"

    tms "How I tried to find the right lines among sixteen thousand audio files.{#r}"

    tms "How all of this gradually turned into what you're playing right now.{#r}"

    tms "And, of course...{#r}"

    tms "Just how bad an idea {i}\"I'll quickly translate one Japanese game\"{/i} really was.{#r}"

    tms "Spoiler.{#r}"
    window hide
    stop sound fadeout 0.3

    pause(2.0)

    scene black
    play sound dramatik

    centered "{size=+14}{color=#ff0000}It was a very bad idea.{/color}{/size}{#r}"

    jump remark_menu

label remark_thanks_menu:
    call remark_thanks
    jump remark_return

# ============================================================
# ГЛАВНОЕ МЕНЮ
# ============================================================

label remark_menu:

    scene black
    with dissolve

    centered "{size=+14}A REMARK from TIMEASOFF{/size}"

    pause(0.7)

    centered "{size=-2}A short bonus chapter about how all of this was created{/size}{#r}"

    pause(0.5)

    menu:

        "How it all started{#r}":

            jump remark_beginning

        "How the remaster came to be{#r}":

            jump remark_remaster

        "How I extracted the resources from the PS2{#r}":

            jump remark_resources

        "Translation and sleppless nights{#r}":

            jump remark_translation

        "The Japanese really went all out{#r}":

            jump remark_japanese

        "A little about me{#r}":

            jump remark_about

        "Translation progress{#r}":

            jump remark_translation_status

        "What's next?{#r}":

            jump remark_future

        "✨ Thanks{#r}":
            jump remark_thanks_menu

        "Return to the game{#r}":

            jump remark_exit


# ============================================================
# КАК ВСЁ НАЧАЛОСЬ
# ============================================================

label remark_beginning:

    $ fade_fx("cr1", bg_position="default")

    tms "It all started pretty ordinarily.{#r}"

    th_tms "We had two bags of grass, 75 mescaline tablets, five sheets of powerful blotter acid...{#r}"
    th_tms "Okay, stop! I'm remembering the wrong thing...{#r}"

    tms "Anyway, one day I was sitting around and thought:{#r}"

    tms "'I should make a ZnT game.'{#r}"

    tms "Spread Zero no Tsukaima to the masses, so to speak.{#r}"

    play sound oh_my 
    show oh_my at Position(xpos=1000, ypos=500)
    "(≡^∇^≡)"

    hide oh_my with dissolve

    tms "The original idea was nothing like this.{#r}"
    tms "There wasn't even any talk of translations or visual novels.{#r}"

    tms "I wanted to make {i}\"Halkeginia Online\"{/i}.{#r}"

    show halkeginia_online at Position(xpos=500, ypos=500) with dissolve
    show halkeginia_online_mini at Position(xpos=1500, ypos=1000) with dissolve

    tms "Yeah.{#r}"

    tms "A full-fledged online game.{#r}"

    tms "At first, it was more of a joke.{#r}"

    hide halkeginia_online
    hide halkeginia_online_mini

    tms "But then I thought...{#r}"

    show think at Position(xpos=1000, ypos=500)

    tms "Why not?{#r}"

    tms "And I started working on it.{#r}"

    hide think

    tms "The first thing I started with was character models.{#r}"

    tms "Since I had never really worked with 3D before, I obviously wasn't going to model Louise from scratch.{#r}"

    show louise_gm at Position(xpos=500, ypos=500) with dissolve

    tms "A quick search turned up a low-poly Louise model for Garry's Mod.{#r}"

    play sound wink

    tms "There it is.{#r}"

    tms "This is where I should start.{#r}"

    hide louise_gm

    show enjoy at Position(xpos=1000, ypos=500)

    tms "A couple of YouTube videos with some guy vomiting in the background{#r}"

    play sound nux

    th_tms "Mmm...{#r}"

    hide enjoy

    show hacker at Position(xpos=1000, ypos=500)

    tms "And I managed to convert the model from Garry's Mod format to a format for Blender.{#r}"

    th_tms "Oh yeah, I'm a hacker{#r}"
    "(■_■)"

    tms "It was my first time working in Blender.{#r}"

    hide hacker

    tms "Louise's model came with textures and a skeleton.{#r}"

    tms "There weren't any particular problems.{#r}"

    tms "I added the animations through Mixamo.{#r}"

    tms "The model was ready.{#r}"

    tms "How about trying to make a game?{#r}"

    show l_run at Position(xpos=500, ypos=500) with dissolve 

    tms "I ended up with a character running around an empty space.{#r}"

    tms "Not bad.{#r}"

    tms "That's what I thought.{#r}"

    pause(0.5)

    tms "But one low-poly Louise model wasn't enough.{#r}"

    hide l_run with dissolve

    tms "I went looking for more models.{#r}"

    tms "And that's where things got really fun.{#r}"

    $ dissolve_fx("cr2", bg_position="default")

    tms "I searched the entire internet.{#r}"

    show zaputalsa at Position(xpos=500, ypos=500)
    tms "I went deep into all sorts of Japanese rabbit holes.{#r}"

    tms "..."

    hide zaputalsa

    show models at Position(xpos=400, ypos=500) with dissolve 

    tms "Eventually, I found some absolutely pathetic MMD models.{#r}"

    show models_koikatsu at Position(xpos=1500, ypos=1000)  with dissolve 

    tms "And also some Koikatsu cards for ZnT.{#r}"

    tms "The characters in Koikatsu already looked more or less decent.{#r}"

    hide models
    hide models_koikatsu

    play sound wink
    show think at Position(xpos=1000, ypos=500)

    tms "And a new idea came to me.{#r}"

    tms "Convert the models from Koikatsu into a proper format for Blender.{#r}"

    tms "Then use Blender to bring them into the form required for the game.{#r}"

    hide think

    tms "That's how I spent many hours.{#r}"

    show tiff at Position(xpos=1500, ypos=1000)  with dissolve 

    tms "I started with Tiffania.{#r}"

    tms "There was a result.{#r}"

    scene black
    with dissolve

    centered "{size=+14}But not the one I expected.{/size}{#r}"

    pause(0.7)

    $ fade_fx("cr2", bg_position="default")

    tms "The model came with textures and bones.{#r}"

    tms "But in MMD format.{#r}"

    tms "When converting it to a human-readable format, there was no UV map.{#r}"

    th_tms "A UV map is, roughly speaking, a layout of the model's surface that tells Blender where to place the texture.{#r}"

    tms "The textures had to be applied all over again.{#r}"

    tms "The skeleton didn't survive properly either.{#r}"

    th_tms "..."

    tms "Okay. I somehow managed to figure out the skeleton.{#r}"

    show durka at Position(xpos=1000, ypos=500)

    play sound suspence
    tms "But putting the textures onto the map seemed like way too much 'fun' to me.{#r}"

    hide durka

    show rage at Position(xpos=1500, ypos=1000)

    play sound wasted

    tms "So I abandoned the idea.{#r}"

    # ИЗОБРАЖЕНИЕ: мем «ну и нахер»
    # ЗВУК: fail sound

    tms "The idea of a 3D game died out.{#r}"

    pause(0.5)

    scene black
    with dissolve

    centered "{size=+14}What came of it in the end?{/size}{#r}"

    pause(0.7)

    $ fade_fx("cr4", bg_position="default")

    show pepit at Position(xpos=500, ypos=500) with dissolve 

    tms "A meme video of Tifa dancing to Pepit Poney.{#r}"

    show tiff at Position(xpos=1500, ypos=1100)  with dissolve 

    tms "An MMD model of Tifa.{#r}"

    show models_koikatsu at Position(xpos=1500, ypos=380)  with dissolve 

    tms "A collected set of Koikatsu cards for ZnT.{#r}"

    tms "And...{#r}"

    scene black
    play sound glass
    centered "{size=+14}{color=#ff0000}A wasted New Year's holiday.{/color}{/size}{#r}"
    centered "{size=+14}{color=#ff0000}☠️{/color}{/size}"

    pause(0.7)

    menu:
        "Continue{#r}":
            jump remark_remaster

        "Return to chapter selection{#r}":
            jump remark_menu

    return


# ============================================================
# КАК ПОЯВИЛАСЬ ИДЕЯ РЕМАСТЕРА
# ============================================================

label remark_remaster:

    $ fade_fx("cr2", bg_position="default")

    tms "After that, I started thinking.{#r}"

    show think at Position(xpos=1000, ypos=500)

    tms "What do I actually need?{#r}"

    play sound think

    tms "3D or 2D?{#r}"

    tms "Multiplayer or single-player?{#r}"

    scene black
    centered "{size=+14}Or maybe I shouldn't invent anything at all?{/size}{#r}"
    pause(0.7)
    $ fade_fx("cr3", bg_position="default")

    show sobranie at Position(xpos=1500, ypos=380) with dissolve
    tms "I even discussed this with the admin of the largest Russian-speaking ZnT community.{#r}"

    show slonyara at Position(xpos=500, ypos=500)
    tms "Our very own elephantine Russian fandom ambassador, so to speak.{#r}"
    tms "Konstantin.{#r}"

    hide sobranie
    hide slonyara

    $ dissolve_fx("cr4", bg_position="default")

    show rainbow at Position(xpos=500, ypos=500) with dissolve

    tms "And gradually, the idea of a visual novel emerged.{#r}"

    tms "After all, that's much easier than making a full-fledged 3D game.{#r}"

    tms "Maybe it would be enough to just port the games that already exist?{#r}"

    tms "After all, there's no need to come up with anything of my own.{#r}"

    play music ou_eee loop
    show oh_my at Position(xpos=1000, ypos=500)

    tms "Everything is already there.{#r}"
    tms "The story.{#r}"
    tms "The characters.{#r}"
    tms "Sprites, CGs.{#r}"
    tms "Music.{#r}"
    tms "And even voice acting.{#r}"

    tms "All that's left is to make a proper port.{#r}"

    show press_button at Position(xpos=1500, ypos=380)

    tms "So that a single button press would let a Zero no Tsukaima fan launch the game.{#r}"
    tms "With a translation.{#r}"
    tms "Without a Japanese interface.{#r}"

    hide oh_my
    show enjoy at Position(xpos=1000, ypos=500)

    tms "Without all the unnecessary ass pain.{#r}"

    stop music fadeout 2.0
    pause(2)

    hide enjoy
    hide press_button
    hide rainbow

    scene black
    centered "{size=+14}The idea remained in its infancy for a couple of months.{/size}{#r}"
    pause(0.7)
    $ fade_fx("cr1", bg_position="default")

    play sound keyboard loop

    show yyy at Position(xpos=1500, ypos=380)

    tms "Meanwhile, I was working my ass off at my JOB like a fucking demon.{#r}"

    show bund at Position(xpos=500, ypos=500)

    tms "And I really didn't have time for it.{#r}"

    hide yyy 
    hide bund

    tms "Days went by like that.{#r}"
    tms "And one day our elephant sends me his test version of a visual novel.{#r}"

    show mnimost at Position(xpos=1500, ypos=700)  with dissolve 
    show mnimost2 at Position(xpos=600, ypos=1000)  with dissolve 

    tms "It was made as an adaptation of the fanfic {i}\"MNIMOST\"{/i}.{#r}"

    play sound suspence

    th_tms "Oh, free advertising.{#r}"
    th_tms "Read it {a=https://author.today/work/587313}here{/a}{#r}"

    pause(1)
    play sound keyboard loop

    hide mnimost
    hide mnimost2

    tms "Quietly, so to speak...{#r}"
    th_tms "Dumped it.{#r}"

    show bund at Position(xpos=500, ypos=500)
    show yyy at Position(xpos=1500, ypos=380)
    tms "By that point, the workload at my JOB had eased up a little.{#r}"
    hide yyy
    hide bund

    tms "And I remembered.{#r}"

    stop sound fadeout 0.3

    pause(2)
    
    play sound wink

    $ fade_fx("cr2", bg_position="default")

    show patrik at Position(xpos=500, ypos=500)

    tms "Porting!{#r}"

    hide patrik
    
    tms "I downloaded a PS2 image of a Zero no Tsukaima game.{#r}"

    tms "The first of the trilogy. Its title is Shouakuma to Harukaze no Concerto.{#r}"
    th_tms "Commonly known as:{#r}"
    th_tms "The Familiar Zero: The Little Devil and Spring Breeze Concerto"

    tms "It was released in 2007, by the way.{#r}"

    tms "Then I installed an emulator.{#r}"

    tms "Set it up.{#r}"

    tms "I opened it.{#r}"

    tms "The game starts.{#r}"

    tms "Everything is in Japanese.{#r}"

    play sound bruh

    th_tms "Expected.{#r}"

    tms "I don't know Japanese, after all.{#r}"

    show epic at Position(xpos=1000, ypos=500)

    tms "I started looking for ways to add a translation.{#r}"

    tms "That's how I found Luna Translator.{#r}"

    th_tms "{a=https://docs.lunatranslator.org/}A program{/a} that can translate text directly over a running game.{#r}"
    th_tms "And it isn't limited to games either — it can translate text from practically any window.{#r}"

    hide epic

    show respect at Position(xpos=1000, ypos=500)
    
    th_tms "It's actually a pretty damn cool piece of software — my respect to the author{#r}"
    "(｀・ω・´)ゞ"

    hide respect

    $ fade_fx("cr4", bg_position="default")

    tms "I launched the emulator with it.{#r}"

    tms "And...{#r}"

    tms "It works.{#r}"

    tms "The dialogues really are translated on the fly.{#r}"

    tms "But the interface, choices, menus...{#r}"
    th_tms "I mean, the entire UI...{#r}"

    play sound bruh
    tms "They remained in the original.{#r}"

    tms "And that's when I realized.{#r}"

    tms "This wouldn't do.{#r}"

    tms "Advice like {i}'just learn Japanese and play — what's the problem'{/i} wouldn't help.{#r}"

    tms "An average Zero no Tsukaima fan would look at all this...{#r}"

    tms "And say:{#r}"

    scene black
    show nu_naher at Position(xpos=500, ypos=500)
    show rage at Position(xpos=1500, ypos=1000)
    play sound nu_naher

    show expression Text(
    "{size=+14}{color=#ff0000}{i}Fuck this.{/i}{/color}{/size}{#r}",
    xalign=0.5,
    yalign=0.5
    ) as naher_text

    pause 3
    hide rage 
    hide naher_text

    $ fade_fx("cr4", bg_position="default")

    tms "And that's how the idea for the remaster was born.{#r}"

    tms "Rewrite the entire game on a new engine.{#r}"

    tms "I didn't spend long thinking about it.{#r}"

    tms "I chose Ren'Py.{#r}"

    tms "Even though I'm a web developer, and a front-end developer at that...{#r}"

    show python at Position(xpos=500, ypos=500)

    tms "I wanted to strangle a boa.{#r}"
    th_tms "Ren'Py uses Python, aka Python, just so you know.{#r}"

    tms "And...{#r}"

    play sound suspence2

    show gorin at Transform(xpos=800, ypos=300, zoom=1.5)

    th_tms "God forbid I have to deal with this layout in Ren'Py.{#r}"

    hide python
    hide gorin

    tms "I thought.{#r}"

    scene black
    centered "{size=+14}{i}Why not give it a try?{/i}{/size}{#r}"
    pause(0.7)

    menu:
        "Continue{#r}":
            jump remark_resources
        "Return to chapter selection{#r}":
            jump remark_menu

    return


# ============================================================
# КАК Я ДОБЫВАЛ РЕСУРСЫ
# ============================================================

label remark_resources:

    $ fade_fx("cr3", bg_position="default")

    tms "So.{#r}"

    tms "To make the remaster, I need the resources from the original game.{#r}"

    tms "I can extract the dialogue through Luna Translator.{#r}"

    tms "All that's left is to extract the audio files and images.{#r}"

    call show_hacker

    tms "I'll find out how to decode PS2 files.{#r}"

    tms "I find the right software.{#r}"

    tms "I try it.{#r}"

    tms "I decoded the binaries.{#r}"

    tms "I got files in PS2 format.{#r}"

    tms "They still need to be decoded separately.{#r}"

    call hide_hacker

    tms "There were no problems unpacking the images.{#r}"

    tms "But the images are small.{#r}"

    play sound huh
    show small at Position(xpos=500, ypos=500)

    tms "Very small.{#r}"

    hide small

    $ dissolve_fx("cr1", bg_position="default")

    tms "So I spent an evening setting up an automatic upscale of all the files in the folder through ComfyUI.{#r}"

    play sound think
    show okak at Position(xpos=500, ypos=500)

    th_tms "While preserving the alpha channel.{#r}"

    hide okak

    tms "There were no problems with the backgrounds and CGs.{#r}"

    $ dissolve_fx("cr4", bg_position="default")

    tms "Everything's good.{#r}"

    $ dissolve_fx("cr2", bg_position="default")

    tms "But the images that had an alpha channel...{#r}"
    th_tms "In other words, a transparent background, simply put.{#r}"

    tms "Sprites.{#r}"

    tms "UI elements.{#r}"

    tms "That's where things got more interesting.{#r}"

    tms "The upscale works.{#r}"

    show dich at Position(xpos=500, ypos=500)

    tms "But the edges of the image turn into some kind of mess.{#r}"

    tms "I tried online tools.{#r}"

    tms "Same problem.{#r}"

    hide dich

    tms "Alright.{#r}"
    tms "At least I have something.{#r}"
    
    tms "I fixed some of them by hand.{#r}"
    show pending at Position(xpos=950, ypos=800)
    show epic at Position(xpos=1000, ypos=500)
    show drawing at Position(xpos=1500, ypos=700)
    show drawing2 at Position(xpos=500, ypos=700)
    play sound thats_me
    tms "I simply redrew the sprites {a=https://www.youtube.com/watch?v=GluUKYiwFTs}from scratch{/a}.{#r}"
    
    pause(0.7)

    hide epic
    hide drawing
    hide drawing2
    hide pending

    tms "Next in line was the audio.{#r}"
    tms "And that's where the biggest problems began.{#r}"

    $ dissolve_fx("cr1", bg_position="default")

    call show_hacker

    tms "The audio decoded incorrectly.{#r}"

    tms "I tried vgmstream.{#r}"
    th_tms "It's a {a=https://github.com/vgmstream/vgmstream}tool{/a} for extracting and converting audio from game formats.{#r}"

    tms "I also tried foobar2000.{#r}"
    th_tms "That's a universal {a=https://www.foobar2000.org}audio player{/a} that can open all sorts of non-standard audio formats.{#r}"

    tms "It seemed like something did decode...{#r}"

    call hide_hacker
    show dog at Position(xpos=1000, ypos=500)
    play sound teeth

    tms "But with stuttering.{#r}"

    tms "I struggled with it for a long time.{#r}"

    tms "Several evenings.{#r}"

    hide dog

    call show_hacker

    tms "And finally I found a way to properly decode the audio.{#r}"

    tms "MFAudio."

    th_tms "An old {a=https://www.zophar.net/utilities/ps2util/mfaudio-1-1.html}utility{/a} for working with game audio formats.{#r}"

    tms "Everything worked properly through it.{#r}"

    tms "For music — 22050 Hz.{#r}"
    tms "For sounds and voice acting — mono, 22050 Hz.{#r}"

    call hide_hacker

    show enjoy at Position(xpos=1000, ypos=500)
    play sound win

    tms "That's it.{#r}"
    tms "It works.{#r}"

    hide enjoy

    pause(0.5)

    tms "But then I found out something else.{#r}"

    tms "If there are thirty music tracks...{#r}"

    tms "A couple dozen sound effects...{#r}"

    tms "Then the number of dialogue files turned out to be...{#r}"

    pause(1.0)

    scene black
    play sound dramatik
    centered "{size=+14}{color=#ff0000}16 000.{/color}{/size}"
    pause(1.0)
    play sound blyat
    centered "{size=+14}{color=#ff0000}A LOT.{/color}{/size}{#r}"
    centered "{size=+14}{color=#ff0000}A WHOLE LOT.{/color}{/size}{#r}"
    pause(1.0)

    $ dissolve_fx("cr1", bg_position="default")

    show pizdech at Position(xpos=1500, ypos=700)
    show tinkoff at Position(xpos=500, ypos=700)
    play sound oh_shit
    th_tms "And that's when I started to realize the full scale of this...{#r}"

    play music ou_eee loop
    th_tms "By the way, I only started playing through the game itself as I translated it.{#r}"
    th_tms "I could have just learned Japanese...{#r}"
    th_tms "Fly to Japan...{#r}"
    th_tms "Buy a PS2 and the original game there...{#r}"
    th_tms "And play through it...{#r}"

    stop music
    th_tms "..."
    
    hide pizdech
    hide tinkoff

    tms "Anyway, I wrote a script.{#r}"

    tms "It ran MFAudio on every STV file in the folder.{#r}"

    th_tms "STV is a PlayStation audio codec.{#r}"

    tms "And converted everything to WAV.{#r}"

    tms "It worked.{#r}"

    show bonk at Position(xpos=1500, ypos=700)
    play sound bonk

    tms "Some audio files turned out to be corrupted.{#r}"

    tms "Oh well.{#r}"

    hide bonk

    tms "A couple dozen of them — no big deal.{#r}"
    tms "The main problem was something else now.{#r}"

    play sound huh
    show think at Position(xpos=1000, ypos=500)

    tms "How do I match the audio to the dialogue?{#r}"
    tms "How do I find the right line among {color=#ff0000}sixteen thousand{/color} files?{#r}"

    hide think

    menu:
        "Continue{#r}":
            jump remark_translation
        "Return to chapter selection{#r}":
            jump remark_menu

    return


# ============================================================
# ПЕРЕВОД И БЕССОННЫЕ НОЧИ
# ============================================================

label remark_translation:

    $ fade_fx("cr1", bg_position="default")

    tms "I need to transcribe the audio into text.{#r}"
    tms "And automatically.{#r}"
    
    call show_hacker

    tms "I'm breaking out the neural network again.{#r}"

    tms "I have a finished script.{#r}"

    tms "Whisper for transcription.{#r}"
    th_tms "A neural network that listens to audio and turns human speech into text.{#r}"

    tms "Google Translator API for automatic translation.{#r}"
    th_tms "Basically, something that lets a program send text to Google Translate by itself and get the translation back.{#r}"

    tms "I tested it.{#r}"

    tms "It works.{#r}"

    tms "I left it running overnight.{#r}"

    tms "Because that's exactly how long it needed.{#r}"

    call hide_hacker

    # ЗВУК: работающий компьютер
    # ИЗОБРАЖЕНИЕ: компьютер ночью

    scene black
    centered "{size=+14}In the morning...{/size}{#r}"

    $ fade_fx("cr4", bg_position="default")

    tms "I get a CSV.{#r}"
    th_tms "A text file in table format.{#r}"

    tms "All the dialogue is saved.{#r}"

    tms "Excellent.{#r}"

    tms "I can make the remaster.{#r}"

    play sound win2

    "＼(＾▽＾)／"

    pause(0.5)

    $ dissolve_fx("cr1", bg_position="default")

    tms "And that's where development began.{#r}"

    tms "Before that, I had only studied Python at a basic level.{#r}"

    tms "And Ren'Py has its own quirks when it comes to syntax.{#r}"

    tms "So a significant part of the project was made according to the principle:{#r}"

    scene black with dissolve
    centered "{size=+14}{i}\"We'll figure it out on the spot.\"{/i}{/size}{#r}"

    $ dissolve_fx("cr1", bg_position="default")

    play sound keyboard loop

    tms "I was kind of too lazy to dig through the documentation.{#r}"

    tms "I mostly looked at finished games written in Ren'Py.{#r}"

    tms "For the logic, I usually brought out the neural network.{#r}"

    tms "But the neural network and Ren'Py don't exactly get along.{#r}"

    play sound error
    tms "So I often had to use the scientific method of trial and error to figure out why some bullshit wasn't working.{#r}"

    tms "Dialogue is dialogue no matter where you are.{#r}"
    tms "Simple.{#r}"
    tms "But tedious.{#r}"
    tms "And when there are thousands of dialogues like that...{#r}"
    tms "That's when it gets fun.{#r}"
    tms "Especially when you don't just have to translate the text.{#r}"
    tms "You also need to figure out which voice recording belongs to it.{#r}"
    tms "Check the translation.{#r}"
    tms "Check how it is displayed.{#r}"
    tms "Check the choices.{#r}"
    tms "And make sure the game still works after all these manipulations.{#r}"
    tms "Sounds like real routine work.{#r}"
    th_tms "And that's exactly what it is.{#r}"
    tms "And it's not a quick job.{#r}"
    tms "Especially when you're doing it in three languages at once.{#r}"
    tms "And you're handling the voice acting on top of that.{#r}"
    th_tms "AI is used for the translation.{#r}"
    th_tms "But everything is carefully checked manually.{#r}"

    scene black with dissolve

    show expression Text(
    "{size=+14}{color=#ff0000}{i}And that's where I miscalculated.{/i}{/color}{/size}{#r}",
    xalign=0.5,
    yalign=0.5
    ) as gde_text0 with dissolve

    pause(2)

    hide gde_text0 with dissolve

    show monkey at Position(xpos=1500, ypos=1000)
    show expression Text(
    "{size=+14}{color=#ff0000}{i}But where?{/i}{/color}{/size}{#r}",
    xalign=0.5,
    yalign=0.5
    ) as gde_text 

    with dissolve

    pause 2
    hide monkey
    hide gde_text
    with dissolve

    pause(0.7)

    $ dissolve_fx("cr1", bg_position="default")

    play sound bruh

    tms "I had no idea how huge this game was when I took it on.{#r}"

    play music danger loop

    tms "I spent sleepless nights sitting there.{#r}"

    tms "Translated.{#r}"

    tms "..."

    tms "Checked.{#r}"

    tms "..."

    tms "Translated again.{#r}"

    tms "And that's how all my free time went into this.{#r}"
    th_tms "And all the time that wasn't free...{#r}"
    
    "( ╥ω╥ )"

    # ИЗОБРАЖЕНИЕ: часы 03:00 / 04:00
    # ЗВУК: тиканье часов

    th_tms "Oh no.{#r}"

    th_tms "I chose the hard way.{#r}"

    "。゜゜(´Ｏ`) ゜゜。"

    tms "This is a thankless job.{#r}"

    tms "But.{#r}"

    stop music fadeout 1.0
    pause(1)

    call remark_thanks

    menu:
        "Continue{#r}":
            jump remark_japanese
        "Return to chapter selection{#r}":
            jump remark_menu

    return

# ============================================================
# БЛАГОДАРНОСТИ
# ============================================================

label remark_thanks:
    play music epic_sax loop
    $ dissolve_fx("cr5", bg_position="default")

    tms "This is something I do for the soul.{#r}"

    tms "And I believe I've still made a good contribution to the fandom.{#r}"

    tms "Especially since I had help.{#r}"

    play sound cheer0

    show alex at Position(xpos=500, ypos=500)  with dissolve

    tms "Thanks to {a=https://t.me/Alex_Hrst}Alexander{/a}for helping with the translation!{#r}"

    hide alex with dissolve  

    play sound cheer3

    show slonyara at Position(xpos=500, ypos=500) with dissolve

    tms "Thanks to our {a=https://t.me/Infected_Dreamer}elephant-Konstantin{/a} and the {a=https://vk.ru/zeronotsukaima}Russian fandom{/a} for staying active even after all these years!{#r}"

    hide slonyara with dissolve

    play sound cheer

    show nobory at Position(xpos=500, ypos=500)  with dissolve

    tms "And of course, thanks to Noboru Yamaguchi for creating Louise and the whole Zero no Tsukaima universe!{#r}"

    hide nobory with dissolve

    stop music fadeout 2.0

    pause(1)

    return

# ============================================================
# ЯПОНЦЫ РЕАЛЬНО ЗАМОРОЧИЛИСЬ
# ============================================================

label remark_japanese:
    
    scene black
    play sound nostalgy loop

    tms "And yet, the Japanese really went all out with this game.{#r}"

    tms "They voiced every single line.{#r}"

    tms "And if a line is repeated in a different dialogue variation...{#r}"

    tms "It's still voiced again.{#r}"

    tms "With a different intonation.{#r}"

    centered "{size=+14}WITH A DIFFERENT INTONATION.{/size}{#r}"
    pause(0.5)

    tms "There were cases where a single line had three different voice versions.{#r}"
    tms "That's when it was repeated across different choice branches.{#r}"
    
    show screen japanese_film_overlay
    $ flash_fx("si_room", sprites=("m 4 happy", "l 1 angry"))

    tms "For example, like with Montmorency's hoho.{#r}"

    centered "{size=+14}{color=#ffffff}Version one{/color}{/size}{#r}"

    voice "ch1.6_m_002"
    m "...Hohoho."

    $ show_sprites(("l 3 angry", "m 4 happy"))
    centered "{size=+14}{color=#ffffff}Version two{/color}{/size}{#r}"

    voice "ch1.6_m_002-2"
    m "...Hohoho."

    $ show_sprites(("k 1", "m 4 happy", "l 3 angry"), center_front=True)

    centered "{size=+14}{color=#ffffff}Version three{/color}{/size}{#r}"

    voice "ch1.6_m_002-3"
    m "...Ohohoho."

    tms "So the duration and joy of Montmorency's hoho directly depends on your choice.{#r}"

    # ЗВУК: мемный вздох

    $ flash_fx("osman_cabinet", sprites=("l 1 sad", "o 1"))

    tms "Even the headmaster's bleating was recorded in three versions here.{#r}"

    centered "{size=+14}{color=#ffffff}Version two{/color}{/size}{#r}"

    voice "ch1.7_o_016"
    o "Now, now, just consider it extra lessons while the repairs are underway."

    centered "{size=+14}{color=#ffffff}Version two{/color}{/size}{#r}"

    voice "ch1.7_o_016-2"
    o "Now, now, just consider it extra lessons while the repairs are underway."

    centered "{size=+14}{color=#ffffff}Version three{/color}{/size}{#r}"

    voice "ch1.7_o_016-3"
    o "Now, now, just consider it extra lessons while the repairs are underway."

    th_tms "Can you picture the seiyuu's faces as they hoho and bleat into the microphone?{#r}"
    tms "Still, they really put in the effort.{#r}"
    tms "You'd think...{#r}"
    tms "Why?{#r}"
    tms "But they did it.{#r}"

    tms "Three times, no less.{#r}"
    "(⊙_⊙)"

    # ИЗОБРАЖЕНИЕ: мем «разработчики, зачем?»
    tms "And now I had to find all of them.{#r}"

    th_tms "Thanks, Japan.{#r}"
    "(×_×)"

    tms "But honestly.{#r}"
    tms "I've played several modern visual novels.{#r}"
    tms "And not Japanese ones, by the way.{#r}"
    tms "In terms of size, they barely even compare to a single chapter of this game.{#r}"
    tms "And that's awesome!{#r}"
    tms "But it would be even cooler if the Japanese themselves had made a port.{#r}"
    tms "And if they had added at least English...{#r}"
    "(｡-ω-｡)"
    tms "There are things like that on Steam right now. Clannad is a good example.{#r}"
    tms "And everyone wins. The publisher can make money too.{#r}"
    
    scene black with dissolve
    centered "{size=+14}But apparently, this is not the story of this franchise.{/size}{#r}"

    stop sound fadeout 2.0
    pause(2)

    hide screen japanese_film_overlay

    menu:
        "Continue{#r}":
            jump remark_about
        "Return to chapter selection{#r}":
            jump remark_menu

    return


# ============================================================
# НЕМНОГО ОБО МНЕ
# ============================================================

label remark_about:

    $ fade_fx("cr5", bg_position="default")

    tms "And, I guess, a little about me.{#r}"
    tms "If you've somehow made it all the way to this chapter...{#r}"
    "👉👈"

    tms "Then you've already figured out that I'm not a professional translator.{#r}"
    tms "And I'm not a professional visual novel developer either.{#r}"

    tms "I'm a web developer, actually.{#r}"

    show js at Position(xpos=1500, ypos=700)

    tms "JavaScript.{#r}"
    th_tms "and Java.{#r}"
    tms "Kek.{#r}"

    hide js

    tms "Web.{#r}"
    tms "Websites.{#r}"
    tms "That's more or less what brought me here.{#r}"

    tms "But I had plenty of motivation.{#r}"
    tms "Zero no Tsukaima isn't just a franchise to me.{#r}"
    tms "Louise has been my first and only waifu ever since we met.{#r}"
    tms "As far as I remember, that was back in 2013.{#r}"
    tms "So, quite a long time ago.{#r}"
    tms "That's why I'm happy to contribute to the development of this universe.{#r}"
    tms "And if thanks to this project even a few people can properly play one of the ZnT games...{#r}"
    tms "Then none of this was for nothing.{#r}"
    tms "This is a fan project.{#r}"
    tms "No commercial stuff.{#r}"
    tms "Simply out of love.{#r}"
    tms "And because someone had to do it.{#r}"

    menu:
        "Continue{#r}":
            jump remark_translation_status
        "Return to chapter selection{#r}":
            jump remark_menu

    return

# ============================================================
# МЕНЮ ПРОГРЕССА
# ============================================================

label remark_translation_status:

    scene black
    with dissolve

    centered "{size=+14}TRANSLATION STATUS{/size}{#r}"

    pause(0.5)

    tms "Well, we can't forget about this.{#r}"
    tms "Let's see how far I've actually managed to get.{#r}"
    tms "Just a warning.{#r}"
    tms "Not very far.{#r}"

    pause(0.5)

    centered "{size=+8}Done{/size}{#r}"
    tms "Prologue"
    tms "Chapter One: \"Louise of Zero\""

    pause(0.8)

    tms "The rest are waiting their turn.{#r}"

    tms "And when I say 'the first chapter'...{#r}"

    tms "Don't picture five minutes of text.{#r}"

    tms "There are over a thousand voiced lines in there.{#r}"

    tms "And four months of work.{#r}"

    play sound glass
    centered "{size=+14}{color=#ff0000}Four.{/color}{/size}{#r}"
    centered "{size=+14}{color=#ff0000}Months.{/color}{/size}"

    pause(0.7)

    tms "For one chapter.{#r}"

    menu:
        "Continue{#r}":
            jump remark_future

        "Return to chapter selection{#r}":
            jump remark_menu

# ============================================================
# ЧТО ДАЛЬШЕ
# ============================================================

label remark_future:

    $ fade_fx("cr5", bg_position="default")

    tms "Well, the big question.{#r}"
    tms "What's next?{#r}"
    tms "Well...{#r}"

    tms "Right now, only a small part of the whole game is ready.{#r}"
    tms "But it's a start.{#r}"
    th_tms "As they say, the most important thing is to start...{#r}"
    tms "There's still the main story ahead.{#r}"
    tms "Many routes.{#r}"
    tms "And separate stories.{#r}"

    tms "So this won't be over quickly.{#r}"
    tms "But after this much work...{#r}"

    pause(0.5)

    scene black
    play sound dramatik
    centered "{size=+14}{color=#ff0000}I decided to take a break.{/color}{/size}{#r}"

    $ fade_fx("cr1", bg_position="default")

    th_tms "Four months for a single chapter is, to put it mildly, a fucking lot.{#r}"
    tms "I want to take a little break from translating.{#r}"
    th_tms "And generally take care of some other things in life.{#r}"

    pause(0.5)

    tms "I can't promise that I'll come back to the translation.{#r}"
    tms "Again, this project has always been driven purely by enthusiasm.{#r}"
    tms "I don't know how long this break will last.{#r}"
    tms "And I don't know if I'll ever have enough time and motivation to continue.{#r}"

    $ fade_fx("cr4", bg_position="default")

    tms "Of course, I'd still love to see how the whole story ends.{#r}"
    tms "And I'd love for fans from all over the world to be able to properly play this game.{#r}"

    pause(0.5)

    tms "So...{#r}"
    th_tms "We'll see.{#r}"
    $ fade_fx("cr5", bg_position="default")
    tms "For now, I'm taking a break from the translation.{#r}"

    tms "I'm leaving the progress here anyway.{#r}"
    tms "Not as a promise of future updates.{#r}"
    tms "Just so you can see how far I actually got.{#r}"

    tms "But for now...{#r}"
    tms "If you find a bug — {a=https://t.me/timeasoff}let me know{/a}.{#r}"
    tms "If you spot a crappy translation — {a=https://t.me/timeasoff}let me know{/a}.{#r}"
    tms "If you want to help — even better.{#r}"
    th_tms "You don't need any particular skills to help.{#r}"

    th_tms "In any case, if something is unclear, I'll explain and help.{#r}"
    th_tms "{a=https://t.me/timeasoff}Write here{/a}{#r}"

    tms "If you just played the game and enjoyed it...{#r}"

    tms "Thank you too.{#r}"

    pause(0.7)

    tms "And now...{#r}"

    tms "Get back to the game.{#r}"

    tms "I've already gotten ahead of myself here.{#r}"

    jump remark_return


# ============================================================
# ВОЗВРАТ К МЕНЮ
# ============================================================

label remark_return:

    scene black
    with dissolve

    centered "{size=+8}Well, anything else you'd like to see?{/size}{#r}"

    pause(0.5)

    menu:

        "Yes, back to the stories{#r}":

            jump remark_menu

        "No, back to the game{#r}":

            jump remark_exit


# ============================================================
# ВЫХОД
# ============================================================

label remark_exit:

    stop sound fadeout 1.0

    scene black
    with fade

    centered "{size=+10}Thanks for stopping by.{/size}{#r}"

    pause(1.5)

    centered "{size=-2}And now — back to Halkeginia.{/size}{#r}"

    pause(1.5)

    return
