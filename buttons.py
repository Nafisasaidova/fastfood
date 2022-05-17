from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


##Til
til=ReplyKeyboardMarkup(
   keyboard = [
	[
	KeyboardButton( text="🇸🇱 O'zbekcha"),
  

	],

	],
	resize_keyboard=True
)


##3 talik knopka
button2=ReplyKeyboardMarkup(
	   keyboard = [
	[
	     KeyboardButton( text="Buyurtma berish 👩‍💻")
	], 
	[

	KeyboardButton( text="Sozlamalar🛠"),
    KeyboardButton( text="Biz bilan aloqa☎️")

	],

	],
	resize_keyboard=True
)

##fast food ruyhati
button3=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Lavash 🌯🌯",callback_data="lav"),
    InlineKeyboardButton( text="Hod Dog 🌭🌭",callback_data="hod"),

	], 
	[

	InlineKeyboardButton( text="Sendvich club 🥪🥪 ",callback_data="send"),
    InlineKeyboardButton( text="Shaurma 🌮🌮",callback_data="shaur"),

	],

 
	[

	InlineKeyboardButton( text="Burger 🍔🍔 ",callback_data="bur"),
    InlineKeyboardButton( text="Donar 🍱🍱",callback_data="don"),
],
	
[

    InlineKeyboardButton( text="Gazaklar 🍟🍟 ",callback_data="gazak"),
    InlineKeyboardButton( text="Ichimliklar 🍹🍹",callback_data="ich"),
],

[
    InlineKeyboardButton( text="Desertlar 🍰🍰",callback_data="des"),
    InlineKeyboardButton( text="Pizza 🍕🍕",callback_data="piz"),
],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortbuyurtma"),
],   
] )

##Lavash uchun
button4=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mol Go'shtlik 🥩",callback_data="mgl"),
    InlineKeyboardButton( text="Qalampirli mol go'sht 🥩🌶",callback_data="mgql"),

	], 
	[

	InlineKeyboardButton( text="Tovuq Go'shtlik 🍗",callback_data="tovl"),
    InlineKeyboardButton( text="Qalampirli tovuq go'sht🍗🌶",callback_data="tgql"),

	],

 
	[

	InlineKeyboardButton( text="Pishloqli tovuq go'shti🍗🧀 ",callback_data="tovpl"),
    InlineKeyboardButton( text="Pishloqli mol go'shti 🥩🧀",callback_data="mgpl"),
],
	
[

    InlineKeyboardButton( text="Fitter 🥬 ",callback_data="fit"),
],   
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavash"),
],   
])



##Hod dog uchun
button5=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Hod Dog Baget Dabl👍",callback_data="hodbag"),
    InlineKeyboardButton( text="Classik Hod Dog 👍",callback_data="hodclass"),

	], 
	[

	InlineKeyboardButton( text="Korolevskiy👍",callback_data="korol"),
    InlineKeyboardButton( text="Tovuqli Hod Dog👍",callback_data="tovuqhod"),

], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="orthoddog"),
],   
])  



##Sendvich uchun
button6=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Classik Sendvich Club👍",callback_data="sendclass"),
    InlineKeyboardButton( text="Tovuqli Sendvich👍",callback_data="sendtovuq")

],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortsendvich"),
],   
])     



##Shaurma uchun
button7=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mol Go'shtli Shaurma👍",callback_data="shaurmol"),
    InlineKeyboardButton( text="Tovuq Shaurma👍",callback_data="shaurtovuq"),

	], 
	[

	InlineKeyboardButton( text="Mol Go'shti+qalampir👍",callback_data="shaurqalampir"),
    InlineKeyboardButton( text="Tovuq Go'shti+qalampir👍",callback_data="tovuqshaurqal"),

],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurma"),
],      
])


##Burger uchun
button8=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Gamburger👍",callback_data="gambur"),
    InlineKeyboardButton( text="Chizburger👍",callback_data="chizbur")

], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortBurger"),
],        
])



##Doner uchun
button9=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Tovuqli👍",callback_data="dontov"),
    InlineKeyboardButton( text="Go'shtli👍",callback_data="donbgush")

], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortdoner"),
],        
])


#Gazak uchun
button10=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="15 gram Fri👍",callback_data="fri"),
    InlineKeyboardButton( text="Kartoshka Derevenskiy👍",callback_data="dereven"),

	], 
	[

	InlineKeyboardButton( text="Guruch katta 👍",callback_data="katta"),
    InlineKeyboardButton( text="Guruch kichik👍",callback_data="kichik"),

], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortgazak"),
],      
])


#Desert uchun
button12=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Assalim👍",callback_data="asal"),
    InlineKeyboardButton( text="Qulupnay👍",callback_data="qulup"),

	], 
	[

	InlineKeyboardButton( text="Choko 👍",callback_data="choko"),
    
], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortdesert"),
],        
])


