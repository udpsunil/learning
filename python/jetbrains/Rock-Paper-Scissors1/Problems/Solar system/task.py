# create the planets.txt
planets = ["Mercury\n",
           "Venus\n",
           "Earth\n",
           "Mars\n",
           "Jupiter\n",
           "Saturn\n",
           "Uranus\n",
           "Neptune\n"]
with open('planets.txt', 'w', encoding='utf-8') as planet_file:
    planet_file.writelines(planets)
