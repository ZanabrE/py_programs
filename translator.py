def english_to_french(english_to_french):#Naming my function as english_to_french
    #Inside my function I can command to do anything in here.
    text1 = input('Enter Hello that will be transleted into French: ')
    english = 'hello'
    if text1 == english:
        print('Hello translated to French is Bonjour.')
    else:
        print('Incorrect!')
    print('--------------------------------------------')
    text2 = input('Enter Bonjour to be translated in English: ')
    french = 'bonjour'
    if text2 == french:
        print('Bonjour translated to English is Hello')
    else:
        print("Incorrect!")
english_to_french(english_to_french='')#This will return the function.


def english_to_german(englishTxt2):#Naming my function as english_to_german
    #Inside my function I can command to do anything in here.
    print('Enter Hello to be translated in German: ')
    englishTxt2 = input('')
    print(englishTxt2 + ' in German is Hallo.')
    print('--------------------------------------------')
    print('Enter Hallo to be translated in English: ')
    germanTxt = input('')
    print(germanTxt + ' transleted to English is Hello.')
english_to_german(englishTxt2='')#This will return the function.