#Pitsa uchun
button13=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Peperoni👍",callback_data="pep"),
    InlineKeyboardButton( text="Ananaslik👍",callback_data="ananas"),

	], 
	[

	InlineKeyboardButton( text="Margaritta 👍",callback_data="margarit"),
    
],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortpissa"),
],     
])

#Icimliklar  uchun
button11=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Choy va kofe👍",callback_data="choy"),
    InlineKeyboardButton( text="Yaxna ichimliklar👍",callback_data="yaxna"),

	], 
	[

	InlineKeyboardButton( text="Fresh va tabiiy soklar👍",callback_data="fresh"),
    
],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortichimlik"),
],    
])

##Lavash uchun icki menu1
button14=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavmini"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassik")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortimollavash"),
],     
])


##Lavash uchun icki menu2
button15=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavmiqalmol"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassikqalmol")

],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortimolqal"),
],    
])




##Lavash uchun icki menu3
button16=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavminitov"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassiktov")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortilavtovuq"),
],    
])


##Lavash tovuq qalampir uchun icki menu4
button17=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavminiqaltov"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassikqaltov")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortilavqaltov"),
],     
])


##Lavash tovuqli pishloqli uchun icki menu5
button18=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavminipishtov"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassikpishtov")

], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortilavpishtov"),
],    
])



##Lavash mol gushi pishloq uchun icki menu6
button19=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavminipishgusht"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavclassikpishgusht")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortilavpishmol"),
],     
])





##Hod dog uchun raqamlar 1
button21=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="hod1"),
    InlineKeyboardButton( text="2️⃣",callback_data="hod2"),
    InlineKeyboardButton( text="3️⃣",callback_data="hod3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="dog4"),
    InlineKeyboardButton( text="5️⃣",callback_data="dog5"),
	InlineKeyboardButton( text="6️⃣",callback_data="dog6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="dog7"),
    InlineKeyboardButton( text="8️⃣",callback_data="dog8"),
	InlineKeyboardButton( text="9️⃣",callback_data="dog9"),


],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="orthoddograq"),
],     
])

button22=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="☎️Raqam Qoldiring!!!",callback_data="raqam"),
    InlineKeyboardButton( text="🏠Manzil qoldiring!!!",callback_data="manzil")

],   
])


##Hod dog uchun raqamlar 2
button23=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="hodclass1"),
    InlineKeyboardButton( text="2️⃣",callback_data="hodclass2"),
    InlineKeyboardButton( text="3️⃣",callback_data="hodclass3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="hodclass4"),
    InlineKeyboardButton( text="5️⃣",callback_data="hodclass5"),
	InlineKeyboardButton( text="6️⃣",callback_data="hodclass6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="hodclass7"),
    InlineKeyboardButton( text="8️⃣",callback_data="hodclass8"),
	InlineKeyboardButton( text="9️⃣",callback_data="hodclass9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="orthoddogclassik"),
],       
])




##Hod dog uchun raqamlar 3
button24=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="korol1"),
    InlineKeyboardButton( text="2️⃣",callback_data="korol2"),
    InlineKeyboardButton( text="3️⃣",callback_data="korol3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="korol4"),
    InlineKeyboardButton( text="5️⃣",callback_data="korol5"),
	InlineKeyboardButton( text="6️⃣",callback_data="korol6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="korol7"),
    InlineKeyboardButton( text="8️⃣",callback_data="korol8"),
	InlineKeyboardButton( text="9️⃣",callback_data="korol9"),


],   
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="orthoddogkorol"),
],     
])



##Hod dog uchun raqamlar 4
button25=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="tovuqhod1"),
    InlineKeyboardButton( text="2️⃣",callback_data="tovuqhod2"),
    InlineKeyboardButton( text="3️⃣",callback_data="tovuqhod3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="tovuqhod4"),
    InlineKeyboardButton( text="5️⃣",callback_data="tovuqhod5"),
	InlineKeyboardButton( text="6️⃣",callback_data="tovuqhod6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="tovuqhod7"),
    InlineKeyboardButton( text="8️⃣",callback_data="tovuqhod8"),
	InlineKeyboardButton( text="9️⃣",callback_data="tovuqhod9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="orthoddogtovuq"),
],     
])




##Mini lavash mol gushti uchun raqamlar 1
button26=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavmini1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavmini2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavmini3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavmini4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavmini5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavmini6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavmini7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavmini8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavmini9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavmini"),
],       
])





##Classik lavash mol gushti uchun raqamlar 2
button27=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassik1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassik2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassik3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassik4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassik5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassik6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassik7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassik8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassik9"),


],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavclassik"),
],          
])


