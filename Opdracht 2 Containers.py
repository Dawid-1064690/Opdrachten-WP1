#Binnen 441 minuten zijn er 331 containers gelost
geloste_containers = 331
print(geloste_containers)
lostijd = 441

gemiddelde_lostijd = lostijd / geloste_containers
print(gemiddelde_lostijd)

#Binnen 295 minuten zijn er 287 containers geladen
geladen_containers = 287
print(geladen_containers)
laadtijd = 295

gemiddelde_laadtijd = laadtijd / geladen_containers
print(gemiddelde_laadtijd)

print(f'De gemiddelde tijd voor het lossen van {geloste_containers} containers bedraagt {lostijd} minuten')
print(f'De gemiddelde tijd voor het laden van {geladen_containers} containers bedraagt {laadtijd} minuten')