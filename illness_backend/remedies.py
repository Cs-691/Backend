

class Remedies():
    remedies = None
    
    def getRemedies(self, illness):
        print(illness)
        illness = illness.lower()
        if illness in self.remedies:
            return self.remedies[illness]
        else:
             return self.remedies['not found']
        
    def __init__(self):
        
        self.remedies = {};
        
        self.remedies['not found']=("we could not find home remedies. Please consult to nearest doctor!")
        
        
        self.remedies['fungal infection'] = (
            
           " Plain yoghurt with active cultures will reduce the growth of the fungi. Yoghurt is full of probiotics,"
           " which are bacteria that line your digestive tract and help your body's ability to absorb vital nutrients and combat infection. Most yoghurts are heated during the process which kill these beneficial organisms,"
            "so make sure you buy one that contains live Lactobacillus strains."
"Coconut oil helps kill species of yeast. The fatty acids act as fungicides that destroy the infection when you dab it onto the affected skin area."
"Apple cider vinegar is a well-known treatment for any kind of fungal infection. Drinking diluted apple cider vinegar may help kill off infections while preventing them from spreading, and increasing recovery time."
"Crushed garlic can also be used as a treatment for fungal infections."
"Aloe Vera contains six antiseptic agents that, according to research, exhibit antifungal, antibacterial, and antiviral activities. Apply the gel from an aloe vera plant onto the ringworm patch three or four times daily."
"If symptoms do not clear up within 2 weeks of using home remedies, then it may be necessary to see a doctor."
            
            )
        
        self.remedies['allergy'] = ("A 2012 review of 10 studies showed that saline nasal irrigation had beneficial effects for both children and adults with allergic rhinitis, which is often referred to as hay fever."
        "By removing moisture from the air, air conditioners and dehumidifiers can limit the growth of mildew and mold that can negatively impact allergie"
        "Although there's no scientific evidence to prove it, a popular theory suggests eating locally produced honey. According to the theory, you will lower your allergic reaction over time to the pollen that the bees collect in your area to make their honey"
        
     )
        self.remedies['gerd'] = (
            
            "A teaspoon of baking soda (a base substance) neutralizes stomach acid so that even if it comes up, you won't feel that burning sensation. "
            "Mix 1 teaspoon of baking soda with 8 ounces of water and drink all of it. Repeat as needed, but don't exceed seven doses in one day."
"People experiencing GERD can get some relief by chewing sugar free gum for 30 minutes after they eat as it stimulates the salivary glands,"
"which increases saliva. The saliva helps wash away acids."
"Bananas have natural antacid properties that counteract acid reflux. Eat a fully ripened banana each day to reduce the discomfort of acid coming back up. Another great fruit to try is an apple. "
"Avoid fruits with high acidic content such as oranges, grapefruit and pineapple."
"Don't lie down after eating as the contents of your stomach can easily be pushed back up."
"Ginger tea is great for many stomach ailments, from the common stomachache to nausea to chronic acid reflux."
"For full flavor, simmer slices of ginger root in water for 30 minutes."
            
     )
        
     
        self.remedies["peptic ulcer disease"] = (
"Cabbage is a popular natural ulcer remedy. Consumption of fresh cabbage juice appeared to help heal stomach ulcers more effectively than the conventional treatment used at the time."
"Probiotics are living organisms that help restore balance to the bacteria in the digestive tract. As well as helping achieve optimal gut health, they can help with treating ulcers.")

        self.remedies["diabetes"] = (
"Regular exercise can help you lose weight and increase insulin activity."
"It is also recommended to count your meal calories, control your carb intake, increase fiber intake, and stay hydrated."
"Getting enough sleep feels great and is necessary for good health. Poor sleeping habits and a lack of rest also affect blood sugar levels and insulin sensitivity.They can increase appetite and promote weight gain.")

        self.remedies["gastroenteritis"] = (
"Let your stomach settle. Don't eat solid foods for a while."
"Try sucking on ice chips or take small sips of water. Drink plenty of liquids taking small, frequent sips."
"Gradually begin eating bland and easy to digest food such as crackers, toast, rice, bananas. Stop eating if nausea returns."
"Avoid alcohol, nicotine, caffeine, dairy products."
"Avoid fatty and highly seasoned foods." 
"Get plenty of rest.")

        self.remedies["hypertension"] = (
            "Weight loss is one of the most effective lifestyle changes for controlling blood pressure." 
            "Losing even a small amount of weight if you're overweight or obese can help reduce your blood pressure."
"Regular physical activity such as 150 minutes a week, or about 30 minutes most days of the week can lower your blood pressure." 
"It is important to be consistent.Some examples of aerobic exercise you may try to lower blood pressure include walking, jogging, cycling, swimming or dancing."
" You can also try high-intensity interval training, which involves alternating short bursts of intense activity with subsequent recovery periods of lighter activity."
"Even a small reduction in the sodium in your diet can improve your heart health and reduce blood pressure by about 5 to 6 mm Hg if you have high blood pressure."
"Limit your alcohol intake."
"Each cigarette you smoke increases your blood pressure for many minutes after you finish." 
"Stopping smoking helps your blood pressure return to normal." 
"Quitting smoking can reduce your risk of heart disease and improve your overall health."
            
            )

        self.remedies["migraine"] = (
"Drink water or coffee."
"Rub peppermint oil on the part that hurts."
"Use hot or cold compress."
"Avoid bright lights or loud noises."
"Try to find a dark, quiet spot to speed up your recovery.")

        self.remedies["chicken pox"] = (
"Calamine lotion can help reduce itching."
"Use a clean finger or cotton swab to spread lotion on affected areas."
"Chicken pox can appear inside your mouth and can be extremely uncomfortable."
"Try sucking on some sugar free popsicle to soothe the mouth sores."
"Oatmeal baths can be soothing and itch-relieving for chickenpox."
" You may also apply oatmeal lotions to skin."
"This can have a soothing and moisturizing effect on itchy chickenpox blisters."
"Trim your fingernails and wear mittens to avoid scratching your skin."
"Chamomile has antiseptic and anti-inflammatory properties when applied to your skin."
"Brew two to three chamomile tea bags and allow to cool or place in a warm bath."
"Then, dip soft cotton pads or washcloths in the tea and apply to itching areas of skin."
"Always pat skin dry gently when done applying the compresses."
"Add one cup of baking soda to a shallow, lukewarm bath. Soak for 15 to 20 minutes.")

        self.remedies["common cold"] = (
"Staying warm and resting when you first come down with a cold or the flu helps your body direct its energy toward the immune battle."
"Gargling can moisten a sore throat and bring temporary relief."
"Gargle with half a teaspoon of salt dissolved in 8 oz warm water, four times daily."
"Hot liquids relieve nasal congestion, prevent dehydration, and soothe the uncomfortably inflamed membranes that line your nose and throat."
"If you're so congested that you can't sleep at night, try a hot toddy, an age-old remedy."
"Sleep with an extra pillow under your head.Elevating your head will help relieve congested nasal passages.")

        self.remedies["pneumonia"] = (
"Gargling with salt water or even just water can help get rid of some of the mucus in your throat and relieve irritation."
"Peppermint can also help alleviate irritation and expel mucus."
"That's because it's a proven decongestant, anti-inflammatory, and painkiller."
"You can also use a lukewarm compress to help cool your body from the outside in."
"Although it may be tempting to use a cold compress, the sudden temperature change can cause chills."
"A lukewarm compress provides a more gradual temperature change."
"If peppermint tea isn't your thing, a glass of warm water will do."
"This can help you stay hydrated and warm you internally. Make extra effort to get in fluids."
"Have a bowl of hot soup, it can also help to replenish vital liquids while it warms from the inside out.") 
        
        self.remedies["dimorphic hemmorhoids(piles)"] = (
            "we recommend people with painful hemorrhoids sit in warm water for 15 minutes, several times a day especially after a bowel movement."
"Witch hazel is reputed to reduce pain, itching and bleeding until hemorrhoids fade out. There isn't much scientific support for"
"its use but it does contain tannins and oils that may help bring down inflammation and slow bleeding."
"The anti-inflammatory properties of aloe vera may help soothe inflammation of hemorrhoids. Only use pure aloe."
"Use these simple ingredients to make a compound that you can apply directly to the inflamed area: Mix 2 tablespoons of "
"Epsom salts with 2 tablespoons of glycerin. Apply the mixture to a gauze pad and place it on the painful area."
 "Leave this application on the area for 15-20 minutes. Repeat every 4-6 hours until the pain eases."
"To help treat and prevent hemorrhoids it's important to eat enough fiber (25 grams a day for women, "
"38 grams a day for men) and to drink at least eight glasses of water a day."
            )
        
        self.remedies["hypoglycemia"] = (
"Try putting petroleum jelly or a heavy moisturizer. It locks water in your skin and helps it to heal and reduce redness."
"Put some apple cider vinegar on your head a few times a week- either full strength or mixed with water."
" Rinse it off after it has dried. Don't try this when your skin is cracked or bleeding."
"Spend some time in the great outdoors.The sun's ultraviolet B rays can help fight your psoriasis."
"Put Dead Sea or Epsom salts into a tub with warm water. Soak for about 15 minutes, and use a moisturizer when you're done to seal in the water."
"Put some ground-up oats in your bath, sit back, and relax. Just make sure the water is warm, not hot, so you don't irritate your skin."
"Eat or drink 15g of fast acting carbohydrates - 3-4 glucose tablets, 4-6 pieces of candy, half cup of fruit juice, half cup of soft drink, or a tablespoon of honey."
" You can also have, if available, jelly beans, skittles, gummy bears, grapes, raisins.")

        self.remedies["(vertigo) paroymsal  positional vertigo"] = (
"Perform the following maneuver Start by sitting upright on a flat surface, with a pillow behind you and with your legs outstretched."
" Turn your head 45 degrees to the right."
" With your head still titled, quickly recline with your head on the pillow. Stay in this position for at least 30 seconds."
" Slowly turn your head to the left, a full 90 degrees, without lifting your neck."
" Engage your whole body, turning it to the left so that you are completely on your left side."
" Slowly return to your original position, looking forward and sitting straight up."
"Feelings of vertigo can be triggered by sleep deprivation."
"If you're experiencing vertigo for the first time, it might be a result of stress or lack of sleep."
"If you can stop what you're doing and take a short nap, you may find that your feelings of vertigo have resolved themselves."
"Sometimes vertigo is caused by simple dehydration. Reducing your sodium intake may help."
" But the best way to stay hydrated is to simply drink plenty of water. Monitor your water intake and try to account for hot, humid conditions and sweaty situations that might make you lose extra fluids.")

        self.remedies["acne"] = (

"Honey is an amazing antimicrobial and wound-healing remedy. To use as an acne home remedy,"
 "dip a cotton swab in the honey and then apply it to the affected area. Leave it for at least 30 minutes before rinsing."
"Lemon contains Vitamin C and has acidic properties to fight off acne-fighting bacteria. It is best to use natural fresh lemon juice. Dip a clean cotton swab in lemon juice."
" Apply it to the affected area and let it stay overnight. Wash it with a lukewarm water the following morning."
"Another alternative is to make a mask of lemon juice and cinnamon powder and apply overnight."
)
        
        self.remedies["urinary tract infection"] = (
"Stay hydrated. Drinking enough water is one of the easiest ways to help prevent and treat UTIs. "
"Water helps the urinary tract organs remove waste from the body efficiently while retaining vital nutrients and electrolytes. "
"Being hydrated also dilutes the urine and speeds its journey through the system, making it harder for bacteria to reach the cells "
"that line urinary organs and to cause an infection."
"Urinate as soon as possible when the urge arises to help treat and prevent UTIs."
"Frequent urination puts pressure on the bacteria in the urinary tract, which can help to clear them out."
"Cranberry juice is one of the most well-established natural treatments for UTIs"
)
        
        self.remedies["psoriasis"] = (
"Try putting petroleum jelly or a heavy moisturizer. It locks water in your skin and helps it to heal and reduce redness."
"Put some apple cider vinegar on your head a few times a week- either full strength or mixed with water. Rinse it off after it has dried."
"Don't try this when your skin is cracked or bleeding."
"Spend some time in the great outdoors. The sun's ultraviolet B rays can help fight your psoriasis."
"Put Dead Sea or Epsom salts into a tub with warm water. Soak for about 15 minutes, and use a moisturizer when you're done to seal in the water."
"Put some ground-up oats in your bath, sit back, and relax. Just make sure the water is warm, not hot, so you don't irritate your skin."
)
        
        self.remedies["impetigo"] = (
        "Use aloe vera directly on the skin. It can also encounter the dryness and itching caused by impetigo "
"Make chamomile tea and use it as a skin wash. Or apply a used, cooled chamomile tea bag directly on sores."
"Place the cut side of a slice of garlic directly on impetigo sores. This may sting a little. You can also press garlic cloves, "
"and then apply topically. Garlic is also great to incorporate into your diet."
"Place a slice of ginger, cut side down, on impetigo sores. It might sting a little. You can also juice ginger root "
"and make a poultice from the juice, applying it topically. Incorporating ginger into your diet is another option."
 )       
        self.remedies["fracture"] = (
"Stop the bleeding by applying pressure."
"Apply ice packs to reduce the swelling and relieve some pain."
"Stop smoking for a while. Bones of patients who smoke take much longer to heal."
"Eat a balanced diet and ensure adequate nutritional intake to let your body recover and heal."
)
        self.remedies["vitamin deficiency"] = (
"Eat foods rich in vitamins."
"Fatty food like tuna, salmon, mackerel, and fish oils are excellent sources of vitamin D."
"Soak in the sun daily if you suffer from vitamin D deficiency."
)

        self.remedies["pregnancy"] = (
"Take a pregnancy test or visit the OBGYN.") 

        self.remedies["stress"] = (
"The smell of lavender is said to instantly relieve stress."
"Mix some drops of lavender oil in your bath or use it in a diffuser for some stress relief."
"30 minutes of exercise everyday can help reduce stress."
"Drink some soothing tea like chamomile tea."
"Herbs like Valerian, lemon balm, kava are extremely helpful."
"Try meditating or relaxation exercises.")

        self.remedies["dehydration"] = (
"Drink water in small sips throughout the day.Also try drinking ORS or electrolyte replenishing drinks."
"Suck on popsicles or ice chips."
"Try to keep body as cool as possible - air conditioned rooms, less layers, breathable fabrics, spray bottles filled with water to spray on skin."
"Increase liquid intake on daily basis with soups, fresh fruit juices, coconut water, electrolyte water, lemon water."
)
        self.remedies["flu"] = (
"Gargle with salt water. It helps relieve a sore, scratchy throat by pulling all the viral fluids out of your throat."
"Chicken soup or bone broth can be super effective."
"Bone broth contains immune supporting vitamins and minerals that can help you recover quicker plus it's easier on the stomach to digest."
"Stay hydrated."
"Sleep! Give the body the rest it needs."
"Breathe in some steam to relieve your stuffy nose.")

        self.remedies["food poisoning"] = (
"Replace all necessary lost minerals, like sodium, potassium, calcium using some ORS or electrolyte water."
"Don't eat for a couple of hours. Gradually begin to eat with bland, easy-to-digest food like crackers, toast, rice."
"Suck on ice chips or drink small sips of water."
"Rest till you feel considerably better."
)
   
        self.remedies["alcohol poisoning"] = (
"This is an emergency situation.Visit the doctor immediately."
"Sleeping it off can put you into unconsciousness. Don't try any home remedies.")