##Mini lavash tovuq gushti uchun raqamlar 1
button28=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavmini2_1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavmini2_2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavmini2_3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavmini2_4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavmini2_5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavmini2_6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavmini2_7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavmini2_8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavmini2_9"),


],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavtovuq"),
],     
])





##Classik lavash tovuq gushti uchun raqamlar 2
button29=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassik2_1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassik2_2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassik2_3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassik2_4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassik2_5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassik2_6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassik2_7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassik2_8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassik2_9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavtovuqclassik"),
],     
])


##Mini lavash mol qalampir gushti uchun raqamlar 2
button30=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavmiqalmol1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavmiqalmol2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavmiqalmol3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavmiqalmol4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavmiqalmol5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavmiqalmol6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavmiqalmol7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavmiqalmol8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavmiqalmol9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminiqalmol"),
],     
])


##Classik lavash mol gushti qalampir uchun raqamlar 2
button31=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassikqalmol1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassikqalmol2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassikqalmol3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassikqalmol4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassikqalmol5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassikqalmol6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassikqalmol7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassikqalmol8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassikqalmol9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavclassikqalmol"),
],     
])



##Mini lavash tovuq gushti qalampir uchun raqamlar 2
button32=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassikqaltov1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassikqaltov2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassikqaltov3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassikqaltov4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassikqaltov5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassikqaltov6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassikqaltov7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassikqaltov8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassikqaltov9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavclassikqaltov"),
],     
])




##Mini lavash tovuq gushti pishloqlik uchun raqamlar 2
button33=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavminipishtov1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavminipishtov2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavminipishtov3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavminipishtov4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavminipishtov5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavminipishtov6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavminipishtov7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavminipishtov8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavminipishtov9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminipishtov"),
],     
])



##classik lavash tovuq gushti pishloqlik uchun raqamlar 2
button34=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassikpishtov1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassikpishtov2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassikpishtov3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassikpishtov4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassikpishtov5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassikpishtov6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassikpishtov7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassikpishtov8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassikpishtov9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavclassikpishtov"),
],     
])




##Mini lavash mol gushti pishloqlik uchun raqamlar 2
button35=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavminipishgusht1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavminipishgusht2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavminipishgusht3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavminipishgusht4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavminipishgusht5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavminipishgusht6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavminipishgusht7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavminipishgusht8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavminipishgusht9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminipishgusht"),
],     
])



##Classik lavash mol gushti pishloqlik uchun raqamlar 2
button36=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavclassikpishgusht1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavclassikpishgusht2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavclassikpishgusht3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavclassikpishgusht4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavclassikpishgusht5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavclassikpishgusht6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavclassikpishgusht7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavclassikpishgusht8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavclassikpishgusht9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavclassikpishgusht"),
],     
])




##Lavash flitter uchun raqamlar 2
button37=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="fit1"),
    InlineKeyboardButton( text="2️⃣",callback_data="fit2"),
    InlineKeyboardButton( text="3️⃣",callback_data="fit3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="fit4"),
    InlineKeyboardButton( text="5️⃣",callback_data="fit5"),
	InlineKeyboardButton( text="6️⃣",callback_data="fit6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="fit7"),
    InlineKeyboardButton( text="8️⃣",callback_data="fit8"),
	InlineKeyboardButton( text="9️⃣",callback_data="fit9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortflit"),
],     
])


##Sendvich tovuqli uchun raqamlar 2
button38=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="sendtovuq1"),
    InlineKeyboardButton( text="2️⃣",callback_data="sendtovuq2"),
    InlineKeyboardButton( text="3️⃣",callback_data="sendtovuq3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="sendtovuq4"),
    InlineKeyboardButton( text="5️⃣",callback_data="sendtovuq5"),
	InlineKeyboardButton( text="6️⃣",callback_data="sendtovuq6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="sendtovuq7"),
    InlineKeyboardButton( text="8️⃣",callback_data="sendtovuq8"),
	InlineKeyboardButton( text="9️⃣",callback_data="sendtovuq9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortsendtovuq"),
],     
])



##Sendvich classik uchun raqamlar 2
button39=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="sendclass1"),
    InlineKeyboardButton( text="2️⃣",callback_data="sendclass2"),
    InlineKeyboardButton( text="3️⃣",callback_data="sendclass3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="sendclass4"),
    InlineKeyboardButton( text="5️⃣",callback_data="sendclass5"),
	InlineKeyboardButton( text="6️⃣",callback_data="sendclass6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="sendclass7"),
    InlineKeyboardButton( text="8️⃣",callback_data="sendclass8"),
	InlineKeyboardButton( text="9️⃣",callback_data="sendclass9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortsendclass"),
],     
])



