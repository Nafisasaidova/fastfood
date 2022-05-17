"""
 This is a echo bot.
 It echoes any incoming text messages.
 """
 
import logging
from config import API_TOKEN 
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

 

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

##Start uchun
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum.BURGERS ga xush kelibsiz 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button2)


##Buyurtma berish
@dp.message_handler(text="Buyurtma berish 👩‍💻")
async def send_welcome(message: types.Message):
    await message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)



##Sozlamalar uchun
@dp.message_handler(text="Sozlamalar🛠")
async def send_welcome(message: types.Message):
    await message.reply("Sozlamalar sozlanmoqda🛠")


##Aloqa uchun
@dp.message_handler(text="Biz bilan aloqa☎️")
async def send_welcome(message: types.Message):
    await message.reply("Sozlamalar sozlanmoqda🛠")

##Buyutma ortga qaytish  
@dp.callback_query_handler(text="ortbuyurtma")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Assalomu aleykum.BURGERS ga xush kelibsiz 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button2)

   
##Lavash uchunS
@dp.callback_query_handler(text="lav")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/1.jpg','rb'),
        caption="""✅Marxamat lavashlar menusi!!!""", reply_markup = button4 )
    #await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)
  

##Lavash ortga qaytish  
@dp.callback_query_handler(text="ortlavash")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    

##Hod dog uchun
@dp.callback_query_handler(text="hod")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Hod Dog menusi!!!</b>",parse_mode='HTML',reply_markup=button5)
    
##Hod dog ortga qaytish  
@dp.callback_query_handler(text="orthoddog")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    



##sendvich uchun
@dp.callback_query_handler(text="send")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Sendvich menusi!!!</b>",parse_mode='HTML',reply_markup=button6)

##Sendvich ortga qaytish  
@dp.callback_query_handler(text="ortsendvich")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    



    
##shaurma uchun
@dp.callback_query_handler(text="shaur")
async def menu_hod(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/2.jpg','rb'),
        caption="""✅Marxamat Shaurma menusi!!!""", reply_markup = button7 )
    #await call.message.answer(f"<b>✅Marxamat Shaurma menusi!!!</b>",parse_mode='HTML',reply_markup=button7)
  
##shaurma ortga qaytish  
@dp.callback_query_handler(text="ortshaurma")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    



##Burger uchun
@dp.callback_query_handler(text="bur")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Burger menusi!!!</b>",parse_mode='HTML',reply_markup=button8)

##Burger uchun ortga qaytish  
@dp.callback_query_handler(text="ortBurger")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    



##Doner uchun
@dp.callback_query_handler(text="don")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Doner menusi!!!</b>",parse_mode='HTML',reply_markup=button9)

##Doner uchun ortga qaytish  
@dp.callback_query_handler(text="ortdoner")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    


##Gazak uchun
@dp.callback_query_handler(text="gazak")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Gazak menusi!!!</b>",parse_mode='HTML',reply_markup=button10)

##Gazak uchun ortga qaytish  
@dp.callback_query_handler(text="ortgazak")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    


##Ichimliklar uchun
@dp.callback_query_handler(text="ich")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)

##Icimliklar uchun ortga qaytish  
@dp.callback_query_handler(text="ortichimlik")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    


##Desert  uchun
@dp.callback_query_handler(text="des")
async def menu_hod(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/3.jpg','rb'),
        caption="""✅Marxamat Desert menusi!!!!!!""", reply_markup = button12 )
    #await call.message.answer(f"<b>✅Marxamat Desert menusi!!!</b>",parse_mode='HTML',reply_markup=button12)

##Desert uchun ortga qaytish  
@dp.callback_query_handler(text="ortdesert")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    

##Pitsa  uchun
@dp.callback_query_handler(text="piz")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Pizza menusi!!!</b>",parse_mode='HTML',reply_markup=button13)


##Pitsa uchun ortga qaytish  
@dp.callback_query_handler(text="ortpissa")
async def menu_hod(call:CallbackQuery):
    await call.message.reply("Marhamat menu: 👩‍🍳👩‍🍳👩‍🍳",reply_markup=button3)    



##ichki menu
#Lavash uchun1
@dp.callback_query_handler(text="mgl")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button14)
    

##Lavash mol gushi uchun ortga qaytish  
@dp.callback_query_handler(text="ortimollavash")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)


##ichki menu
#Lavash uchun2
@dp.callback_query_handler(text="mgql")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button15)

    
##Lavash mol gushi qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortimolqal")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)


##ichki menu
# tovuqli avash uchun3
@dp.callback_query_handler(text="tovl")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button16)
    

##Lavash tovuqli uchun ortga qaytish  
@dp.callback_query_handler(text="ortilavtovuq")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)




##ichki menu
#Lavash tovuq qalampir  uchun4
@dp.callback_query_handler(text="tgql")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button17)

##Lavash tovuqli qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortilavqaltov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)


    

##ichki menu
#Lavash uchun5
@dp.callback_query_handler(text="tovpl")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button18)
    
##Lavash tovuqli pishloqli uchun ortga qaytish  
@dp.callback_query_handler(text="ortilavpishtov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)



##ichki menu
#Lavash uchun6
@dp.callback_query_handler(text="mgpl")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button19)

##Lavash tovuqli pishloqli uchun ortga qaytish  
@dp.callback_query_handler(text="ortilavpishmol")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)












