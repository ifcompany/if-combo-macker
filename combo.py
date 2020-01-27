from os import system
system('clear')
baner = '''
\033[0;93m	@@@   \033[0;94m|           |\033[0;93m User:@@@   \033[0;94m|
\033[0;93m	@@@@@ \033[0;94m|\033[0;91m = User =\033[0;92m> \033[0;94m|\033[0;93m User:@@@@  \033[0;94m|
\033[0;93m	@@@@  \033[0;94m|           |\033[0;93m User:@@@@@ \033[0;94m|


      \033[0;95m && \033[0;92mif Combo macker \033[0;95m &&
 \033[0;95m      && \033[4;34mT\033[0;93m.\033[4;34mme/Thelinkif\033[0;95m   &&
  \033[0;95m     && \033[4;34mwww\033[0;93m.\033[4;34mifcompany\033[0;93m.\033[4;34mir\033[0;95m &&
   \033[0;95m    && \033[4;33mProgrammer\033[0;36m : \033[0;101m007\033[0;95m && \033[0;33mV 1.5.0\033[0m
'''
print(baner)

username = input('\033[0;32m$ \033[0;36mEnter The Username list \033[0;34m\> \033[0;37m')
user = open(username, "r").read().splitlines()

pa33 = input('\033[0;32m$ \033[0;36mEnter The Password list \033[0;34m\> \033[0;37m')
passlist = open(pa33, "r").read().splitlines()

goodlist = input('\033[0;32m$ \033[0;36mEnter The GooDlist name \033[0;34m\> \033[0;37m')

f = open(goodlist, "a")
for er in user:
    for p in passlist:
        print('\033[0;34m'+er+"\033[0;32m:\033[0;35m"+p)
        f.write(er+":"+p+'\n')
print('\033[0;31mThe End\033[0m')
f.close()
