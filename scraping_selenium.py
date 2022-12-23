#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:10:19 2021

@author: tryopx80p
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import random
import requests



list1 = [1, 2, 3]

driver= webdriver.Chrome()
driver.get("https://redjum.pj.gob.pe/redjum/#/")
btn_rango_periodos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[2]/ul/li[4]/a')
time.sleep(1)
btn_rango_periodos.click()
input_captcha= driver.find_element(By.XPATH, '//*[@id="captcha"]')
valor_captcha = input('Ingresa el valor del Captcha:')
input_captcha.send_keys(valor_captcha)
btn_captcha= driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button')
btn_captcha.click()
time.sleep(1)
contador_contenido = 2;
lista_deudores = []
while True:
    try:   
        
        contador_filas = 2;        
        while True:            
            deudor = {}
            deuda = {}   
            lista_deuda = []            
            try:
                nombre_deudor = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/table/tbody/tr['+ str(contador_filas) +']/td[2]').text
                deudor['nombreDeudor'] = nombre_deudor                
                tipo_documento = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/table/tbody/tr['+ str(contador_filas) +']/td[3]').text
                deudor['tipoDocumento'] = tipo_documento
                numero_documento = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/table/tbody/tr['+ str(contador_filas) +']/td[4]').text
                deudor['numeroDocumento'] = numero_documento
                btn_detalle = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/table/tbody/tr['+ str(contador_filas) +']/td[6]/button')
                btn_detalle.click()
                time.sleep(random.choice(list1))
                lugar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]').text
                deuda['lugar'] = lugar
                a_favor = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[7]/td[3]').text
                deuda['afavor'] = a_favor            
                moneda = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[8]/td/div/table/tbody/tr/td[1]').text
                deuda['moneda'] = moneda                
                monto = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr[8]/td/div/table/tbody/tr/td[2]').text
                deuda['monto'] = monto
                contador_filas += 1                
                lista_deudores.append(deudor)                
                lista_deuda.append(deuda)
                deudor['deudas'] = lista_deuda      
                btn_cerrar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/button')
                time.sleep(random.choice(list1))
                btn_cerrar.click()                
            except Exception as e:
                print(e)
                break        
        contador_contenido += 1
        btn_siguiente= driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/ul/li['+ str(contador_contenido) +']/a')
        time.sleep(random.choice(list1))
        btn_siguiente.click()
    except Exception as e:
        print(e)
        break
 

driver.close()
api_key = "http://localhost:9090/deudores";
data = requests.post(api_key, json = lista_deudores)
if(data.status_code == 200):
    data = data.json()    
    print(data)
else:
    print(data)
        