##Mini lavash tovuq gushti qalampir uchun raqamlar 2
button40=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavminiqaltov1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavminiqaltov2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavminiqaltov3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavminiqaltov4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavminiqaltov5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavminiqaltov5"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavminiqaltov7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavminiqaltov8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavminiqaltov9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminiqaltov"),
],     
])



##Gamburger uchun raqamlar 
gamburger=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="gambur1"),
    InlineKeyboardButton( text="2️⃣",callback_data="gambur2"),
    InlineKeyboardButton( text="3️⃣",callback_data="gambur3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="gambur4"),
    InlineKeyboardButton( text="5️⃣",callback_data="gambur5"),
	InlineKeyboardButton( text="6️⃣",callback_data="gambur6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="gambur7"),
    InlineKeyboardButton( text="8️⃣",callback_data="gambur8"),
	InlineKeyboardButton( text="9️⃣",callback_data="gambur9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortgambur"),
],     
])



##Chizburger uchun raqamlar 
chizburger=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="chizbur1"),
    InlineKeyboardButton( text="2️⃣",callback_data="chizbur2"),
    InlineKeyboardButton( text="3️⃣",callback_data="chizbur3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="chizbur4"),
    InlineKeyboardButton( text="5️⃣",callback_data="chizbur5"),
	InlineKeyboardButton( text="6️⃣",callback_data="chizbur6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="chizbur7"),
    InlineKeyboardButton( text="8️⃣",callback_data="chizbur8"),
	InlineKeyboardButton( text="9️⃣",callback_data="chizbur9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortchizbur"),
],     
])




##Doner uchun raqamlar 
donertov=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="dontov1"),
    InlineKeyboardButton( text="2️⃣",callback_data="dontov2"),
    InlineKeyboardButton( text="3️⃣",callback_data="dontov3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="dontov4"),
    InlineKeyboardButton( text="5️⃣",callback_data="dontov5"),
	InlineKeyboardButton( text="6️⃣",callback_data="dontov6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="dontov7"),
    InlineKeyboardButton( text="8️⃣",callback_data="dontov8"),
	InlineKeyboardButton( text="9️⃣",callback_data="dontov9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortdontov"),
],     
])



##Doner uchun raqamlar 2
donergush=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="donbgush1"),
    InlineKeyboardButton( text="2️⃣",callback_data="donbgush2"),
    InlineKeyboardButton( text="3️⃣",callback_data="donbgush3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="donbgush4"),
    InlineKeyboardButton( text="5️⃣",callback_data="donbgush5"),
	InlineKeyboardButton( text="6️⃣",callback_data="donbgush6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="donbgush7"),
    InlineKeyboardButton( text="8️⃣",callback_data="donbgush8"),
	InlineKeyboardButton( text="9️⃣",callback_data="donbgush9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortdonbgush"),
],     
])



##Gazak uchun raqamlar 1
friuchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="fri1"),
    InlineKeyboardButton( text="2️⃣",callback_data="fri2"),
    InlineKeyboardButton( text="3️⃣",callback_data="fri3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="fri4"),
    InlineKeyboardButton( text="5️⃣",callback_data="fri5"),
	InlineKeyboardButton( text="6️⃣",callback_data="fri6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="fri7"),
    InlineKeyboardButton( text="8️⃣",callback_data="fri8"),
	InlineKeyboardButton( text="9️⃣",callback_data="fri9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortfriraqam"),
],     
])



##Gazak uchun raqamlar 1
derevenskiy=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="dereven1"),
    InlineKeyboardButton( text="2️⃣",callback_data="dereven2"),
    InlineKeyboardButton( text="3️⃣",callback_data="dereven3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="dereven4"),
    InlineKeyboardButton( text="5️⃣",callback_data="dereven5"),
	InlineKeyboardButton( text="6️⃣",callback_data="dereven6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="dereven7"),
    InlineKeyboardButton( text="8️⃣",callback_data="dereven8"),
	InlineKeyboardButton( text="9️⃣",callback_data="dereven9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortdereven"),
],     
])



##Gazak uchun raqamlar 3
guruchkatta=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="katta1"),
    InlineKeyboardButton( text="2️⃣",callback_data="katta2"),
    InlineKeyboardButton( text="3️⃣",callback_data="katta3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="katta4"),
    InlineKeyboardButton( text="5️⃣",callback_data="katta5"),
	InlineKeyboardButton( text="6️⃣",callback_data="katta6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="katta7"),
    InlineKeyboardButton( text="8️⃣",callback_data="katta8"),
	InlineKeyboardButton( text="9️⃣",callback_data="katta9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortkatta"),
],     
])



