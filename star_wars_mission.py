import random

characters = [
    "A Jedi Knight",
    "A Padawan",
    "A Rebel Pilot",
    "A Mandalorian",
    "A Smuggler",
    "A Clone Trooper",
    "A Resistance Spy",
    # New Characters
    "Yoda",
    "Luke Skywalker",
    "Din Djarin"

]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar",
    # New Planets
    "Starkiller Base"
]

missions = [
    "Rescue a captured droid",
    "Recover stolen battle plans",
    "Escape an Imperial base",
    "Protect a hidden Jedi temple",
    "Deliver a secret message",
    "Destroy a Sith weapon",
    "Find a lost lightsaber",
    # New Missions 
    "Rrescue Grogue (Baby Yoda)"
]

enemies = [
    "Darth Vader",
    "A Sith Inquisitor",
    "Stormtroopers",
    "Bounty Hunters",
    "A Crime Lord",
    "Battle droids",
    "The First Order",
    # New Enamies
    "Kylo Ren",
    "Darth Maul",
    "Count Dooku"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "A Group of Ewoks",
    "A Mysterious Rebel Informant"
    # New Allies
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter",
    # New Ships
    "Death Star",
    "Imperial Star Destroyer"
]

weapons = [
    "a red lightsaber",
    "a green lightsaber"
    "Luke's lightsaber",
    "a blaster",
    "the Darksaber",
    "a Beskar spear",
    "nothing but the knowledge of the force",
    "a flamethrower"
]


def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)
    weapon = random.choice(weapons)

    print("\n==============================")
    print("  STAR WARS MISSION BRIEFING  ")
    print("==============================")
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Difficulty:", difficulty)

    print("\nBriefing:")
    print(f"{character} must travel to {planet} aboard the {ship}.")
    print(f"With help from {ally}, and carrying {weapon},")
    print(f"they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    print("May the Force be with you.")

def main():
    print("Welcome to the Star Wars Mission Generator!")

    while True:
        choice = input("\nGenerate a new mission? yes/no: ").title()

        if choice == "Yes":
            generate_mission()
        elif choice == "No":
            print("Goodbye, young Jedi.")
            break
        else:
            print("Please type yes or no.")
main()