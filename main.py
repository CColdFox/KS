# -*- coding: <latin-1> -*-
# by CColdFox / waw
# https://github.com/CColdFox/KS
# big thanks to billythegoat356 for his Pystyle project, check him out: https://github.com/billythegoat356

from pystyle import Anime, Colors, Colorate, System, Center, Write
import pyautogui as auto
import time

banner = r"""
  ::  :  ::  ::  ::  :  ::  ::  :: ::  ::  ::  :: ::  ::  ::  :  ::  ::  ::  :  ::  ::  :: ::  ::  ::  :: ::  ::
::  §%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$::  
  #%%%%%%$                                                                                          %%%%%%%%%%::
: %%%%%%                                                                                             %%%%%%%%%  
 §%%%%%                                                                                               %%%%%%%% :
:§%%%%%                                                                                               %%%%%%%%  
 §%%%%%                                                                                               %%%%%%%% :
:§%%%%%                                                                                               %%%%%%%%  
:§%%%%%                        §§                                                                     %%%%%%%%  
 §%%%%%                        §/            **§  §*  *§  : §                                         %%%%%%%% :
:§%%%%%          :§§§          §/            /  § §  §//# $                                           %%%%%%%%  
 §%%%%%      §§§§§§§§§§§§§§§§§§§             /  § §  §  § $                                           %%%%%%%% :
:§%%%%%             §                                                                                 %%%%%%%%  
 §%%%%%                                                                                               %%%%%%%% :
:§%%%%%                                                                                               %%%%%%%%  
 §%%%%%                                                                                               %%%%%%%% :
:§%%%%%                                                                                               %%%%%%%%  
 §%%%%%&                                                                                             §%%%%%%%% :
:§%%%%%%/                                                                                           /%%%%%%%%%  
 /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%% :
::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$  
  :§%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ::
::  :: ::  ::  ::  :: ::  ::  ::  :  ::  ::  ::  :  ::  ::  :: ::  ::  ::  :: ::  ::  ::  :  ::  ::  ::  :  ::  """

ascii_art = r"""

 _   __             _____ _                 _       _   _             
| | / /            /  ___(_)               | |     | | (_)            
| |/ /  ___ _   _  \ `--. _ _ __ ___  _   _| | __ _| |_ _  ___  _ __  
|    \ / _ \ | | |  `--. \ | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \ 
| |\  \  __/ |_| | /\__/ / | | | | | | |_| | | (_| | |_| | (_) | | | |
\_| \_/\___|\__, | \____/|_|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|
             __/ |                                                    
            |___/"""[1:]              

def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("Key Simulation")
    Anime.Fade(text=Center.Center(banner), color=Colors.red_to_blue, mode=Colorate.Vertical, enter=True)

def main():
	global custom_msg
	System.Clear()
	print('\n'*2)
	print(Colorate.Diagonal(color=Colors.red_to_blue, text=Center.XCenter(ascii_art)))
	print('\n'*3)
	custom_msg = Write.Input(text="Enter the message that you want to send with this program > ", color=Colors.red_to_blue, interval=0.005)
	print()
	Write.Print(text="You have 5 seconds to go to a textbar in any software, the program will write your message automatically.", color=Colors.red_to_blue, interval=0.005)
	time.sleep(5)
	for char in (custom_msg):
		auto.press(char)
	time.sleep(0.00001)

if __name__ == '__main__':
    init()
    while True:
        main()