##Gazak uchun raqamlar 3
guruchkichik=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="kichik1"),
    InlineKeyboardButton( text="2️⃣",callback_data="kichik2"),
    InlineKeyboardButton( text="3️⃣",callback_data="kichik3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="kichik4"),
    InlineKeyboardButton( text="5️⃣",callback_data="kichik5"),
	InlineKeyboardButton( text="6️⃣",callback_data="kichik6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="kichik7"),
    InlineKeyboardButton( text="8️⃣",callback_data="kichik8"),
	InlineKeyboardButton( text="9️⃣",callback_data="kichik9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortkichik"),
],     
])


#Assalim uchun raqamlar 3
assalim=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="asal1"),
    InlineKeyboardButton( text="2️⃣",callback_data="asal2"),
    InlineKeyboardButton( text="3️⃣",callback_data="asal3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="asal4"),
    InlineKeyboardButton( text="5️⃣",callback_data="asal5"),
	InlineKeyboardButton( text="6️⃣",callback_data="asal6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="asal7"),
    InlineKeyboardButton( text="8️⃣",callback_data="asal8"),
	InlineKeyboardButton( text="9️⃣",callback_data="asal9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortasal"),
],     
])




#Quluonay uchun raqamlar 3
qulupnay=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="qulup1"),
    InlineKeyboardButton( text="2️⃣",callback_data="qulup2"),
    InlineKeyboardButton( text="3️⃣",callback_data="qulup3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="qulup4"),
    InlineKeyboardButton( text="5️⃣",callback_data="qulup5"),
	InlineKeyboardButton( text="6️⃣",callback_data="qulup6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="qulup7"),
    InlineKeyboardButton( text="8️⃣",callback_data="qulup8"),
	InlineKeyboardButton( text="9️⃣",callback_data="qulup9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortqulup"),
],     
])





#Choko uchun raqamlar 3
chokouchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="choko1"),
    InlineKeyboardButton( text="2️⃣",callback_data="choko2"),
    InlineKeyboardButton( text="3️⃣",callback_data="choko3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="choko4"),
    InlineKeyboardButton( text="5️⃣",callback_data="choko5"),
	InlineKeyboardButton( text="6️⃣",callback_data="choko6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="choko7"),
    InlineKeyboardButton( text="8️⃣",callback_data="choko8"),
	InlineKeyboardButton( text="9️⃣",callback_data="choko9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortchoko"),
],     
])

	

#Peperoni  uchun raqamlar 3
pepucun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="pep1"),
    InlineKeyboardButton( text="2️⃣",callback_data="pep2"),
    InlineKeyboardButton( text="3️⃣",callback_data="pep3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="pep4"),
    InlineKeyboardButton( text="5️⃣",callback_data="pep5"),
	InlineKeyboardButton( text="6️⃣",callback_data="pep6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="pep7"),
    InlineKeyboardButton( text="8️⃣",callback_data="pep8"),
	InlineKeyboardButton( text="9️⃣",callback_data="pep9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortpep"),
],     
])

	
	
#Ananaslik  uchun raqamlar 3
ananaslik=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="ananas1"),
    InlineKeyboardButton( text="2️⃣",callback_data="ananas2"),
    InlineKeyboardButton( text="3️⃣",callback_data="ananas3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="ananas4"),
    InlineKeyboardButton( text="5️⃣",callback_data="ananas5"),
	InlineKeyboardButton( text="6️⃣",callback_data="ananas6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="ananas7"),
    InlineKeyboardButton( text="8️⃣",callback_data="ananas8"),
	InlineKeyboardButton( text="9️⃣",callback_data="ananas9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortananas"),
],     
])


#Margarita  uchun raqamlar 3
margarita=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="margarit1"),
    InlineKeyboardButton( text="2️⃣",callback_data="margarit2"),
    InlineKeyboardButton( text="3️⃣",callback_data="margarit3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="margarit4"),
    InlineKeyboardButton( text="5️⃣",callback_data="margarit5"),
	InlineKeyboardButton( text="6️⃣",callback_data="margarit6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="margarit7"),
    InlineKeyboardButton( text="8️⃣",callback_data="margarit8"),
	InlineKeyboardButton( text="9️⃣",callback_data="margarit9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortmargarit"),
],     
])   

    





##Shairma uchun icki menu1
Molgushishaurma=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="shamolgushimini"),
    InlineKeyboardButton( text="Classsik👍",callback_data="shamolgushclas")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortimolshaurga"),
],     
])


##Lavash uchun icki menu2
shaurtovuquchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="shaurtovuqmini"),
    InlineKeyboardButton( text="Classsik👍",callback_data="shaurtovuqclas")

],
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurtovuqga"),
],    
])




##Lavash uchun icki menu3
shaurmaqalampir=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="shaurqalampirmini"),
    InlineKeyboardButton( text="Classsik👍",callback_data="shaurqalampirclas")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurqalampir"),
],    
])


