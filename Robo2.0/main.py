#for MAC OS
# import os
#
# if __name__ == '__main__':
#     print('Welcome to Robo speaker 2.0 sponsored by Unknown-X')
#     x= input('Lets start the chat by typing something : ')
#     while x != 'exit':
#         command = f"say {x}"
#         os.system(command)
#         x = input('Type something (or "exit" to quit): ')
# os.system("say 'Bye bye buddy See ya'")


# for windows
import os

if __name__ == '__main__':
    print('Welcome to Robo speaker 2.0 Sponsored by Unknown-X')
    x = input('Lets start the chat by typing something : ')
    while x != 'exit':
            command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
            os.system(command)
            x = input('Type something (or "exit" to quit): ')
    os.system('powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye bye buddy See ya\')"')



# optimized approach for both windows and macOS
# import os
# import platform
#
# if __name__ == '__main__':
#     print('Welcome to Robo speaker 2.0 ... sponsored by Unknown-X')
#     x = input('Lets start the chat by typing something : ')
#     while x != 'exit':
#         if platform.system() == 'Windows':
#             command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
#         else:
#             command = f"say {x}"
#         os.system(command)
#         x = input('Type something (or "exit" to quit): ')
#     if platform.system() == 'Windows':
#         os.system('powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye bye buddy See ya\')"')
#     else:
#         os.system("say 'Bye bye buddy See ya'")