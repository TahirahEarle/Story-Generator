''' 
Created By: Tahirah Earle
Date: September 28, 2022
Purpose: This code generates a story based on the words inputted by the user. 
This code uses the fstrings and madlib functions
'''
print('─' * 37, 'Story Generator', '─' * 37)
print('─' * 91) 

noun=input("Noun: ")
noun3=input("Noun: ")
verb=input("Verb: ")
verb1=input("Verb: ")
item=input("Item: ")
adj=input("Adjective: ")
adj1=input("Adjective: ")
adj2=input("Adjective: ")
colour=input("Colour: ")
verb2=input("Verb: ")
season=input("Season: ")
adj3=input("Adjective: ")
adj4=input("Adjective: ")
verb3=input("Verb: ")
bodyaction=input("A bodily action: ")
fictionalcharacter=input("A fictional character: ")

storygenerator= f"Confusion and chaos lifted. All was still and clear in {noun} mind. Only hours earlier he was filled \
with misery, {adj1}, and desperation. But now the {fictionalcharacter} curse had taken control, freed from its \
chains and eager to make up for lost time. {verb} claws easily removed the {item} from his body. He would have \
no more use for them. He had emerged beside a small, {adj3} river which was painted {adj} under the clear sky. \
It was {adj2}, the dead of {season}, and his breath misted before his eyes. The weather did not bother him. This \
body was made for endurance. His long, wiry limbs held easy strength. He felt a {verb2} run through his whole body.\
An electrically charged energy that needed to be {verb1}. His magnified senses announced the presence of all living \
{noun3} within {bodyaction} distance. None could defy him; none could oppose him. All would {verb3} before him. \
But it would make no difference. This night would be coloured in {colour}. He threw back his head and let out a \
howl of hysteria, {adj4}, and fervour. The night belonged to {noun}. The full moon was up, and the chase was on."
print('─' * 91)

print(storygenerator)