##Lavash tovuq qalampir uchun icki menu4
shaurqaltov=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Mini👍",callback_data="lavminiqaltovmini"),
    InlineKeyboardButton( text="Classsik👍",callback_data="lavminiqaltovclas")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortmollavminiqaltov"),
],     
])







#Mol gushi classik shaurma  uchun raqamlar 3
shamolgushimini=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shamolgushimini1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shamolgushimini2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shamolgushimini3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shamolgushimini4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shamolgushimini5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shamolgushimini6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shamolgushimini7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shamolgushimini8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shamolgushimini9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshamolgushimini"),
],     
])   

    





#Mol gushi classik shaurma  uchun raqamlar 3
shamolgushclas=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shamolgushclas1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shamolgushclas2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shamolgushclas3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shamolgushclas4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shamolgushclas5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shamolgushclas6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shamolgushclas7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shamolgushclas8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shamolgushclas9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshamolgushclas"),
],     
])   







#Tovuq  gushi mini shaurma  uchun raqamlar 3
shaurmatovuqmini=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shaurtovuqmini1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shaurtovuqmini2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shaurtovuqmini3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shaurtovuqmini4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shaurtovuqmini5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shaurtovuqmini6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shaurtovuqmini7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shaurtovuqmini8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shaurtovuqmini9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurtovuqmini"),
],     
])   





#Tovuq  gushi mini shaurma  uchun raqamlar 3
shaurmatovuq=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shaurtovuqclas1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shaurtovuqclas2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shaurtovuqclas3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shaurtovuqclas4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shaurtovuqclas5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shaurtovuqclas6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shaurtovuqclas7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shaurtovuqclas8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shaurtovuqclas9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurtovuqclas"),
],     
])   









#Mol  gushi qalampir mini shaurma  uchun raqamlar 3
shaurqalampirmini=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shaurqalampirmini1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shaurqalampirmini2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shaurqalampirmini3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shaurqalampirmini4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shaurqalampirmini5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shaurqalampirmini6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shaurqalampirmini7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shaurqalampirmini8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shaurqalampirmini9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurqalampirmini"),
],     
])   





#Mol  gushi qalampir classik shaurma  uchun raqamlar 3
shaurqalampirclas=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="shaurqalampirclas1"),
    InlineKeyboardButton( text="2️⃣",callback_data="shaurqalampirclas2"),
    InlineKeyboardButton( text="3️⃣",callback_data="shaurqalampirclas3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="shaurqalampirclas4"),
    InlineKeyboardButton( text="5️⃣",callback_data="shaurqalampirclas5"),
	InlineKeyboardButton( text="6️⃣",callback_data="shaurqalampirclas6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="shaurqalampirclas7"),
    InlineKeyboardButton( text="8️⃣",callback_data="shaurqalampirclas8"),
	InlineKeyboardButton( text="9️⃣",callback_data="shaurqalampirclas9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortshaurqalampirclas"),
],     
])   



#Tovuq  gushi qalampir mini shaurma  uchun raqamlar 3
lavminiqaltovmini=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavminiqaltovmini1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavminiqaltovmini2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavminiqaltovmini3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavminiqaltovmini4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavminiqaltovmini5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavminiqaltovmini6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavminiqaltovmini7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavminiqaltovmini8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavminiqaltovmini9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminiqaltovmini"),
],     
])   




#Tovuq  gushi qalampir mini shaurma  uchun raqamlar 3
lavminiqaltovclas=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="lavminiqaltovclas1"),
    InlineKeyboardButton( text="2️⃣",callback_data="lavminiqaltovclas2"),
    InlineKeyboardButton( text="3️⃣",callback_data="lavminiqaltovclas3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="lavminiqaltovclas4"),
    InlineKeyboardButton( text="5️⃣",callback_data="lavminiqaltovclas5"),
	InlineKeyboardButton( text="6️⃣",callback_data="lavminiqaltovclas6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="lavminiqaltovclas7"),
    InlineKeyboardButton( text="8️⃣",callback_data="lavminiqaltovclas8"),
	InlineKeyboardButton( text="9️⃣",callback_data="lavminiqaltovclas9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlavminiqaltovclas"),
],     
])   



#Choy2
choyuchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Kofelar👍",callback_data="kofemitti"),
    InlineKeyboardButton( text="Choylar👍",callback_data="choymitti")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortchoy"),
],     
])




#Choy2
yaxnauchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Fanta👍",callback_data="fanta"),
    InlineKeyboardButton( text="Sprite👍",callback_data="sprite")

],  
[
	InlineKeyboardButton( text="Coca Cola👍",callback_data="cola"),
    InlineKeyboardButton( text="Nestle👍",callback_data="nestle")

],  

