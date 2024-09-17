internet_choice_str = input('Welke internetverbinding wilt u gebruiken? 4G,5G,WIFI OPEN.')

internet_choice = internet_choice_str.upper()

if internet_choice == '4G':
    print(f"U heeft voor de internetverbinding {internet_choice} gekozen")

if internet_choice == '5G':
    print(f"U heeft voor de internetverbinding {internet_choice} gekozen")

if internet_choice == 'WIFI OPEN':
    print(f"U heeft voor de internetverbinding {internet_choice} gekozen.")
    answer_str = input('Weet u zeker dat u door wilt gaan met deze internetverbinding? [JA of NEE]')
    answer = answer_str.upper()
    if answer == 'JA':
        print(f"U heeft voor internetverbinding {internet_choice} gekozen")
    if answer == 'NEE':
        print(f"Het is niet gelukt om u met {internet_choice} te verbinden, probeer het nogmaals.")