##ichki menu
#Lavash uchun7
@dp.callback_query_handler(text="fit")
async def menu_tanlash(call:CallbackQuery):
      await call.message.answer_photo(
        photo=open('images/4.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button37 )
    #await call.message.answer(f"<b>✅Narxi:   20 000 so'm\nTarkibi: Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan.\nMiqdorini tanlang yoki kiriting!!!</b>",parse_mode='HTML',reply_markup=button37)






##Lavash flit uchun ortga qaytish  
@dp.callback_query_handler(text="ortflit")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat lavashlar menusi!!!</b>",parse_mode='HTML',reply_markup=button4)






##ichki menu
# Baget Dabl Hod dog uchun
@dp.callback_query_handler(text="hodbag")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/5.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup = button21 )
    #await call.message.answer(f"<b>✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\nNarxi 17000 ming.!!!</b>",parse_mode='HTML',reply_markup=button21)




##ichki menu2
#Baget Dabl Hod dog uchun 1
@dp.callback_query_handler(text="hod1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 17000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)

##Hod dog raqamlar uchun ortga qaytish  
@dp.callback_query_handler(text="orthoddograq")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Hod Dog menusi!!!</b>",parse_mode='HTML',reply_markup=button5)


##ichki menu2
# Baget Dabl Hod dog uchun 2
@dp.callback_query_handler(text="hod2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 34000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Baget Dabl Hod dog uchun 3
@dp.callback_query_handler(text="hod3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 51000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Baget Dabl Hod dog uchun 4
@dp.callback_query_handler(text="dog4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 68000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Baget Dabl Hod dog uchun 5
@dp.callback_query_handler(text="dog5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 85000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Baget Dabl Hod dog uchun 6
@dp.callback_query_handler(text="dog6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 102000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Baget Dabl Hod dog uchun 7
@dp.callback_query_handler(text="dog7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 119000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
# Baget Dabl Hod dog uchun 8
@dp.callback_query_handler(text="dog8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 136000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Baget dabl Hod dog uchun 9

@dp.callback_query_handler(text="dog9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Hod dog Baget Dabl jo'natiladi.\nNarxi 153000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




















##ichki menu
# Classik Hod dog uchun
@dp.callback_query_handler(text="hodclass")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/6.jpg','rb'),
        caption="""Narxi:8000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup = button23 )
   # await call.message.answer(f"<b>✅Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz. \nNarxi: 8 000 so'm.!!!</b>",parse_mode='HTML',reply_markup=button23)



##ichki menu3
# Classik Hod dog uchun 2


@dp.callback_query_handler(text="hodclass1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Classik Hod dog jo'natiladi.\nNarxi 8000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##Hod dog raqamlar classik uchun ortga qaytish  
@dp.callback_query_handler(text="orthoddogclassik")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Hod Dog menusi!!!</b>",parse_mode='HTML',reply_markup=button5)



##ichki menu2
# Classik Hod dog uchun 2
@dp.callback_query_handler(text="hodclass2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Classik Hod dog jo'natiladi.\nNarxi 16000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Classik Hod dog uchun 3
@dp.callback_query_handler(text="hodclass3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Classik Hod dog jo'natiladi.\nNarxi 24000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
# Classik Hod dog uchun 4
@dp.callback_query_handler(text="hodclass4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Classik Hod dog jo'natiladi.\nNarxi 32000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Classik Hod dog uchun 5
@dp.callback_query_handler(text="hodclass5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Classik Hod dog jo'natiladi.\nNarxi 40000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Classik Hod dog uchun 6
@dp.callback_query_handler(text="hodclass6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Classik Hod dog jo'natiladi.\nNarxi 48000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Classik Hod dog uchun 7
@dp.callback_query_handler(text="hodclass7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Classik Hod dog jo'natiladi.\nNarxi 56000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
# Classik Hod dog uchun 8
@dp.callback_query_handler(text="hodclass8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Classik Hod dog jo'natiladi.\nNarxi 64000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
# Classik Hod dog uchun 9
@dp.callback_query_handler(text="hodclass9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Classik Hod dog jo'natiladi.\nNarxi 72000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)





##ichki menu
# Korolevskiy Hod dog uchun
@dp.callback_query_handler(text="korol")
async def menu_tanlash(call:CallbackQuery):
        await call.message.answer_photo(
        photo=open('images/7.jpg','rb'),
        caption="""Narxi:15000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup = button24 )
    #await call.message.answer(f"<b>✅Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz.\nNarxi: 15 000 so'm.!!!</b>",parse_mode='HTML',reply_markup=button24)



##ichki menu3
# Korolevskiy Hod dog uchun 2


@dp.callback_query_handler(text="korol1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 15000  ming.!!!</b>",parse_mode='HTML',reply_markup=button22)

##Hod dog raqamlar classik uchun ortga qaytish  
@dp.callback_query_handler(text="orthoddogkorol")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Hod Dog menusi!!!</b>",parse_mode='HTML',reply_markup=button5)





##ichki menu2
# Korolevskiy Hod dog uchun 2
@dp.callback_query_handler(text="korol2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 30000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Korolevskiy Hod dog uchun 3
@dp.callback_query_handler(text="korol3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 45000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Korolevskiy Hod dog uchun 4
@dp.callback_query_handler(text="korol4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 60000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Korolevskiy Hod dog uchun 5
@dp.callback_query_handler(text="korol5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 75000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Korolevskiy Hod dog uchun 6
@dp.callback_query_handler(text="korol6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 90000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Korolevskiy Hod dog uchun 7
@dp.callback_query_handler(text="korol7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 105000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Korolevskiy Hod dog uchun 8
@dp.callback_query_handler(text="korol8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 120000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Korolevskiy Hod dog uchun 9
@dp.callback_query_handler(text="korol9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 135000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)






##ichki menu
# Tovuqli Hod dog uchun
@dp.callback_query_handler(text="tovuqhod")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/8.jpg','rb'),
        caption="""Narxi:17000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup = button25 )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, ketchup va xantal, qovurilgan piyoz.\nNarxi: 17 000 so'm.!!!</b>",parse_mode='HTML',reply_markup=button25)



##ichki menu3
# Tovuqli Hod dog uchun 2


@dp.callback_query_handler(text="tovuqhod1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 17000  ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##Hod dog raqamlar classik uchun ortga qaytish  
@dp.callback_query_handler(text="orthoddogtovuq")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Hod Dog menusi!!!</b>",parse_mode='HTML',reply_markup=button5)



##ichki menu2
# Tovuqli Hod dog uchun 2
@dp.callback_query_handler(text="tovuqhod2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 34000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Tovuqli Hod dog uchun 3
@dp.callback_query_handler(text="tovuqhod3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 51000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Tovuqli Hod dog uchun 4
@dp.callback_query_handler(text="tovuqhod4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 68000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Tovuqli Hod dog uchun 5
@dp.callback_query_handler(text="tovuqhod5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Korolevskiy Hod dog jo'natiladi.\nNarxi 85000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Tovuqli Hod dog uchun 6
@dp.callback_query_handler(text="tovuqhod6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Tovuqli Hod dog jo'natiladi.\nNarxi 102000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Tovuqli Hod dog uchun 7
@dp.callback_query_handler(text="tovuqhod7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Tovuqli Hod dog jo'natiladi.\nNarxi 119000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Tovuqli Hod dog uchun 8
@dp.callback_query_handler(text="tovuqhod8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Tovuqli Hod dog jo'natiladi.\nNarxi 136000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Tovuqli Hod dog uchun 9
@dp.callback_query_handler(text="tovuqhod9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Tovuqli Hod dog jo'natiladi.\nNarxi 153000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu
# Mini  gushtlik lavash uchun
@dp.callback_query_handler(text="lavmini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/9.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button26 )
    # await call.message.answer(f"<b>✅ Narxi:   18 000 so'm.\nTarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting!!!</b>",parse_mode='HTML',reply_markup=button26)



##ichki menu3
# Mini  gushtlik lavash uchun 1


@dp.callback_query_handler(text="lavmini1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Go'shtlik lavash jo'natiladi.\nNarxi 18000  ming.!!!</b>",parse_mode='HTML',reply_markup=button22)





##ichki menu2
# Mini  gushtlik lavash uchun 2
@dp.callback_query_handler(text="lavmini2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Go'shtlik lavash jo'natiladi.\nNarxi 36000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##Lavash  raqamlar mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavmini")
async def menu_hod(call:CallbackQuery):
 await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button14)
    


##ichki menu2
# Mini  gushtlik lavash uchun 3
@dp.callback_query_handler(text="lavmini3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Go'shtlik lavash jo'natiladi.\nNarxi 54000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  gushtlik lavash uchun 4
@dp.callback_query_handler(text="lavmini4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Go'shtlik lavash jo'natiladi.\nNarxi 72000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Mini  gushtlik lavash uchun 5
@dp.callback_query_handler(text="lavmini5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Go'shtlik lavash jo'natiladi.\nNarxi 90000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Mini  gushtlik lavash uchun 6
@dp.callback_query_handler(text="lavmini6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Go'shtlik lavash jo'natiladi.\nNarxi 108000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Mini  gushtlik lavash uchun 7
@dp.callback_query_handler(text="lavmini7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Go'shtlik lavash jo'natiladi.\nNarxi 126000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  gushtlik lavash uchun 8
@dp.callback_query_handler(text="lavmini8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Go'shtlik lavash jo'natiladi.\nNarxi 144000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  gushtlik lavash uchun 9
@dp.callback_query_handler(text="lavmini9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Go'shtlik lavash jo'natiladi.\nNarxi 162000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu
# Classik  gushtlik lavash uchun
@dp.callback_query_handler(text="lavclassik")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/9.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button27 )
    #await call.message.answer(f"<b>✅  Narxi:   22 000 so'm.\nTarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting!!!</b>",parse_mode='HTML',reply_markup=button27)



##ichki menu3
# Classik  gushtlik lavash uchun 1


@dp.callback_query_handler(text="lavclassik1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 22000  ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##Lavash  raqamlar classik uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavclassik")
async def menu_hod(call:CallbackQuery):
 await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button14)
    



##ichki menu2
# Classik  gushtlik lavash uchun 2
@dp.callback_query_handler(text="lavclassik2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 44000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Classik  gushtlik lavash uchun 3
@dp.callback_query_handler(text="lavclassik3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 66000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Classik  gushtlik lavash uchun 4
@dp.callback_query_handler(text="lavclassik4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 88000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Classik  gushtlik lavash uchun 5
@dp.callback_query_handler(text="lavclassik5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 110000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Classik  gushtlik lavash uchun 6
@dp.callback_query_handler(text="lavclassik6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 132000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Classik  gushtlik lavash uchun 7
@dp.callback_query_handler(text="lavclassik7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 154000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Classik  gushtlik lavash uchun 8
@dp.callback_query_handler(text="lavclassik8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 176000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Classik  gushtlik lavash uchun 9
@dp.callback_query_handler(text="lavclassik9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Go'shtlik Classik lavash jo'natiladi.\nNarxi 198000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu
# Mini  tovuqlik lavash uchun
@dp.callback_query_handler(text="lavminitov")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/10.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button28 )
    #await call.message.answer(f"<b>✅  Narxi:   18 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting!!!</b>",parse_mode='HTML',reply_markup=button28)



##ichki menu3
# Mini  tovuqlik lavash uchun 1


@dp.callback_query_handler(text="lavmini2_1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 1 ta Tovuqlik lavash jo'natiladi.\nNarxi 18000  ming.!!!</b>",parse_mode='HTML',reply_markup=button22)

##Lavash  raqamlar tovuq mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavtovuq")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button16)
    



##ichki menu2
# Mini  tovuqlik lavash uchun 2
@dp.callback_query_handler(text="lavmini2_2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 2 ta Tovuqlik lavash jo'natiladi.\nNarxi 36000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)







##ichki menu2
# Mini  tovuqlik lavash uchun 3
@dp.callback_query_handler(text="lavmini2_3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 3 ta Tovuqlik lavash jo'natiladi.\nNarxi 54000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  tovuqlik lavash uchun 4
@dp.callback_query_handler(text="lavmini2_4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 4 ta Tovuqlik lavash jo'natiladi.\nNarxi 72000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Mini  tovuqlik lavash uchun 5
@dp.callback_query_handler(text="lavmini2_5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 5 ta Tovuqlik lavash jo'natiladi.\nNarxi 90000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)


##ichki menu2
# Mini  tovuqlik lavash uchun 6
@dp.callback_query_handler(text="lavmini2_6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 6 ta Tovuqlik lavash jo'natiladi.\nNarxi 108000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)




##ichki menu2
# Mini  tovuqlik lavash uchun 7
@dp.callback_query_handler(text="lavmini2_7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 7 ta Tovuqlik lavash jo'natiladi.\nNarxi 126000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  tovuqlik lavash uchun 8
@dp.callback_query_handler(text="lavmini2_8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 8 ta Tovuqlik lavash jo'natiladi.\nNarxi 144000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu2
#Mini  tovuqlik lavash uchun 9
@dp.callback_query_handler(text="lavmini2_9")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Sizga 9 ta Tovuqlik lavash jo'natiladi.\nNarxi 162000 ming.!!!</b>",parse_mode='HTML',reply_markup=button22)



##ichki menu
#Mini lavash mol gushi qalampir lavash uchun raqamlar
@dp.callback_query_handler(text="lavmiqalmol")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/11.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button30 )
    #await call.message.answer(f"<b>✅Narxi:   18 000 so'm.\nTarkibi: Xamir, go`sht, garimdor, chips, pomidor, bodring, sous, mayonez,\nMiqdorini tanlang yoki kiriting  </b>",parse_mode='HTML',reply_markup=button30)





#Mini lavash mol gushi qalampir ortga qaytish
@dp.callback_query_handler(text="ortlavminiqalmol")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button15)
    




##ichki menu
#classik lavash mol gushi qalampir lavash uchun raqamlar
@dp.callback_query_handler(text="lavclassikqalmol")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/11.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button31 )
    #await call.message.answer(f"<b>✅Narxi:   22 000 so'm.\nTarkibi: Xamir, go`sht, garimdori, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button31)



#Classik lavash  raqamlar mol gushi qalampir mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavclassikqalmol")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button15)
    




##ichki menu
#mini lavash tovuq gushi qalampir lavash uchun raqamlar
@dp.callback_query_handler(text="lavminiqaltov")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/12.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button40 )
    #await call.message.answer(f"<b>✅ Narxi:   18 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, garimdor, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button40)


#Mini lavash  raqamlar tovuq gushi qalampir mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavminiqaltov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button17)
    


##ichki menu
#classik lavash tovuq gushi qalampir lavash uchun raqamlar
@dp.callback_query_handler(text="lavclassikqaltov")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/12.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button32 )
    #await call.message.answer(f"<b>✅Narxi:   22 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, garimdor, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button32)





#classik lavash  raqamlar tovuq gushi qalampir mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavclassikqaltov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button17)
    


##ichki menu
#mini lavash tovuq gushi pishloq lavash uchun raqamlar
@dp.callback_query_handler(text="lavminipishtov")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/13.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button33 )
    #await call.message.answer(f"<b>✅Narxi:   20 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, chips, pishloq, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button33)


#Classik lavash  raqamlar tovuq gushi pishloq mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavminipishtov")
async def menu_hod(call:CallbackQuery):
        await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button18)
    


##ichki menu
#Classik lavash tovuq gushi pishloq lavash uchun raqamlar
@dp.callback_query_handler(text="lavclassikpishtov")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/13.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button34 )
    #await call.message.answer(f"<b>✅Narxi:   24 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, chips, pishloq, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button34)


#classik lavash  raqamlar tovuq gushi pishloq mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavclassikpishtov")
async def menu_hod(call:CallbackQuery):
        await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button18)
    


##ichki menu
#mini lavash mol gushi pishloq lavash uchun raqamlar
@dp.callback_query_handler(text="lavminipishgusht")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/14.jpg','rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button35 )
    #await call.message.answer(f"<b>✅Narxi:   20 000 so'm.\nTarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button35)


#Mini lavash  raqamlar mol gushi pishloq mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavminipishgusht")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button19)
    



##ichki menu
#mini lavash classik mol gushi pishloq lavash uchun raqamlar
@dp.callback_query_handler(text="lavclassikpishgusht")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/14.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button36 )
    #await call.message.answer(f"<b>✅Narxi:   24 000 so'm.\nTarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez.\nMiqdorini tanlang yoki kiriting</b>",parse_mode='HTML',reply_markup=button36)


#Mini lavash classik raqamlar mol gushi pishloq mini uchun ortga qaytish  
@dp.callback_query_handler(text="ortlavclassikpishgusht")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button19)
    



##ichki menu
#Clasik sendvich uchun raqamlar
@dp.callback_query_handler(text="sendclass")
async def menu_tanlash(call:CallbackQuery):
         await call.message.answer_photo(
        photo=open('images/15.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang""", reply_markup = button39 )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 22 000 so'm.</b>",parse_mode='HTML',reply_markup=button39)


#Classik senvich uchun ortga qaytish  
@dp.callback_query_handler(text="ortsendclass")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Sendvich menusi!!!</b>",parse_mode='HTML',reply_markup=button6)
    




##ichki menu
#Tovuqli  sendvich uchun raqamlar
@dp.callback_query_handler(text="sendtovuq")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/15.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang""", reply_markup = button38 )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 22 000 so'm.</b>",parse_mode='HTML',reply_markup=button38)


#Tovuqli senvich uchun ortga qaytish  
@dp.callback_query_handler(text="ortsendtovuq")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Sendvich menusi!!!</b>",parse_mode='HTML',reply_markup=button6)
    


##ichki menu
#Gamburger uchun raqamlar
@dp.callback_query_handler(text="gambur")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/16.jpg','rb'),
        caption="""Narxi:22000 ming so'm 
Miqdorini tanlang""", reply_markup = gamburger )
    #await call.message.answer(f"<b>✅Narxi: 18 000 so'm.</b>",parse_mode='HTML',reply_markup=gamburger)


#gamburger uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortgambur")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Burger menusi!!!</b>",parse_mode='HTML',reply_markup=button8)



##ichki menu
#Chizburger uchun raqamlar
@dp.callback_query_handler(text="chizbur")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/17.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Miqdorini tanlang""", reply_markup = gamburger )
    #await call.message.answer(f"<b>✅Narxi: 20 000 so'm.</b>",parse_mode='HTML',reply_markup=chizburger)


#Chizburger uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortchizbur")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Burger menusi!!!</b>",parse_mode='HTML',reply_markup=button8)



##ichki menu
#Tovuqli Doner uchun raqamlar
@dp.callback_query_handler(text="dontov")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/18.jpg','rb'),
        caption="""Narxi:23000 ming so'm 
Miqdorini tanlang""", reply_markup = donertov )
    #await call.message.answer(f"<b>✅Doner go'shtlik.\nNarxi: 23 000 so'm.</b>",parse_mode='HTML',reply_markup=donertov)


#Tovuqli doner uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortdontov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Doner menusi!!!</b>",parse_mode='HTML',reply_markup=button9)




##ichki menu
#Gushtli Doner uchun raqamlar
@dp.callback_query_handler(text="donbgush")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/19.jpg','rb'),
        caption="""Narxi:23000 ming so'm 
Miqdorini tanlang""", reply_markup = donergush )
    #await call.message.answer(f"<b>✅Doner go'shtlik.\nNarxi: 23 000 so'm.</b>",parse_mode='HTML',reply_markup=donergush)


#Gushtli doner uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortdonbgush")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Doner menusi!!!</b>",parse_mode='HTML',reply_markup=button9)




##ichki menu
#Fri uchun raqamlar
@dp.callback_query_handler(text="fri")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/20.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""", reply_markup = friuchun )
    #await call.message.answer(f"<b>✅Kartoshka fri.\nNarxi:  6000 so'm.</b>",parse_mode='HTML',reply_markup=friuchun)


#Fri uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortfriraqam")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Gazak menusi!!!</b>",parse_mode='HTML',reply_markup=button10)


##ichki menu
# derevenskiy uchun raqamlar
@dp.callback_query_handler(text="dereven")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/21.jpg','rb'),
        caption="""Narxi:6000 ming so'm 
Miqdorini tanlang""", reply_markup = derevenskiy )
    #await call.message.answer(f"<b>✅Kartoshka fri.\nNarxi:  6000 so'm.</b>",parse_mode='HTML',reply_markup=derevenskiy)


#Fri uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortdereven")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Gazak menusi!!!</b>",parse_mode='HTML',reply_markup=button10)




##ichki menu
#Katta guruch uchun raqamlar
@dp.callback_query_handler(text="katta")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/22.jpg','rb'),
        caption="""Narxi:8000 ming so'm 
Miqdorini tanlang""", reply_markup = guruchkatta )
    #await call.message.answer(f"<b>✅Guruch Katta.\nNarxi:  4000 so'm.</b>",parse_mode='HTML',reply_markup=guruchkatta)


#Fri uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortkatta")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Gazak menusi!!!</b>",parse_mode='HTML',reply_markup=button10)



##ichki menu
#Kichik guruch uchun raqamlar
@dp.callback_query_handler(text="kichik")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/22.jpg','rb'),
        caption="""Narxi:4000 ming so'm 
Miqdorini tanlang""", reply_markup = guruchkichik )
    #await call.message.answer(f"<b>✅Guruch Kichik.\nNarxi:  2000 so'm.</b>",parse_mode='HTML',reply_markup=guruchkichik)


#Kichik guruch uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortkichik")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Gazak menusi!!!</b>",parse_mode='HTML',reply_markup=button10)





##ichki menu
#assalim uchun raqamlar
@dp.callback_query_handler(text="asal")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/23.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang""", reply_markup = assalim )
    #await call.message.answer(f"<b>✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem.\nNarxi: 14 000 so'm</b>",parse_mode='HTML',reply_markup=assalim)


#assalim uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortasal")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Desert menusi!!!</b>",parse_mode='HTML',reply_markup=button12)






##ichki menu
#qulupnay uchun raqamlar
@dp.callback_query_handler(text="qulup")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/24.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Qulupnayli Muss.
Miqdorini tanlang""", reply_markup = qulupnay )
    #await call.message.answer(f"<b>✅Qulupnayli Muss.\nNarxi: 14 000 so'm</b>",parse_mode='HTML',reply_markup=qulupnay)


#qulupnay uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortqulup")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Desert menusi!!!</b>",parse_mode='HTML',reply_markup=button12)






##ichki menu
#choko uchun raqamlar
@dp.callback_query_handler(text="choko")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/25.jpg','rb'),
        caption="""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang""", reply_markup = chokouchun )
    #await call.message.answer(f"<b>✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.\nNarxi: 14 000 so'm</b>",parse_mode='HTML',reply_markup=chokouchun)


#choko uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortchoko")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Desert menusi!!!</b>",parse_mode='HTML',reply_markup=button12)







##ichki menu
#pizza peperoni uchun raqamlar
@dp.callback_query_handler(text="pep")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/26.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца Пепперони\nПицца Пепперони     33см.\nСоус Томатный Для Пиццы\nТонкое тесто.\nСыр 110 гр.
Miqdorini tanlang""", reply_markup = pepucun )
    #await call.message.answer(f"<b>✅Пицца Пепперони\nПицца Пепперони     33см.\nСоус Томатный Для Пиццы\nТонкое тесто.\nСыр 110 гр.\nNarxi: 65 000 so'm</b>",parse_mode='HTML',reply_markup=pepucun)


#pizza peperoni uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortpep")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Pizza menusi!!!</b>",parse_mode='HTML',reply_markup=button13)






##ichki menu
#pizza ananaslik uchun raqamlar
@dp.callback_query_handler(text="ananas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/27.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца с Ананасом.\nПицца с Колбасой     33см.\nСоус Томатный Для Пиццы\n3 вида колбас 130гр.\nТонкое тесто\nКукуруза\nСыр 100гр.\nГрибы\
Miqdorini tanlang""", reply_markup = ananaslik )
    #await call.message.answer(f"<b>✅Пицца с Ананасом.\nПицца с Колбасой     33см.\nСоус Томатный Для Пиццы\n3 вида колбас 130гр.\nТонкое тесто\nКукуруза\nСыр 100гр.\nГрибы\nNarxi: 65 000 so'm</b>",parse_mode='HTML',reply_markup=ananaslik)


#pizza ananaslik uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortananas")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Pizza menusi!!!</b>",parse_mode='HTML',reply_markup=button13)




##ichki menu
#pizza margarita uchun raqamlar
@dp.callback_query_handler(text="margarit")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/28.jpg','rb'),
        caption="""Narxi:65000 ming so'm 
✅Пицца Маргарита\nПицца Маргарита  33см.\nСоус Томатный Для Пиццы \nТонкое тесто \nСыр 100гр.\nПомидоры
Miqdorini tanlang""", reply_markup = ananaslik )
    #await call.message.answer(f"<b>✅Пицца Маргарита\nПицца Маргарита  33см.\nСоус Томатный Для Пиццы \nТонкое тесто \nСыр 100гр.\nПомидоры\nNarxi: 53 000 so'm</b>",parse_mode='HTML',reply_markup=margarita)


#pizza margarita uchun  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortmargarit")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Pizza menusi!!!</b>",parse_mode='HTML',reply_markup=button13)





##ichki menu
#Shaurma uchun1
@dp.callback_query_handler(text="shaurmol")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/29.jpg','rb'),
        caption="""✅Kategoriyalardan birini tanlang!!""", reply_markup = Molgushishaurma )
   #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=Molgushishaurma)

    
##Shaurma mol gushi qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortimolshaurga")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Shaurma menusi!!!</b>",parse_mode='HTML',reply_markup=button7)








##ichki menu
#Shaurma uchun2
@dp.callback_query_handler(text="shaurtovuq")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/30.jpg','rb'),
        caption="""✅Kategoriyalardan birini tanlang!!""", reply_markup = shaurtovuquchun )
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurtovuquchun)

    
##Shaurma mol gushi qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortshaurtovuqga")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Shaurma menusi!!!</b>",parse_mode='HTML',reply_markup=button7)





##ichki menu
#Shaurma uchun3
@dp.callback_query_handler(text="shaurqalampir")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/31.jpg','rb'),
        caption="""✅Kategoriyalardan birini tanlang!!""", reply_markup = shaurmaqalampir )
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurmaqalampir)

    
##Shaurma mol gushi qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortshaurqalampir")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Shaurma menusi!!!</b>",parse_mode='HTML',reply_markup=button7)












##ichki menu
#Shaurma uchun4
@dp.callback_query_handler(text="tovuqshaurqal")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/32.jpg','rb'),
        caption="""✅Kategoriyalardan birini tanlang!!""", reply_markup = shaurqaltov )
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurqaltov)

    
##Shaurma mol gushi qalampir uchun ortga qaytish  
@dp.callback_query_handler(text="ortmollavminiqaltov")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Shaurma menusi!!!</b>",parse_mode='HTML',reply_markup=button7)





##ichki menu
#Shaurma mol gushi mini uchun raqamlar
@dp.callback_query_handler(text="shamolgushimini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/29.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shamolgushimini )
    #await call.message.answer(f"<b>✅Kulcha, go'sht, pomidor, sous,  piyoz\nNarxi: 18 000 so'm</b>",parse_mode='HTML',reply_markup=shamolgushimini)

#Shaurma mol gushi mini  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshamolgushimini")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=Molgushishaurma)





##ichki menu
#Shaurma mol gushi classik uchun raqamlar
@dp.callback_query_handler(text="shamolgushclas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/29.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shamolgushclas )
    #await call.message.answer(f"<b>✅Kulcha, go'sht, pomidor, sous,  piyoz\nNarxi: 18 000 so'm</b>",parse_mode='HTML',reply_markup=shamolgushclas)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshamolgushclas")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=Molgushishaurma)




##ichki menu
#Shaurma mol gushi classik uchun raqamlar
@dp.callback_query_handler(text="shaurtovuqmini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/30.jpg','rb'),
        caption="""Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shaurmatovuqmini )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 18 000 so'm</b>",parse_mode='HTML',reply_markup=shaurmatovuqmini)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshaurtovuqmini")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurtovuquchun)




##ichki menu
#Shaurma mol gushi classik uchun raqamlar
@dp.callback_query_handler(text="shaurtovuqclas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/30.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shaurmatovuq )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 20 000 so'm</b>",parse_mode='HTML',reply_markup=shaurmatovuq)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshaurtovuqclas")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurtovuquchun)




##ichki menu
#Shaurma mol gushi qalampir mini uchun raqamlar
@dp.callback_query_handler(text="shaurqalampirmini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/31.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shaurqalampirmini )
    #await call.message.answer(f"<b>✅Kulcha, mol go'shti, pomidor, sous,  piyoz. \nNarxi: 18 000 so'm</b>",parse_mode='HTML',reply_markup=shaurqalampirmini)

#Shaurma mol gushi mini  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshaurqalampirmini")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurmaqalampir)





##ichki menu
#Shaurma mol gushi qalampir classik uchun raqamlar
@dp.callback_query_handler(text="shaurqalampirclas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/31.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = shaurqalampirclas )
    #await call.message.answer(f"<b>✅Kulcha, mol go'shti, pomidor, sous,  piyoz. \nNarxi: 20 000 so'm</b>",parse_mode='HTML',reply_markup=shaurqalampirclas)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortshaurqalampirclas")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurmaqalampir)





##ichki menu
#Shaurma tovuq gushi qalampir mini uchun raqamlar
@dp.callback_query_handler(text="lavminiqaltovmini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/32.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = lavminiqaltovmini )
    #await call.message.answer(f"<b>✅Kulcha,tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 20 000 so'm</b>",parse_mode='HTML',reply_markup=lavminiqaltovmini)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortlavminiqaltovmini")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurqaltov)







##ichki menu
#Shaurma tovuq gushi qalampir classik uchun raqamlar
@dp.callback_query_handler(text="lavminiqaltovclas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/32.jpg','rb'),
        caption="""Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang""", reply_markup = lavminiqaltovclas )
    #await call.message.answer(f"<b>✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz. \nNarxi: 20 000 so'm</b>",parse_mode='HTML',reply_markup=lavminiqaltovclas)

#Shaurma mol gushi claasik  raqamlar ortga qaytish  
@dp.callback_query_handler(text="ortlavminiqaltovclas")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=shaurqaltov)






##ichki menu
#Choy uchun kichik menu
@dp.callback_query_handler(text="choy")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=choyuchun)

#Choy uchun kichik menu ortga qaytish  
@dp.callback_query_handler(text="ortchoy")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)





##ichki menu
#Choy uchun kichik menu
@dp.callback_query_handler(text="yaxna")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=yaxnauchun)

#Choy uchun kichik menu ortga qaytish  
@dp.callback_query_handler(text="ortyaxnauchun")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)






##ichki menu
#Freshlar uchun kichik menu
@dp.callback_query_handler(text="fresh")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=freshuchun)

#Choy uchun kichik menu ortga qaytish  
@dp.callback_query_handler(text="ortfresh")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)






##ichki menu
#Kofelar uchun kichik menu
@dp.callback_query_handler(text="kofemitti")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=kofelarucun)

#Choy uchun kichik menu ortga qaytish  
@dp.callback_query_handler(text="ortkofelarucun")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=choyuchun)





##ichki menu
#choylar uchun kichik menu
@dp.callback_query_handler(text="choymitti")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=coyuchun)

#Choy uchun kichik menu ortga qaytish  
@dp.callback_query_handler(text="ortcoyuchun")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=choyuchun)







##ichki menu
#Fanta uchun raqamlar
@dp.callback_query_handler(text="fanta")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/33.jpg','rb'),
        caption="""11000 narxi""", reply_markup = fantauchun )
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=fantauchun)

#Fanta uchun  ortga qaytish  
@dp.callback_query_handler(text="ortfanta")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=yaxnauchun)






##ichki menu
#Sprite uchun raqamlar
@dp.callback_query_handler(text="sprite")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/34.jpg','rb'),
        caption="""11000 narxi""", reply_markup = spriteuchun) 
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=spriteuchun)

#Sprite uchun  ortga qaytish  
@dp.callback_query_handler(text="ortsprite")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=yaxnauchun)



##ichki menu
#cola uchun raqamlar
@dp.callback_query_handler(text="cola")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/35.jpg','rb'),
        caption="""11000 narxi""", reply_markup = colaucun)
    #await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=colaucun)

#Cola uchun  ortga qaytish  
@dp.callback_query_handler(text="ortcola")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=yaxnauchun)


##ichki menu
#nestle uchun raqamlar
@dp.callback_query_handler(text="nestle")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/36.jpg','rb'),
        caption="""4000 narxi""", reply_markup = nestle)
   # await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=nestle)

#Nestle uchun  ortga qaytish  
@dp.callback_query_handler(text="ortnestle")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=yaxnauchun)



##ichki menu
#fresh uchun raqamlar
@dp.callback_query_handler(text="freshcha")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/37.jpg','rb'),
        caption="""✅Sok Bliss 10000mig so'm!!!""", reply_markup = freshcha)
    #await call.message.answer(f"<b>✅Sok Bliss 10000mig so'm!!!</b>",parse_mode='HTML',reply_markup=freshcha)

#Fresh uchun  ortga qaytish  
@dp.callback_query_handler(text="ortfreshcha")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)





##ichki menu
#fresholma uchun raqamlar
@dp.callback_query_handler(text="fresholma")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/38.jpg','rb'),
        caption="""✅Fresh sabzi + olma 13000mig so'm!!!""", reply_markup = fresholma)
    #await call.message.answer(f"<b>✅Fresh sabzi + olma 13000mig so'm!!!</b>",parse_mode='HTML',reply_markup=fresholma)

#Fresh olma uchun  ortga qaytish  
@dp.callback_query_handler(text="ortfresholma")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Marxamat Ichimliklar menusi!!!</b>",parse_mode='HTML',reply_markup=button11)





##ichki menu
#Americano kofe uchun raqamlar
@dp.callback_query_handler(text="amerika")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/39.jpg','rb'),
        caption="""✅Ameicani narxi 12000!!!!!!""", reply_markup = amerika)
    #await call.message.answer(f"<b>✅Ameicani narxi 12000!!!</b>",parse_mode='HTML',reply_markup=amerika)

#Americano uchun  ortga qaytish  
@dp.callback_query_handler(text="ortamerika")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=kofelarucun)




##ichki menu
#Coppuccino kofe uchun raqamlar
@dp.callback_query_handler(text="cappu")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/40.jpg','rb'),
        caption="""✅Coppuccino Narxi 18000!!!!!!""", reply_markup = cappuci)
    #await call.message.answer(f"<b>✅Coppuccino Narxi 18000!!!</b>",parse_mode='HTML',reply_markup=cappuci)

#Cappuccino uchun  ortga qaytish  
@dp.callback_query_handler(text="ortcappu")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=kofelarucun)





