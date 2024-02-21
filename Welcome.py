import pygame as py
import time as t

# initialize  pygame
py.init()

# setup with display
screen_width: int = 800
screen_hight = 600
screen = py.display.set_mode((screen_width, screen_hight))
py.display.set_caption("BMS")
font = py.font.SysFont(None,55)  # Choose any font and size you like

# set up font  text
text = "Welcome to Bank Management System "
text_color = (255, 255, 255)  # White color
# display display
text_surface = font.render(text, True, text_color)
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_hight // 2))
screen.blit(text_surface, text_rect)
im=py.image.load('C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\wellcome img.jpg')
size=im.get_rect().size
screen.blit(im,(205,30))
# Update the display
py.display.flip()

# Wait for a few seconds
t.sleep(3)

# Quit Pygame
py.base.quit()


def Main_menu():
     print('1.Create New Account'
       '\n2.Deposit Amount'
       '\n3.Withdraw Amount'
       '\n4.Statement Check'
       '\n5.Update Bank Account'
       '\n6.Closeing Bank Account'
       "\n7.Online Bank "
        "\n8.Loan Apply"
       '\n9.Exit')
     ch=int(input('Enter your choice:'))
     i=1
     while(i<=3):
         if ch == 1:
             import Createnewacc
         elif ch == 2:
             import Depositamount
         elif ch == 3:
             import WithdrawAmount
         elif ch == 4:
             import StatementCheck
         elif ch == 5:
             import Updatebankacc
         elif ch == 6:
             import Closeingbankacc
         elif ch == 7:
             import OnlineBank
         elif ch ==8:
             import LoanApply
         elif ch == 9:
             import Exit
             break
         else:
             print('Please enter the correct choice')
         i+=1
Main_menu()

