import play
eat = True
play.set_backdrop("purple")

#коли програма працює функція для початку гри
@play.when_program_starts
def start():
    global player, speech
    text1 = play.new_text(words="г - гладити, р - розсмішити, в - відпочивати" , x=0 , y=250, font_size=40)
    text2 = play.new_text(words="к - кормити, п - причепурити, пробіл - піти", x=0 , y=210, font_size=40)
    player = play.new_image(image="hello!.jpg", x=0, y=0, size=100)
    speech = play.new_text(words="Привіт друже!", x=0, y=-250, font_size=40)


#повторювати завжди(ігровий цикл)
@play.repeat_forever
async def do():
    global eat
    if play.key_is_pressed("г"):
        await play.timer(1.0)
        player.image = "normX2 (1).png"
        speech.words = "Добре"
        await play.timer(4.0)
        player.image = "SHIT_FLOPPER_008 (1) (1).png"
        speech.words = "В мене сьогодні поганий настрій"
        await play.timer(3.0)
        speech.words = "Тому спробуй мене розсмішити"
    if play.key_is_pressed("р"):
        await play.timer(2.0)
        player.image = "smile.jpg"
        speech.words = "Гарний жарт*)"
        await play.timer(4.0)
        player.image = "SHIT_FLOPPER_008 (1) (1).png"
        speech.words = "Жартуєш ти добре, але час обідати"
        await play.timer(3.0)
        speech.words = "Швидко покорми мене!"



    if play.key_is_pressed("к"):
        await play.timer(1.0)
        player.image = "boss.jpg"
        speech.words = "Дякую за обід*)"
        await play.timer(3.0)
        player.image = "boss2.jpg"
        speech.words = "Тепер можна й відпочити"
    if play.key_is_pressed("в"):
        await play.timer(1.0)
        player.image = "lazy.jpg"
        speech.words = "Який гарний день для відпочинку.Чи не так?*)"
        await play.timer(4.0)
        player.image = "pon.jpg"
        speech.words = "Сьогодні справді гарний день але..."
        await play.timer(4.0)
        speech.words = "подивись який я негарний, негайно причепури мене"
    if play.key_is_pressed("п"):
        await play.timer(1.0)
        player.image = "Beautiful.jpg"
        speech.words = "Який я гарний"
    if play.key_is_pressed("space"):
        await play.timer(1.0)
        player.image = "bye.jpg"
        speech.words = "Вже йдеш? Гарного дня"
        await play.timer(3.0)
        speech.words = "Повертайся скоріше, я буду чекати на тебе*)"




    



    
        

    




    

#запуск програми
play.start_program()