[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortyaxnauchun"),
],     
])



#Choy2
freshuchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Bliss sok 1l👍",callback_data="freshcha"),
    InlineKeyboardButton( text="Olma va sabzi fresh👍",callback_data="fresholma")

],  
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortfresh"),
],     
])




#Kofelar uchun
kofelarucun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Americano👍",callback_data="amerika"),
    InlineKeyboardButton( text="Cappuccino👍",callback_data="cappu")

],  
[
	InlineKeyboardButton( text="Cofe 3v1👍",callback_data="cofe"),
    InlineKeyboardButton( text="Latte👍",callback_data="latte")

],  

[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortkofelarucun"),
],     
])




 

	
#Choy2
coyuchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="Ko'k choy👍",callback_data="ko'k"),
    InlineKeyboardButton( text="Qora choy👍",callback_data="qora")

],  
[
	InlineKeyboardButton( text="Limon choy👍",callback_data="limon"),
    

],  

[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortcoyuchun"),
],     
])




#Fanta  uchun raqamlar 3
fantauchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="fanta1"),
    InlineKeyboardButton( text="2️⃣",callback_data="fanta2"),
    InlineKeyboardButton( text="3️⃣",callback_data="fanta3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="fanta4"),
    InlineKeyboardButton( text="5️⃣",callback_data="fanta5"),
	InlineKeyboardButton( text="6️⃣",callback_data="fanta6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="fanta7"),
    InlineKeyboardButton( text="8️⃣",callback_data="fanta8"),
	InlineKeyboardButton( text="9️⃣",callback_data="fanta9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortfanta"),
],     
])   









#Sprite uchun raqamlar 3
spriteuchun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="sprite1"),
    InlineKeyboardButton( text="2️⃣",callback_data="sprite2"),
    InlineKeyboardButton( text="3️⃣",callback_data="sprite3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="sprite4"),
    InlineKeyboardButton( text="5️⃣",callback_data="sprite5"),
	InlineKeyboardButton( text="6️⃣",callback_data="sprite6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="sprite7"),
    InlineKeyboardButton( text="8️⃣",callback_data="sprite8"),
	InlineKeyboardButton( text="9️⃣",callback_data="sprite9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortsprite"),
],     
])   






#cola uchun raqamlar 3
colaucun=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="cola1"),
    InlineKeyboardButton( text="2️⃣",callback_data="cola2"),
    InlineKeyboardButton( text="3️⃣",callback_data="cola3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="cola4"),
    InlineKeyboardButton( text="5️⃣",callback_data="cola5"),
	InlineKeyboardButton( text="6️⃣",callback_data="cola6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="cola7"),
    InlineKeyboardButton( text="8️⃣",callback_data="cola8"),
	InlineKeyboardButton( text="9️⃣",callback_data="cola9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortcola"),
],     
])   






#cola uchun raqamlar 3
nestle=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="nestle1"),
    InlineKeyboardButton( text="2️⃣",callback_data="nestle2"),
    InlineKeyboardButton( text="3️⃣",callback_data="nestle3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="nestle4"),
    InlineKeyboardButton( text="5️⃣",callback_data="nestle5"),
	InlineKeyboardButton( text="6️⃣",callback_data="nestle6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="nestle7"),
    InlineKeyboardButton( text="8️⃣",callback_data="nestle8"),
	InlineKeyboardButton( text="9️⃣",callback_data="nestle9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortnestle"),
],     
])   




#Fresh uchun raqamlar 1
freshcha=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="freshcha1"),
    InlineKeyboardButton( text="2️⃣",callback_data="freshcha2"),
    InlineKeyboardButton( text="3️⃣",callback_data="freshcha3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="freshcha4"),
    InlineKeyboardButton( text="5️⃣",callback_data="freshcha5"),
	InlineKeyboardButton( text="6️⃣",callback_data="freshcha6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="freshcha7"),
    InlineKeyboardButton( text="8️⃣",callback_data="freshcha8"),
	InlineKeyboardButton( text="9️⃣",callback_data="freshcha9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortfreshcha"),
],     
])   






#fersh  uchun raqamlar 2
fresholma=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="fresholma1"),
    InlineKeyboardButton( text="2️⃣",callback_data="fresholma2"),
    InlineKeyboardButton( text="3️⃣",callback_data="fresholma3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="fresholma4"),
    InlineKeyboardButton( text="5️⃣",callback_data="fresholma5"),
	InlineKeyboardButton( text="6️⃣",callback_data="fresholma6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="fresholma7"),
    InlineKeyboardButton( text="8️⃣",callback_data="fresholma8"),
	InlineKeyboardButton( text="9️⃣",callback_data="fresholma9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortfresholma"),
],     
])   