##ichki menu
#Kofe3v1 kofe uchun raqamlar
@dp.callback_query_handler(text="cofe")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/41.jpg','rb'),
        caption="""✅Kofe 3 v 1☕️ 3000ming so'm!!!!""", reply_markup = cofe)
    #await call.message.answer(f"<b>✅Kofe 3 v 1☕️ 3000ming so'm!!!</b>",parse_mode='HTML',reply_markup=cofe)

#Kofe3v1 uchun  ortga qaytish  
@dp.callback_query_handler(text="ortcofe")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=kofelarucun)



##ichki menu
#kuk choy kofe uchun raqamlar
@dp.callback_query_handler(text="latte")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/42.jpg','rb'),
        caption="""✅Latte big 120g☕️ 15000mig so'm!!!!""", reply_markup = latte)
    #await call.message.answer(f"<b>✅Choy ko'k 3000mig so'm!!!</b>",parse_mode='HTML',reply_markup=latte)

#Latte uchun  ortga qaytish  
@dp.callback_query_handler(text="ortko'k")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=ortlatte)





##ichki menu
#kuk choy kofe uchun raqamlar
@dp.callback_query_handler(text="ko'k")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/43.jpg','rb'),
        caption="""✅Choy ko'k 3000mig so'm!!!!""", reply_markup = kukchoy)
    #await call.message.answer(f"<b>✅Choy ko'k 3000mig so'm!!!</b>",parse_mode='HTML',reply_markup=kukchoy)

