# Import de terminal colorido
from colorama.ansi import Fore
# Importando palavras
from palavras import palavras
# Importando seletor aleatório
from random import randrange
# Importando contador de coleções
from collections import Counter
# Importando operações de expressões regulares
import re

palavra_dica = palavras[randrange(0, len(palavras))]
palavra_escolhida = palavra_dica[0]
dica = palavra_dica[1]
letras_chutadas = []
letras_acertadas = []
preview = []
tentativas = len(palavra_escolhida)
# Função que conta a quantidade de vezes que uma letra repete
count = Counter(palavra_escolhida)

# Preenchendo o preview de espaços placeholder para substituir mais tarde
for x in range(len(palavra_escolhida)):
    preview.append('*')


# Função que verifica se acertou
def verifica(chute):
    if chute in palavra_escolhida:
        print(f'{Fore.GREEN}Acertou!{Fore.WHITE}')

        for x in range(count[chute]):
            letras_acertadas.append(chute)

        for match in re.finditer(chute, palavra_escolhida):
            s = match.start()
            preview[s] = chute

        print(preview)

    else:
        print(f'{Fore.RED}Errou{Fore.WHITE}')

    letras_chutadas.append(chute)


# Classe com as ascii art do projeto
class ascii_art():
    def trofeu():
        print(f''' {Fore.YELLOW}
               ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                           \|               :::::/|/
                            |               ::::::|
                            | Jogador de forca::::|
                            |         Nº1    :::::|
                            |               ::::::|
                            |              .::::::|
                            J              :::::::F
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
        ____________________________|  """|"_________________________________________
                                    |  :::|
                                    F   ::J
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `"""---------"""'

                                    Parabéns!!!
        ''')

    def enforcado():
        print(f'''{Fore.RED}

                            .ed"""" """$$$$be.
                           -"           ^""**$$$e.
                         ."                   '$$$c
                        /                      "4$$b
                       d  3                      $$$$
                       $  *                   .$$$$$$
                      .$  ^c           $$$$$e$$$$$$$$.
                      d$L  4.         4$$$$$$$$$$$$$$b
                      $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
          e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
         z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
        4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
        ^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
          "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
                "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
                  ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
                     "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
                           "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                          "$   "%*ebJLzb$e$$$$$b $P"
                            %..      4$$$$$$$$$$ "
                             $$$e   z$$$$$$$$$$%
                              "*$c  "$$$$$$$P"
                               ."""*$$$$$$$$bc
                            .-"    .$***$$$"""*e.
                         .-"    .e$"     "*$c  ^*b.
                  .=*""""    .e$*"          "*bc  "*$e..
                .$"        .z*"               ^*$e.   "*****e.
                $$ee$c   .d"                     "*$.        3.
                ^*$E")$..$"                         *   .ee==d%
                   $.d$$$*                           *  J$$$e*
                    """""                              "$$$"

        ''')

    def titulo():
        print(f'''{Fore.GREEN}
        
           ___                         _        ______                  
          |_  |                       | |       |  ___|                 
            | | ___   __ _  ___     __| | __ _  | |_ ___  _ __ ___ __ _ 
            | |/ _ \ / _` |/ _ \   / _` |/ _` | |  _/ _ \| '__/ __/ _` |
        /\__/ / (_) | (_| | (_) | | (_| | (_| | | || (_) | | | (_| (_| |
        \____/ \___/ \__, |\___/   \__,_|\__,_| \_| \___/|_|  \___\__,_|
                      __/ |                                             
                     |___/                                              
        {Fore.WHITE}
        ''')


# Menu principal

# Iniciando arte do título
ascii_art.titulo()
print(f'{Fore.CYAN}Github e Behance: /manzolimatheus')
print(f'* Matheus Manzoli & Raíne Felix - 3ºDS *{Fore.WHITE}')

# Mostrando quantidade de caracteres da palavra secreta
print(f'Palavra secreta: {preview}')
print(f'{Fore.GREEN}Dica: {Fore.WHITE}{dica}')

# Jogo
while tentativas > 0:
    if len(letras_acertadas) == len(palavra_escolhida):
        print(f'A palavra era {palavra_escolhida}! Parabéns!')
        print(f'{Fore.GREEN}Você ganhou o jogo!')
        ascii_art.trofeu()
        break
    else:
        chute = input(f'Diga uma letra: {Fore.CYAN}').upper()[:1]

        if chute in letras_chutadas:
            print(
                f'{Fore.WHITE}Você já chutou {Fore.MAGENTA}{chute}{Fore.WHITE}! Tente novamente.')
        else:
            verifica(chute)
            tentativas -= 1

        print(f'Tentativas restantes:{Fore.GREEN} {tentativas} {Fore.WHITE}')
else:
    if len(letras_acertadas) == len(palavra_escolhida):
        print(f'A palavra era {palavra_escolhida}! Parabéns!')
        print(f'{Fore.GREEN}Você ganhou o jogo!')
        ascii_art.trofeu()
    else:
        print(f'A palavra era {palavra_escolhida}!...')
        print(f'{Fore.RED}Enforcado! Você perdeu.')
        ascii_art.enforcado()