#Amerikano kofe  uchun raqamlar 1
amerika=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="amerika1"),
    InlineKeyboardButton( text="2️⃣",callback_data="amerika2"),
    InlineKeyboardButton( text="3️⃣",callback_data="amerika3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="amerika4"),
    InlineKeyboardButton( text="5️⃣",callback_data="amerika5"),
	InlineKeyboardButton( text="6️⃣",callback_data="amerika6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="amerika7"),
    InlineKeyboardButton( text="8️⃣",callback_data="amerika8"),
	InlineKeyboardButton( text="9️⃣",callback_data="amerika9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortamerika"),
],     
])   





#Coppuccino kofe  uchun raqamlar 2
cappuci=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="cappu1"),
    InlineKeyboardButton( text="2️⃣",callback_data="cappu2"),
    InlineKeyboardButton( text="3️⃣",callback_data="cappu3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="cappu4"),
    InlineKeyboardButton( text="5️⃣",callback_data="cappu5"),
	InlineKeyboardButton( text="6️⃣",callback_data="cappu6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="cappu7"),
    InlineKeyboardButton( text="8️⃣",callback_data="cappu8"),
	InlineKeyboardButton( text="9️⃣",callback_data="cappu9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortcappu"),
],     
])   



# kofe 3v1 uchun raqamlar 2
cofe=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="cofe1"),
    InlineKeyboardButton( text="2️⃣",callback_data="cofe2"),
    InlineKeyboardButton( text="3️⃣",callback_data="cofe3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="cofe4"),
    InlineKeyboardButton( text="5️⃣",callback_data="cofe5"),
	InlineKeyboardButton( text="6️⃣",callback_data="cofe6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="cofe7"),
    InlineKeyboardButton( text="8️⃣",callback_data="cofe8"),
	InlineKeyboardButton( text="9️⃣",callback_data="cofe9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortcofe"),
],     
])   



# latte uchun raqamlar 2
latte=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="latte1"),
    InlineKeyboardButton( text="2️⃣",callback_data="latte2"),
    InlineKeyboardButton( text="3️⃣",callback_data="latte3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="latte4"),
    InlineKeyboardButton( text="5️⃣",callback_data="latte5"),
	InlineKeyboardButton( text="6️⃣",callback_data="latte6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="latte7"),
    InlineKeyboardButton( text="8️⃣",callback_data="latte8"),
	InlineKeyboardButton( text="9️⃣",callback_data="latte9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlatte"),
],     
])   






   # qora choy uchun raqamlar 1
qora=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="qora1"),
    InlineKeyboardButton( text="2️⃣",callback_data="qora2"),
    InlineKeyboardButton( text="3️⃣",callback_data="qora3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="qora4"),
    InlineKeyboardButton( text="5️⃣",callback_data="qora5"),
	InlineKeyboardButton( text="6️⃣",callback_data="qora6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="qora7"),
    InlineKeyboardButton( text="8️⃣",callback_data="qora8"),
	InlineKeyboardButton( text="9️⃣",callback_data="qora9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortqora"),
],     
])   
 



 # qora choy uchun raqamlar 1
limon=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="limon1"),
    InlineKeyboardButton( text="2️⃣",callback_data="limon2"),
    InlineKeyboardButton( text="3️⃣",callback_data="limon3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="limon4"),
    InlineKeyboardButton( text="5️⃣",callback_data="limon5"),
	InlineKeyboardButton( text="6️⃣",callback_data="limon6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="limon7"),
    InlineKeyboardButton( text="8️⃣",callback_data="limon8"),
	InlineKeyboardButton( text="9️⃣",callback_data="limon9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortlimon"),
],     
])   
 


  # qora choy uchun raqamlar 1
kukchoy=InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton( text="1️⃣",callback_data="ko'k1"),
    InlineKeyboardButton( text="2️⃣",callback_data="ko'k2"),
    InlineKeyboardButton( text="3️⃣",callback_data="ko'k3"),

	], 
	[

	InlineKeyboardButton( text="4️⃣",callback_data="ko'k4"),
    InlineKeyboardButton( text="5️⃣",callback_data="ko'k5"),
	InlineKeyboardButton( text="6️⃣",callback_data="ko'k6"),


],   
 
	[

	InlineKeyboardButton( text="7️⃣",callback_data="ko'k7"),
    InlineKeyboardButton( text="8️⃣",callback_data="ko'k8"),
	InlineKeyboardButton( text="9️⃣",callback_data="ko'k9"),


], 
[

    InlineKeyboardButton( text="⬅️Ortga ",callback_data="ortko'k"),
],     
])   
 




ortbuyurtma



	#InlineKeyboardButton( text="Limon choy👍",callback_data="limon"),
    


