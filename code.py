
amount = int(input("input the amount of fantasy NPC's to create:"))
counter = 1

import random

# Specifics of the generated npc in question, and store the data 

Name = ["Velvetta", "Charllete", "Madoka", "Temptriss", "Bebe", "Hydra", "Momo", "Unit", "Lollipop", "quandale", "Octavia", "Law", "boo", "hawk", "Eep", "Zircon", "Flowetta", "Agustus", "Chroma", "Gigi", "Lilywrite", "eternia", "blade", "Sayaka", "Junko", "Ophilia", "Unnamed"]
status = ["The witch of revenge", "The Ghoul", "The eldrich being beyond human comprehension", "The lost princess", "The nutcracker witch", "The labrynth monster", "The concept", "The demigod", "The archangle", "The lost spirit", "The witch of salvation", "The darkest shadow", "The chain witch", "The wanderer", "The thing?", "The magician", "The overseer", "The queen", "The corrupted soul", "The ultimate being", "The dammed", "The hated", "The *****", "The savior", "The witch of guilt", "The witch of the stars", "The doll witch", "the magical girl"]
age = random.randint(1,999)
power_level = random.randint(1,1020)
health = random.randint(1,100)
hostility = random.randint(1, 100)
print("\n")

# Make the amount of NPCs requested
while counter <= amount:
    print(random.choice(Name), random.choice(status), f" - Age: {age} yrs. \n    power_level: {power_level} \n   health: {health} \n   hostility: {hostility} \n")
    age = random.randint(1, 999)
    power_level = random.randint(1, 1020)
    health = random.randint(1,100)
    hostility = random.randint(1, 100)
    counter += 1
    
#Describe what everything does

print("\n \n What everything does: \n Status: status is basicly what species or what ranking the NPC is, there are many fictional titles but those are to not be left explained, just use your imagination!!! \n Age: Age is quite literally just the Npc's age. The age range is VERY extensive and wide due to most of the species not being human \n Power level: power level is how strong the NPC is, if one NPC's power level is stronger than another then they are more likely to defeat the other (obviosly) \n Health: self explanitory how much health something has, or how hard it is to kill or defeat this NPC \n hostility: basicly how good or bad the NPC is, the more hostility the more evil the NPC's intentions should be, the opposite goes for less hostility \n that's all andTHE END thank you for using this npc generator")