#Latte uchun  ortga qaytish  
@dp.callback_query_handler(text="ortko'k")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=coyuchun)


##ichki menu
#kuk choy kofe uchun raqamlar
@dp.callback_query_handler(text="qora")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/43.jpg','rb'),
        caption="""✅ Ko'k  choy 3000mig so'm!!!""", reply_markup = qora)
    #await call.message.answer(f"<b>✅Qora ko'k 3000mig so'm!!!</b>",parse_mode='HTML',reply_markup=qora)

#Latte uchun  ortga qaytish  
@dp.callback_query_handler(text="ortqora")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=coyuchun)





##ichki menu
#Limon choy kofe uchun raqamlar
@dp.callback_query_handler(text="limon")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/44.jpg','rb'),
        caption="""✅Limon choy 5000mig so'm!!""", reply_markup = qora)
    #await call.message.answer(f"<b>✅Limon choy 5000mig so'm!!!</b>",parse_mode='HTML',reply_markup=limon)

#Limon uchun  ortga qaytish  
@dp.callback_query_handler(text="ortlimon")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=coyuchun)




##ichki menu
#lavash tovuq gushi classik uchun raqamlar
@dp.callback_query_handler(text="lavclassiktov")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/10.jpg','rb'),
        caption="""Narxi:20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup = button29 )
    #await call.message.answer(f"<b>✅Narxi:   22 000 so'm.\nTarkibi: Xamir, Tovuq go`sht, chips, pomidor, bodring, sous, mayonez!!!</b>",parse_mode='HTML',reply_markup=button29)

#lavash tovuq gushi classik  ortga qaytish  
@dp.callback_query_handler(text="ortlavtovuqclassik")
async def menu_hod(call:CallbackQuery):
    await call.message.answer(f"<b>✅Kategoriyalardan birini tanlang!!!</b>",parse_mode='HTML',reply_markup=button19)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





