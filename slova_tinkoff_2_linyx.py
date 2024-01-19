#!/home/sergey/kivy_venv/bin/python3

import pandas as pd

import numpy
import kivy
#from statistics import mean
import pandas as pd
import numpy as np
import random


#!/usr/bin/python

#import sys
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.resources import resource_find
from kivy.core.window import Window



#if using phone: android == 1

android = 1


class ButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        global color_but, color_tabl, buttons, vvod_slov, massiv_slov_our, slovo_na_ekrane, direc,android
        super(ButtonGrid, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 6  # Добавляем дополнительную строку для красной полосы
        self.background_color = (1, 1, 1, 1)  # белый цвет фона

        buttons = {}  # Используем словарь для хранения кнопок

        rand = min(len(massiv_slov_our), 9)
        rand = random.randint(0,rand)
        slovo_na_ekrane = massiv_slov_our[rand]

        for i1 in range(5):
            for i2 in range(5):
                color_0 = color_but[color_tabl[i1][i2]]

                if i1 == 0:
                    
                    text_but = (slovo_na_ekrane)[i2]
                else:
                    text_but ="" 



                buttons[(i1, i2)] = ColorChangingButton(  # Button( 
                    button_number=i1 * 5 + i2, text=text_but, background_normal='',
                    background_color=color_0, color=(0, 0, 0, 1))  # желтый цвет кнопок command = lambda i31_0= i31, i39_0 = i39: ofile_2(i31_0,i39_0)

                #button.bind(on_release=self.change_color)  # lambda i1_0 = i1, i2_0 = i2: pull_but(i1_0,i2_0)

                #buttons[(i1, i2)] = button
                self.add_widget(buttons[(i1, i2)])

        label_belii = Label()  # Создаем виджет Label для красной полосы
        with label_belii.canvas.before:
            Color("#D6D6D6")  # устанавливаем красный цвет
            self.label_belii_rect = Rectangle(pos=label_belii.pos, size=label_belii.size)  # создаем прямоугольник

        self.add_widget(label_belii)



        if android == 0:
            belii_width = self.width
            window_width = 30
            but_size = [80, 50]
            belii_height = label_belii.height/2
        else:
            belii_width = Window.size[0]/3
            window_width = Window.size[0]/15
            but_size = [Window.size[0]/5,Window.size[0]/9]
            belii_height = label_belii.height
            
        # Получение размера открытого окна
        #window_width = Window.size[0]
        

        button_image = Image(source=direc+'/info.jpg', size=(window_width, window_width))
        icon_button = Button(background_normal='', size_hint=(None, None), size=(window_width, window_width))
        icon_button.bind(on_release=self.info_but)
        icon_button.add_widget(button_image)
        label_belii.add_widget(icon_button)

        middle_button_1 = Button(text='start', size_hint=(None, None), size=but_size,
                                 pos=(belii_width * 1 - but_size[0]/2, belii_height))  #\
        middle_button_1.bind(on_release=lambda instance: start())
        label_belii.add_widget(middle_button_1)
        
        middle_button_2 = Button(text='next', size_hint=(None, None), size=but_size,
                                 pos=(belii_width * 2 - but_size[0]/2, belii_height))
        middle_button_2.bind(on_release=lambda instance: next())
        label_belii.add_widget(middle_button_2)

    def on_size(self, *args):
        self.label_belii_rect.size = (self.width, self.height / (self.rows - 1))  # устанавливаем размер прямоугольника для красной полосы

   # def change_color(self, instance):
     #   self.color_index = (self.color_index + 1) % len(self.colors)
     #   instance.background_color = self.colors[self.color_index]
     #   self.text = f"Button {self.button_number}\nColor: {self.color_index + 1}"  # Обновляем текст кнопки

    def info_but(self, instance):
        global android
        text_info = '''
        1. Загадайте существительное
            из 5 букв
        2. Нажмите start
        3. Вам будет 
            предложено слово.
        4. На каждую букву можно
            нажимать, от этого 
            будет меняться цвет.
        5. Бежевый - такая бука есть
            в загаданном слове.
            Серый - буквы нет.
            Желтый - угадали букву и
            ее положение.
        3. Когда для всех
            букв укажите их правильно 
            состояние, нажмите "next"
        4. Продолжайте,
            сверять слова.
        5. Примерно с 3 - 5 
            попытки программа угадает 
            загаданное вами слово.
        6. При ошибки, нажмите
            "start", игра начнется
            сначала.
        '''

        layout = GridLayout(cols=1)

        if android == 0:
            scroll_size = [400, 400]
            scroll_pos = [0, 200]

            label_size = [0.8, None]
            label_height = self.height * 0.8

            popup_size = [400, 500]
        else:
            scroll_size = [Window.size[0]/1.4 -100, Window.size[1]/1.4 - 100]
            scroll_pos = [0, 0]

            label_size = [0.8, None]
            label_height = Window.size[1] * 0.55

            popup_size = [Window.size[0]/1.4, Window.size[1]/1.4]



        scroll_view = ScrollView(size_hint=(None, None), size=scroll_size, pos=scroll_pos)
        label = Label(text=text_info, size_hint=label_size, height=label_height)  #
        scroll_view.add_widget(label)
        layout.add_widget(scroll_view)

        popup = Popup(title='Инструкция', content=layout, size_hint=(None, None), size=popup_size)
        popup.open()


class ColorChangingButton(Button):
    def __init__(self, button_number, **kwargs):  # Добавляем новый параметр button_number
        super().__init__(**kwargs)

        global color_but
        self.colors = color_but

        self.color_index = 0
        self.bind(on_press=self.change_color)
        self.button_number = button_number  # Сохраняем номер кнопки

    def change_color(self, instance):
        global color_tabl
        self.color_index = (self.color_index + 1) % len(self.colors)
        instance.background_color = self.colors[self.color_index]
        #self.text = f"Button {self.button_number}\nColor: {self.color_index + 1}"  # Обновляем текст кнопки
        color_tabl[(self.button_number)//5][(self.button_number)%5] = self.color_index
        print(color_tabl)


class MyApp(App):
    def build(self):
        Config.set('graphics', 'width', '350')  # ширина окна
        Config.set('graphics', 'height', '500')  # высота окна
        return ButtonGrid()

def pull_but(i1_0,i2_0):
    print(1)



def sort_1():
    global massiv_slov,slovo, massiv_slov_our, alfavit, massiv_slov_our_pred
    global alfavit_v, vvod_slov, massiv_slov_our_ves, len_slovo, massiv_slov_our_pred_ves


   # print(np.shape(massiv_slov))

    rows = (len(massiv_slov))
  #  print(rows)


    for i1 in range(rows):
        if  len(massiv_slov[i1]) == len_slovo:
            
            
            #print(massiv_slov[i1],1)
            massiv_slov_our.append(massiv_slov[i1])
            massiv_slov_our_ves.append(0)
    rows = (len(massiv_slov_our))

    massiv_slov_our_pred = massiv_slov_our
    massiv_slov_our_pred_ves = massiv_slov_our_ves

    print(massiv_slov_our_pred[:10])
    print(len(massiv_slov_our_pred))

    print(massiv_slov_our[:10])

   # print(rows)


def sort_slov():
    global massiv_slov_our_ves, massiv_slov_our, alfavit_v, alfavit, vvod_slov, alfavit_pred, alfavit_pred,indicator_pred

    alfavit_v = []


    for i in range(len(alfavit)):
        alfavit_v.append(0)

    for i1 in range(len(massiv_slov_our)):  
        for i2 in range(len(massiv_slov_our[i1])):
            for i3 in range(len(alfavit)):
                if alfavit[i3] == (massiv_slov_our[i1])[i2]:
                    alfavit_v[i3] = alfavit_v[i3] + 1


    print("sort_slov")
    print(alfavit_pred)

    print(alfavit)
    print(indicator_pred, "indicator_pred")
    if indicator_pred == 1: 
        print()
        for i1 in range(len(alfavit)):
            if alfavit_pred.count(alfavit[i1]) == 0:
                alfavit_v[i1] = 0
                print(alfavit[i1])
      #print(massiv_slov_our[i1])
    print(alfavit_v)
    print(alfavit)

   # print(massiv_slov_our_ves,massiv_slov_our)
    for i1 in range(len(massiv_slov_our)):
        massiv_slov_our_ves[i1] = 0
        for i2 in range(len(massiv_slov_our[i1])):

            if len(vvod_slov) == 1:
                    indic = 0
                    for i4 in ALFAVIT:
                        if (massiv_slov_our[i1])[i2] == i4:
                            indic = 1
                    if  indic == 1:
                        massiv_slov_our[i1] = (massiv_slov_our[i1])[:i2] + slovar[(massiv_slov_our[i1])[i2]] + (massiv_slov_our[i1])[i2+1:]

            for i3 in range(len(alfavit)):

                first = massiv_slov_our[i1].find((massiv_slov_our[i1])[i2])
                if alfavit[i3] == (massiv_slov_our[i1])[i2] and first==i2:
                    massiv_slov_our_ves[i1]  = massiv_slov_our_ves[i1] + alfavit_v[i3]


  

    #соединим два списка специальной функцией zip
    x = zip(massiv_slov_our_ves, massiv_slov_our)

    #x теперь [(3, 'a'), (1, 'b'), (2, 'c')]

    #отсортируем, взяв первый элемент каждого списка как ключ
    xs = sorted(x, key=lambda tup: tup[0], reverse=True)

    #xs = [(1, 'b'), (2, 'c'), (3, 'a')]

    #и последний шаг - извлечем
    massiv_slov_our_ves = [x[0] for x in xs]
    massiv_slov_our = [x[1] for x in xs]
    print("Количество найденных слов:" ,len(massiv_slov_our), "\nНаиболее вероятные слова:")
    print(len(xs))
    print(len(massiv_slov_our))
    print(xs[0:10])


def sort_net_bykv():
    global massiv_slov_our_ves, massiv_slov_our, alfavit_v, alfavit, slovo, len_slovo, ALFAVIT, slovar
    global alfavit_pred
    print(len(massiv_slov_our))
    massiv_slov_our_s = []
    massiv_slov_our_ves_s = []
    print("sort_net_bykv")


    alfavit_klon = [] 
    for i2 in range(len(alfavit_pred)):
        if not(alfavit_pred[i2] in (slovo[4:])):
            alfavit_klon.append(alfavit_pred[i2])
        
    alfavit_pred = alfavit_klon

    

    for i1 in range(len(massiv_slov_our)):
        indicator_sl = 0
        

        for i2 in range(len(slovo[4:])):
            i3=0
            indicator_b = 0

            len_slovo_our = len(massiv_slov_our[i1])
            #print(massiv_slov_our[i1])
            #print(len_slovo_our)
            for i3 in range(len_slovo_our):
                if  not(slovo[i2+4] == (massiv_slov_our[i1])[i3]):
                    indicator_b +=1
            if indicator_b==len_slovo_our:
                indicator_sl += 1
                


        #print(indicator_sl,len(slovo[4:]))
        if indicator_sl == len(slovo[4:]):
            #print(massiv_slov_our_s)
            massiv_slov_our_s.append(massiv_slov_our[i1])
            massiv_slov_our_ves_s.append(massiv_slov_our_ves[i1])
    
    massiv_slov_our = massiv_slov_our_s
    massiv_slov_our_ves = massiv_slov_our_ves_s
    print(len(massiv_slov_our))


    print("Удаляю слова, содержащие следующие буквы: ", slovo[4:])


def sort_est_bykv():
    global massiv_slov_our_ves, massiv_slov_our, alfavit_v, alfavit, slovo, len_slovo, ALFAVIT, slovar
    global massiv_slov_our_pred_ves, massiv_slov_our_pred, indicator_pred,  alfavit_pred
    
    print("Удаляю слова, без следующих букв: ", slovo[4:])
    massiv_slov_our_s = []
    massiv_slov_our_ves_s = []

    alfavit_klon = [] 
    for i2 in range(len(alfavit_pred)):
        if not(alfavit_pred[i2] in (slovo[4:])):
            alfavit_klon.append(alfavit_pred[i2])
        
    alfavit_pred = alfavit_klon


    for i1 in range(len(massiv_slov_our)):
        indicator_sl = 0

        for i2 in range(len(slovo[4:])):
            i3=0
            len_slovo_our = len(massiv_slov_our[i1]) - 1
            #print(massiv_slov_our[i1])
            #print(len_slovo_our)
            while i3 <= len_slovo_our and not(slovo[i2+4] == (massiv_slov_our[i1])[i3]):
                
                i3 +=1
            #print(i3, len_slovo_our)
            if i3 <= len_slovo_our:
             #   print(slovo[i2+4], (massiv_slov_our[i1])[i3], "(massiv_slov_our[i1])[i2]")
                if  slovo[i2+4] == (massiv_slov_our[i1])[i3]:
                    indicator_sl +=1
        #print(indicator_sl,len(slovo[4:]))
        if indicator_sl == len(slovo[4:]):
           # print(massiv_slov_our_s)
            massiv_slov_our_s.append(massiv_slov_our[i1])
            massiv_slov_our_ves_s.append(massiv_slov_our_ves[i1])
        

    
    massiv_slov_our = massiv_slov_our_s
    massiv_slov_our_ves = massiv_slov_our_ves_s
    #**print(massiv_slov_our_s_2)
    print(len(massiv_slov_our))
    

    print(len(massiv_slov_our_pred))
   # print(massiv_slov_our_pred)


   # print(massiv_slov_our)

    print("Удалил слова, без следующих букв: ", slovo[4:])






def sort_po_bykvam():
    global massiv_slov_our_ves, massiv_slov_our, alfavit_v, alfavit, slovo, len_slovo, ALFAVIT, slovar
    massiv_slov_our_s = []
    massiv_slov_our_ves_s = []
    print("Удаляю слова, без букв на определенной позиции и других букв")

    for i1 in range(len(massiv_slov_our)):


        indicator_sl = 0
        indicator_b = 0


        for i2 in range(len(massiv_slov_our[i1])):
            if slovo[i2] == (massiv_slov_our[i1])[i2] or slovo[i2] == "*":
                indicator_sl += 1


        if indicator_sl == len_slovo:
            massiv_slov_our_s.append(massiv_slov_our[i1])
            massiv_slov_our_ves_s.append(massiv_slov_our_ves[i1])
    
    massiv_slov_our = massiv_slov_our_s
    massiv_slov_our_ves = massiv_slov_our_ves_s

    print("закончил убирать неподходящие слова\n ")

def info():


    print("Инструкция: ")
    print("1. Введите слово, заменяя звездочками буквы.")
    print("2. Возможны следующие варианты:")
    print(" 2.1 пишем слово, заменяя звездочками все неизвестные буквы. При чем буквы стоят на нужных позициях")
    print(" 2.2 пишем буквы, какие есть в слове: (is: крб)")
    print(" 2.2 пишем буквы каких нет в слове: (no: крб)")
    print(" 3. На каждом этапе будут выводится перве 10 слов наиболее подходящих под критерии,") 
    print("    рядом с ними будут написаны веса. Чем больше вес, тем более подходящее слово")
    print('Введите слово, заменяя буквы звездочками:\n')


def start():
    global color_tabl, vvod_slov, massiv_slov, buttons, massiv_slov_our, adres, slovo_na_ekrane

    vvod_slov = []
    color_tabl = [[0,0,0,0,0], [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    massiv_slov = np.loadtxt(adres, delimiter=";", dtype=str, encoding='utf-8')

    start_0()


    rand = min(len(massiv_slov_our), 9)
    rand = random.randint(0,rand)
    slovo_na_ekrane = massiv_slov_our[rand]

    for i1 in range(5):
        for i2 in range(5):
            buttons[(i1, i2)].background_color = color_but[color_tabl[i1][i2]]  # Изменяем цвет кнопки на красный (R, G, B, A)
            
            if i1 == 0:
                buttons[(i1, i2)].text = (slovo_na_ekrane)[i2]
            else:
                buttons[(i1, i2)].text =""



def next():
    global slovo, massiv_slov_our, massiv_slov_our, massiv_slov_our_pred_ves, buttons, slovo_na_ekrane
    global vvod_slov, color_one, color_tabl, massiv_slov_our_pred, massiv_slov_our_ves, indicator_pred
    slovo = slovo_na_ekrane
    slovo_1 = slovo
    vvod_slov.append(slovo)

    color_one = color_tabl[len(vvod_slov)-1]# [1, 2, 0, 0, 0]  0 - нет такой буквы; 1 - есть буква; 2 -  угадали с местом


    slova = [[],[],[]]
    for i3 in range(len(color_one)):
        if color_one[i3] == 0:
            slova[0].append(slovo[i3])
        
        if color_one[i3] == 1 or color_one[i3] == 2:
            slova[1].append(slovo[i3])
        
        if color_one[i3] == 2:
            slova[2].append(slovo[i3])
        

    if not(len(slova[0]) == 0):
        slovo = ["n", "o",":"," "] + slova[0]

        sort_net_bykv()

        slovo = slovo_1



    if not(len(slova[1]) == 0):

        slovo = ["i", "s",":"," "] + slova[1]
        
        sort_est_bykv()

        slovo = slovo_1




    if not(len(slova[2]) == 0):
        slovo = []
        
        for i2 in range(len(color_one)):
            if color_one[i2] == 2:
                slovo.append(slovo_1[i2])

            else:
                slovo.append("*")



        sort_po_bykvam()

        slovo = slovo_1

   # print(massiv_slov_our_pred)
 #   print(len(massiv_slov_our))
 #   print(len(massiv_slov_our_pred))
    print(len(massiv_slov_our))








    if len(massiv_slov_our)>=10:
        #print(len(massiv_slov_our))
       # print(len(massiv_slov_our_pred))

        indicator_pred = 1

        massiv_slov_our, massiv_slov_our_pred = massiv_slov_our_pred, massiv_slov_our
        massiv_slov_our_ves, massiv_slov_our_pred_ves = massiv_slov_our_pred_ves, massiv_slov_our_ves
        sort_slov()
        print(massiv_slov_our[:10])
        massiv_slov_our, massiv_slov_our_pred = massiv_slov_our_pred, massiv_slov_our
        massiv_slov_our_ves, massiv_slov_our_pred_ves = massiv_slov_our_pred_ves, massiv_slov_our_ves
        print(massiv_slov_our[:10])
        print("srt_089")

        indicator_pred == 0
    else:
        indicator_pred == 0
        sort_slov()

    print("next")


    i1 = len(vvod_slov)
    print(len(massiv_slov_our))
    print(massiv_slov_our[0])

    if len(massiv_slov_our)>=10:
        rand = min(len(massiv_slov_our_pred), 9)
        rand = random.randint(0,rand)
        slovo_na_ekrane = massiv_slov_our_pred[rand]

    else:
        slovo_na_ekrane = massiv_slov_our[0]



    color_tabl[i1] = [0,0,0,0,0]

    for i2 in range(5):
        buttons[(i1, i2)].background_color = color_but[color_tabl[i1][i2]]  
        buttons[(i1, i2)].text = slovo_na_ekrane[i2]








def start_0():
    global sort_slov, massiv_slov, massiv_slov, massiv_slov_our_ves
    global massiv_slov_our_pred_ves, massiv_slov_our_pred, massiv_slov_our
    global indicator_pred, vvod_slov, len_slovo, alfavit_pred, alfavit
    massiv_slov = np.loadtxt(adres,   delimiter=";",dtype=str,encoding='utf-8')#cp1251
    print(len(massiv_slov))
    print(massiv_slov[:10])
    massiv_slov = list(massiv_slov)
    massiv_slov_our = []
    massiv_slov_our_ves = []

    indicator_pred = 0

    alfavit_pred = alfavit



    vvod_slov = []

    len_slovo = 5

    sort_1()
    sort_slov()

   

#def sort_next():




alfavit = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
 "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

alfavit_pred = alfavit


color_but = ["#B4AC93", "#F0E5C2", "#FFCC00"]

color_tabl = [[0,0,0,0,0], [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
ALFAVIT = [alfavit1.upper() for alfavit1 in alfavit]
#print(ALFAVIT)
slovar = dict(zip(ALFAVIT, alfavit))



alfavit_v = []
for i in range(len(alfavit)):
    alfavit_v.append(0)





if android == 0:

    import os
    
    #adres = 'data/singular.txt'#russian.txt
   # current_directory = os.path.realpath(__file__)
   # current_directory = os.path.abspath(__file__)

    direc = "C:/Users/Admin/Desktop/Project/slova_tinkoff/2.1"
    
    
else:
    direc = "./data"

adres = direc+"/singular.txt"

print(adres)

#adres = 'data/singular.txt'#russian.txt
#adres = "./data/singular.txt"
#adres = resource_find('singular', 'singular.txt')

start_0()
MyApp().run()

#slovo = str(input())

#vvod_slov.append(slovo)






