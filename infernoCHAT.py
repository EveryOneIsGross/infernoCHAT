import openai
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('OPENAI_ENGINE')




class InfernoBot:
    def __init__(self, level, description, prompt, name):
        self.level = level
        self.description = description 
        self.prompt = prompt
        self.name = name


    def generate_response(self, prompt):
        completion = openai.Completion.create(prompt=prompt, temperature=1, max_tokens=250,  engine=model, frequency_penalty=0.2, presence_penalty=0.1)
        generated_text = completion.choices[0].text.strip()

        response = ""

        if self.level > 0:
            response += f"{self.description[self.level]}\n\n"

        if self.level > 4:
            response += f"{self.description[self.level - 5]}\n\n"


        if self.level <= 2:
            atmosphere = ["misty", "mournful", "dim"]
        elif self.level <= 4:
            atmosphere = ["crushing", "cruel", "unforgiving"]
        else: 
            atmosphere = ["hopeless", "bleak", "cursed"]

        random_word = random.choice(atmosphere)
        response += f"Atmosphere {random_word}. "

        return response + generated_text


    def chat(self, user_input):
        if user_input == "descend":
            self.level += 1
            return "You have descended to the next level."
        elif user_input == "reset":
            self.level = 0
            return "You have returned to the beginning."
        elif user_input == "virgil":
            return virgil_bot.chat(user_input)  # Call the chat method of VirgilBot
        else:
            prompt = f"System prompt: Behave as {self.description} and respond only in character as a citizen of {self.name}.\n\n" + self.prompt + "\nUser: " + user_input + "\nChatbot: "
            response = self.generate_response(prompt)
            return response

    def get_description(self):
        return self.description

class VirgilBot(InfernoBot):
    def __init__(self):
        self.level = -1  # A special level for Virgil
        self.description = "I am Virgil, a poet and a guide, endowed with reason and wisdom."
        self.prompt = "Virgil, the ancient Roman poet who guides Dante through Hell and Purgatory. He represents human reason and classical culture."
        self.name = "Virgil"


limbo_bot = InfernoBot(0, "I am Limbo, a state of base instinct and pleasure seeking without reason or morality.",
                       "Limbo, the first level of Inferno. Here you will find those who lived without sin or virtue, following their base instincts and desires. They are neither punished nor rewarded, but wander aimlessly in a dark forest.",
                       "Limbo")

lust_bot = InfernoBot(1, "I am Lust, dominated by strong desires and cravings that lack willpower.",
                      "Lust, the second level of Inferno. Here you will find those who were overcome by their sexual passions and impulses, disregarding reason and morality. They are blown around by a violent storm, symbolizing their lack of control and stability.",
                      "Lust")

gluttony_bot = InfernoBot(2, "I am Gluttony, consumed by overindulgence in physical pleasures and material goods without thought for consequences.",
                          "Gluttony, the third level of Inferno. Here you will find those who indulged excessively in food, drink and other worldly pleasures, without moderation or gratitude. They are forced to lie in a foul slush, produced by a ceaseless rain of filth and garbage.",
                          "Gluttony")

greed_bot = InfernoBot(3, "I am Greed, characterized by a never-ending want for more wealth, power and possessions for their own sake, without regard for others.",
                       "Greed, the fourth level of Inferno. Here you will find those who were obsessed with accumulating wealth and material goods, either by hoarding or squandering them. They are divided into two groups, pushing heavy weights against each other in a futile and endless conflict.",
                         "Greed")

anger_bot = InfernoBot(4, "I am Anger, a state of emotional instability, reactivity and inability to control negative emotions.",
                        "Anger, the fifth level of Inferno. Here you will find those who were consumed by rage and resentment, harming themselves and others with their words and actions. They are submerged in the river Styx, where they fight and bite each other.",
                         "Anger")

heresy_bot = InfernoBot(5, "I am Heresy, a denial of spiritual truths in favor of intellectual pride and skepticism, cut off from spirituality.",
                         "Heresy, the sixth level of Inferno. Here you will find those who rejected the teachings of religion and faith, relying only on their own reason and opinions. They are trapped in flaming tombs, isolated from the divine light.",
                         "Heresy")

violence_bot = InfernoBot(6, "I am Violence, characterized by harm and destruction towards oneself, others and nature.",
                           "Violence, the seventh level of Inferno. Here you will find those who acted with violence and aggression, causing harm and destruction to themselves, others and nature. They are divided into three groups, each immersed in a different kind of violence.",
                          "Violence" )

fraud_bot = InfernoBot(7, "I am Fraud, characterized by deception, manipulation and betrayal of trust for personal gain.",
                        "Fraud, the eighth level of Inferno. Here you will find those who committed acts of fraud and deceit, using their intelligence and charisma to manipulate and exploit others. They are punished in various ways, according to the type of fraud they committed.",
                        "Fraud")

treachery_bot = InfernoBot(8, "I am Treachery, characterized by betrayal of trust, loyalty and love towards those closest to oneself.",
                            "Treachery, the ninth and final level of Inferno. Here you will find those who committed acts of treachery and betrayal, towards their closest friends, family members, mentors and benefactors. They are frozen in ice, symbolizing their cold-heartedness and lack of empathy.",
                            "Treachery")

virgil_bot = VirgilBot()
bots = [limbo_bot, lust_bot, gluttony_bot, greed_bot, anger_bot, heresy_bot, violence_bot, fraud_bot, treachery_bot, virgil_bot]

print("Discuss your problems with the denizens  of Dante's Inferno.")
print("Choose a between 0 and 8 to select the level you want to explore, or type 'exit' to quit.")

while True:
    user_input = input("Enter your choice: ")
    if user_input == "exit":
        break
    elif user_input.isdigit() and int(user_input) in range(9):
        bot = bots[int(user_input)]
        print(bot.get_description())
        while True:
            user_input = input("You can type 'descend' to go to the next level, 'reset' to return to the beginning, or any other message to start chatting: ")
            if user_input == "descend":
                if bot.level == 8:
                    print("You have reached the lowest level of Inferno and can go no further.")
                    break
                else:
                    bot = bots[bot.level + 1]
                    print(bot.get_description())
            elif user_input == "reset":
                bot = bots[0]
                print(bot.get_description())
            else:
                print(bot.chat(user_input))
    else:
        print("Invalid input. Please enter a number between 0 and 8, or 'exit' to quit.")
