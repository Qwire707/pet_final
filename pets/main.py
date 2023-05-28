import play
eat = True
play.set_backdrop("purple")

#коли програма прцює фнкція для початку гри
@play.when_program_starts
def start():
    global player, speech
    text1 = play.new_text(words="г - гладити, р - розсмішити, в - відпочивати" , x=0 , y=250, font_size=40)
    text2 = play.new_text(words="к - кормити, п - причепурити, пробіл - піти", x=0 , y=210, font_size=40)
    player = play.new_image(image="hello!.jpg", x=0, y=0, size=100)
    speech = play.new_text(words="Hello my friend", x=0, y=-250, font_size=40)


#повторювати завжди(ігровий цикл)
@play.repeat_forever
async def do():
    global eat
    if play.key_is_pressed("г"):
        await play.timer(1.0)
        player.image = "normX2 (1).png"
        speech.words = "Good"
        await play.timer(3.0)
        player.image = "SHIT_FLOPPER_008 (1) (1).png"
        speech.words = "I'm in a bad mood today"
        await play.timer(3.0)
        speech.words = "well, make me laugh quickly"
    if play.key_is_pressed("р"):
        await play.timer(2.0)
        player.image = "smile.jpg"
        speech.words = "Nice joke*)"
    if play.key_is_pressed("к"):
        await play.timer(1.0)
        player.image = "boss.jpg"
        speech.words = "thanks for the food*)"
    if play.key_is_pressed("в"):
        await play.timer(1.0)
        player.image = "lazy.jpg"
        speech.words = "how to rest well*)"
    if play.key_is_pressed("п"):
        await play.timer(1.0)
        player.image = "pon.jpg"
        speech.words = "don't touch me, I'm still resting"
    if play.key_is_pressed("П"):
        await play.timer(1.0)
        player.image = "Beautiful.jpg"
        speech.words = "i am beautiful now"
    if play.key_is_pressed("space"):
        await play.timer(1.0)
        player.image = "bye.jpg"
        speech.words = "are you leaving?"
        await play.timer(3.0)
        speech.words = "come back soon, I'll be waiting*)"



    



    
        

    




    

#запуск програми
play.start_program()
