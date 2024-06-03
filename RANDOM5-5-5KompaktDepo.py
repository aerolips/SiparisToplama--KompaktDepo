import numpy as np
import pandas as pd

environment_rows = 6
environment_columns = 6

rewards_control = np.full((environment_rows, environment_columns), 0)
rewards_kat1 = np.full((environment_rows, environment_columns), 0)
rewards_kat2 = np.full((environment_rows, environment_columns), 0)
rewards_kat3 = np.full((environment_rows, environment_columns), 0)
rewards_kat4 = np.full((environment_rows, environment_columns), 0)
rewards_kat5 = np.full((environment_rows, environment_columns), 0)

csv_data = pd.read_csv("C:/Users/Ali Gündüz/Desktop/RANDOM25siparis12.csv")
siparissayisi25 = 1
siparissayisi = 25

for index, row in csv_data.iterrows():
    satir = int(row['satir'])
    sutun = int(row['sutun'])
    rewards_kat1[satir][sutun] = row['rewards_kat1']
    rewards_kat2[satir][sutun] = row['rewards_kat2']
    rewards_kat3[satir][sutun] = row['rewards_kat3']
    rewards_kat4[satir][sutun] = row['rewards_kat4']
    rewards_kat5[satir][sutun] = row['rewards_kat5']
    rewards_control[satir, sutun] = int(row['urunsayisi'])
    
capacity_values = np.zeros((environment_rows, environment_columns))
for i in range(1, 6):
  capacity_values[0, i] = 5
for j in range(1, 6):
  capacity_values[1, j] = 5
for o in range(1, 6):
  capacity_values[2, o] = 5
for ı in range(1, 6):
  capacity_values[3, ı] = 5
for u in range(1, 6):
  capacity_values[4, u] = 5

for i in range(6):
    capacity_values[i, 0] = -1000
capacity_values[5,1] = -1000
capacity_values[5,2] = -1000
capacity_values[5,4] = -1000
capacity_values[5,5] = -1000

def get_starting_location():
    current_row_index = 0
    current_column_index = 0
    return current_row_index, current_column_index

def next_location(order_number):
    next_row_index = int(csv_data.loc[csv_data['sira'] == order_number, 'satir'].iloc[0])
    next_column_index = int(csv_data.loc[csv_data['sira'] == order_number, 'sutun'].iloc[0])
    return next_row_index, next_column_index

def get_difference(current_state, next_state):
    row_difference = next_state[0] - current_state[0]
    column_difference = next_state[1] - current_state[1]
    return row_difference, column_difference

def kutu(current_state):
    global kutuyok
    kutuyok = 0
    kutuhareket = [current_state]
    if rewards_kat2[current_state[0], current_state[1]] == 2:
        if current_state[0] == 0:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                else:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 4:
                kutuhareket.append('kutuyok')
                kutuyok = 1
             
        elif current_state[0] > 0:
            if capacity_values[current_state[0], current_state[1]] == 5:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 4:
                kutuhareket.append('kutuyok')
                kutuyok = 1
            
    if rewards_kat2[current_state[0], current_state[1]] == 0 and rewards_kat3[current_state[0], current_state[1]] == 3:
        if current_state[0] == 0:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 5:
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 1 or current_state[1] == 2 or current_state[1] == 3:
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 5:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 1 or current_state[1] == 2 or current_state[1] == 3:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 3:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                                          
        if current_state[0] == 1:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1 or current_state[1] == 4 or current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 3:
                kutuhareket.append('kutuyok')
                kutuyok = 1   
         
        elif current_state[0] > 1:
            if capacity_values[current_state[0], current_state[1]] == 5:
                for a in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 4:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 3:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                          
    if rewards_kat2[current_state[0], current_state[1]] == 0 and rewards_kat3[current_state[0], current_state[1]] == 0 and rewards_kat4[current_state[0], current_state[1]] == 4:
        if current_state[0] == 0:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 3:
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state) 
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 5:
                    for a in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 1 or current_state[1] == 2:
                    for a in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 3:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state) 
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 5:
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 1 or current_state[1] == 2:
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 3:
                if current_state[1] == 3:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 5:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                elif current_state[1] == 1 or current_state[1] == 2:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
            if capacity_values[current_state[0], current_state[1]] == 2:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                           
        if current_state[0] == 1:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 4:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                elif current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)      
                if current_state[1] == 1 or current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 4:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
                elif current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)  
                    
                if current_state[1] == 1 or current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 3:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            
            if capacity_values[current_state[0], current_state[1]] == 2:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                
        if current_state[0] == 2:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 1:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 2:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3: 
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                for a in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 3:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 2:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                
        if current_state[0] == 3 or current_state[0] == 4:
            if capacity_values[current_state[0], current_state[1]] == 5:
                for a in range(3):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(3):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                for m in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for n in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 4:
                for m in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for n in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 3:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 2:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                             
    if rewards_kat2[current_state[0], current_state[1]] == 0 and rewards_kat3[current_state[0], current_state[1]] == 0 and rewards_kat4[current_state[0], current_state[1]] == 0 and rewards_kat5[current_state[0], current_state[1]] == 5:
        if current_state[0] == 0:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 1:
                    for a in range(4):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for b in range(4):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    for a in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 5:
                    for a in range(4):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for b in range(4):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 1:
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
            
            if capacity_values[current_state[0], current_state[1]] == 3:
                if current_state[1] == 1:
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 5:
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 2:
                if current_state[1] == 1:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 4:
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
                if current_state[1] == 5:
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 1:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                        
        if current_state[0] == 1:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for m in range(3):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for n in range(3):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    for a in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 3:
                if current_state[1] == 5:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 4:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 3:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 2:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 1:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                                       
        if current_state[0] == 2:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                   for m in range(2):
                       current_state = (current_state[0] - 1, current_state[1])
                       kutuhareket.append(current_state)
                   for n in range(2):
                       current_state = (current_state[0] + 1, current_state[1])
                       kutuhareket.append(current_state)
                   current_state = (current_state[0] - 1, current_state[1])
                   kutuhareket.append(current_state)
                   current_state = (current_state[0] + 1, current_state[1])
                   kutuhareket.append(current_state)
                   for k in range(2):
                       current_state = (current_state[0], current_state[1] - 1)
                       kutuhareket.append(current_state)
                   for l in range(2):
                       current_state = (current_state[0], current_state[1] + 1)
                       kutuhareket.append(current_state)
                   current_state = (current_state[0], current_state[1] - 1)
                   kutuhareket.append(current_state)
                   current_state = (current_state[0], current_state[1] + 1)
                   kutuhareket.append(current_state)
                if current_state[1] == 4:
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1 or current_state[1] == 3:
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    for k in range(2):
                        current_state = (current_state[0], current_state[1] + 1)
                        kutuhareket.append(current_state)
                    for l in range(2):
                        current_state = (current_state[0], current_state[1] - 1)
                        kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                if current_state[1] == 5:
                   for m in range(2):
                       current_state = (current_state[0] - 1, current_state[1])
                       kutuhareket.append(current_state)
                   for n in range(2):
                       current_state = (current_state[0] + 1, current_state[1])
                       kutuhareket.append(current_state)
                   current_state = (current_state[0] - 1, current_state[1])
                   kutuhareket.append(current_state)
                   current_state = (current_state[0] + 1, current_state[1])
                   kutuhareket.append(current_state)
                   current_state = (current_state[0], current_state[1] - 1)
                   kutuhareket.append(current_state)
                   current_state = (current_state[0], current_state[1] + 1)
                   kutuhareket.append(current_state)
                if current_state[1] == 4:
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1 or current_state[1] == 3:
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    for a in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 3:
                   for m in range(2):
                       current_state = (current_state[0] - 1, current_state[1])
                       kutuhareket.append(current_state)
                   for n in range(2):
                       current_state = (current_state[0] + 1, current_state[1])
                       kutuhareket.append(current_state)
                   current_state = (current_state[0] - 1, current_state[1])
                   kutuhareket.append(current_state)
                   current_state = (current_state[0] + 1, current_state[1])
                   kutuhareket.append(current_state)
                   
            if capacity_values[current_state[0], current_state[1]] == 2:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 1:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                         
        if current_state[0] == 3:
            if capacity_values[current_state[0], current_state[1]] == 5:
                if current_state[1] == 5:
                    for a in range(3):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 1 or current_state[1] == 3 or current_state[1] == 4:
                    for a in range(3):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                if current_state[1] == 2:
                    for a in range(3):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for b in range(3):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    for m in range(2):
                        current_state = (current_state[0] - 1, current_state[1])
                        kutuhareket.append(current_state)
                    for n in range(2):
                        current_state = (current_state[0] + 1, current_state[1])
                        kutuhareket.append(current_state)
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] - 1)
                    kutuhareket.append(current_state)
                    current_state = (current_state[0], current_state[1] + 1)
                    kutuhareket.append(current_state)
                    
            if capacity_values[current_state[0], current_state[1]] == 4:
                for a in range(3):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(3):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                for m in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for n in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                          
            if capacity_values[current_state[0], current_state[1]] == 3:
                for a in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 2: 
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 1:
                kutuhareket.append('kutuyok')
                kutuyok = 1
          
        if current_state[0] == 4:
            if capacity_values[current_state[0], current_state[1]] == 5:
                for a in range(4):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for b in range(4):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                for m in range(3):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for n in range(3):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                for k in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for l in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 4:
                for m in range(3):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for n in range(3):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                for k in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for l in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
            
            if capacity_values[current_state[0], current_state[1]] == 3:
                for k in range(2):
                    current_state = (current_state[0] - 1, current_state[1])
                    kutuhareket.append(current_state)
                for l in range(2):
                    current_state = (current_state[0] + 1, current_state[1])
                    kutuhareket.append(current_state)
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 2:
                current_state = (current_state[0] - 1, current_state[1])
                kutuhareket.append(current_state)
                current_state = (current_state[0] + 1, current_state[1])
                kutuhareket.append(current_state)
                
            if capacity_values[current_state[0], current_state[1]] == 1:
                kutuhareket.append('kutuyok')
                kutuyok = 1
                                   
    return kutuhareket

def hareket(current_state, fark):
    route = [current_state]
    if fark[0] != 0:
        if fark[0] == 1:
            current_state = (current_state[0] + 1, current_state[1])
            route.append(current_state)   
        if fark[0] == 2:
            for i in range(2):
                current_state = (current_state[0] + 1, current_state[1])
                route.append(current_state) 
        if fark[0] == 3:
            for i in range(3):
                current_state = (current_state[0] + 1, current_state[1])
                route.append(current_state)
        if fark[0] == 4:
            for i in range(4):
                current_state = (current_state[0] + 1, current_state[1])
                route.append(current_state)
        if fark[0] == 5:
            for i in range(5):
                current_state = (current_state[0] + 1, current_state[1])
                route.append(current_state)
                
        if fark[0] == -1:
            current_state = (current_state[0] - 1, current_state[1])
            route.append(current_state)
        if fark[0] == -2:
            for i in range(2):
                current_state = (current_state[0] - 1, current_state[1])
                route.append(current_state) 
        if fark[0] == -3:
            for i in range(3):
                current_state = (current_state[0] - 1, current_state[1])
                route.append(current_state)
        if fark[0] == -4:
            for i in range(4):
                current_state = (current_state[0] - 1, current_state[1])
                route.append(current_state)
        if fark[0] == -5:
            for i in range(5):
                current_state = (current_state[0] - 1, current_state[1])
                route.append(current_state)
    
    if fark[1] != 0:
        if fark[1] == 1:
            current_state = (current_state[0], current_state[1] + 1)
            route.append(current_state)
        if fark[1] == 2:
            for i in range(2):
                current_state = (current_state[0], current_state[1] + 1)
                route.append(current_state)
        if fark[1] == 3:
            for i in range(3):
                current_state = (current_state[0], current_state[1] + 1)
                route.append(current_state)
        if fark[1] == 4:
            for i in range(4):
                current_state = (current_state[0], current_state[1] + 1)
                route.append(current_state)
        if fark[1] == 5:
            for i in range(5):
                current_state = (current_state[0], current_state[1] + 1)
                route.append(current_state)
                
        if fark[1] == -1:
            current_state = (current_state[0], current_state[1] - 1)
            route.append(current_state)
        if fark[1] == -2:
            for i in range(2):
                current_state = (current_state[0], current_state[1] - 1)
                route.append(current_state) 
        if fark[1] == -3:
            for i in range(3):
                current_state = (current_state[0], current_state[1] - 1)
                route.append(current_state)
        if fark[1] == -4:
            for i in range(4):
                current_state = (current_state[0], current_state[1] - 1)
                route.append(current_state)
        if fark[1] == -5:
            for i in range(5):
                current_state = (current_state[0], current_state[1] - 1)
                route.append(current_state)

    return route, current_state

current_state = get_starting_location()
next_order_number = 1
kat = 0
toplanansiparis = 0
islemsayisi = 0

# 1. Siparişin Konumuna Gidilmesi
if current_state[0] == 0 and current_state[1] == 0 and next_order_number == 1:
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route1 = route
    print("Optimal Route:", route1)
    print(current_state)
    konum1 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
# 1. Siparişin İstasyona Teslim Edilmesi
if toplanansiparis == 1:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route1_9 = []
            else:
                route1_9 = kutuhareket
                print("Optimal Route:", route1_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
    
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route2 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route2)
    print(current_state)
    konum2 = current_state
    print("------------------------------------------------------------------------")
#1. Siparişin Kutusunun Düzeltilmesi ve 2. Siparişe Gitmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 1:
    if kat == 1:
        if kutuyok == 0:
            route2_1 = route2[::-1] + route1_9[::-1]
            current_state = konum1
            kat = -1
            print("Optimal Route:", route2_1)
            next_order_number = 2
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route3 = route
            print("Optimal Route:", route3)
            print(current_state)
            konum3 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            next_order_number = 2
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route3 = route
            print("Optimal Route:", route3)
            print(current_state)
            konum3 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")     
    else:
        next_order_number = 2
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route3 = route
        print("Optimal Route:", route3)
        print(current_state)
        konum3 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#2. Siparişin İstasyona Götürülmesi
if toplanansiparis == 2:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route3_1 = []
            else:
                route3_1 = kutuhareket
                print("Optimal Route:", route3_1)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
    
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route4 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route4)
    print(current_state)
    konum4 = current_state
    print("------------------------------------------------------------------------")
#2. Siparişin Kutusunun Düzeltilmesi ve 3. Siparişe Gitmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 2:
    if kat == 1:
        if kutuyok == 0:
            route4_9 = route4[::-1] + route3_1[::-1]
            current_state = konum3
            kat = -1
            print("Optimal Route:", route4_9)
            next_order_number = 3
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route5 = route
            print("Optimal Route:", route5)
            print(current_state)
            konum5 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            next_order_number = 3
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route5 = route
            print("Optimal Route:", route5)
            print(current_state)
            konum5 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
    else:
        next_order_number = 3
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route5 = route
        print("Optimal Route:", route5)
        print(current_state)
        konum5 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#3. Siparişin İstasyona Bırakılması
if toplanansiparis == 3:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route5_9 = []
            else:
                route5_9 = kutuhareket
                print("Optimal Route:", route5_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
    
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route6 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route6)
    print(current_state)
    konum6 = current_state
    print("------------------------------------------------------------------------")
#3. Siparişin Kutusunun Düzeltilmesi Gerekiyorsa Düzeltilmesi ve 4. Siparişe Gidilmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 3:
    if kat == 1:
        if kutuyok == 0:
            route6_9 = route6[::-1] + route5_9[::-1]
            current_state = konum5
            kat = -1
            print("Optimal Route:", route6_9)
            next_order_number = 4
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route7 = route
            print("Optimal Route:", route7)
            print(current_state)
            konum7 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            next_order_number = 4
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route7 = route
            print("Optimal Route:", route7)
            print(current_state)
            konum7 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
    else:
        next_order_number = 4
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route7 = route
        print("Optimal Route:", route7)
        print(current_state)
        konum7 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#4. Siparişin İstasyona Bırakılması
if toplanansiparis == 4:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route7_9 = []
            else:
                route7_9 = kutuhareket
                print("Optimal Route:", route7_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
    
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route8 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route8)
    print(current_state)
    konum8 = current_state
    print("------------------------------------------------------------------------")
#4. Siparişin Kutusunun Düzeltilmesi Gerekiyorsa Düzeltilmesi ve 5. Siparişe Gidilmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 4:
    if kat == 1:
        if kutuyok == 0:
            route8_9 = route8[::-1] + route7_9[::-1]
            current_state = konum7
            kat = -1
            print("Optimal Route:", route8_9)
            next_order_number = 5
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route9 = route
            print("Optimal Route:", route9)
            print(current_state)
            konum9 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            next_order_number = 5
            next_state = next_location(next_order_number)
            fark = get_difference(current_state, next_state)
            route, current_state = hareket(current_state, fark)
            route9 = route
            print("Optimal Route:", route9)
            print(current_state)
            konum9 = current_state
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
    else:
        next_order_number = 5
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route9 = route
        print("Optimal Route:", route9)
        print(current_state)
        konum9 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#5. Siparişin İstasyona Bırakılması
if toplanansiparis == 5:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route9_9 = []
            else:
                route9_9 = kutuhareket
                print("Optimal Route:", route9_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
    
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route10 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route10)
    print(current_state)
    konum10 = current_state
    print("------------------------------------------------------------------------")
#1. Siparişin Kutusunu Yerine Bırakma
if current_state[0] == 5 and current_state[1] == 3 and toplanansiparis == 5 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route10_8 = route10[::-1] + route9_9[::-1]
            current_state = konum9
            kat = -1
            print("Optimal Route:", route10_8)
            route10_9 = route10
            current_state = konum8
            print("Optimal Route:", route10_9)
            route11 = route2[::-1]
            print("Optimal Route:", route11)
            capacity_values[5, 3] -= 1           
            islemsayisi += 1
            konum11 = konum1
            current_state = konum11
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route11 = route2[::-1]
            print("Optimal Route:", route11)
            capacity_values[5, 3] -= 1 
            islemsayisi += 1
            konum11 = konum1
            current_state = konum11
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route11 = route2[::-1]
        print("Optimal Route:", route11)
        capacity_values[5, 3] -= 1 
        islemsayisi += 1
        konum11 = konum1
        current_state = konum11
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#6. Siparişe Gidilmesi
if islemsayisi == 6:
    next_order_number = 6
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route12 = route
    print("Optimal Route:", route12)
    print(current_state)
    konum12 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#6. Siparişin İstasyona Bırakılması
if toplanansiparis == 6 and islemsayisi == 6:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route12_9 = []
            else:
                route12_9 = kutuhareket
                print("Optimal Route:", route12_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
     
    capacity_values[current_state[0], current_state[1]] -= 1
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route13 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route13)
    print(current_state)
    konum13 = current_state
    print("------------------------------------------------------------------------")
#6. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 2. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 7 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route13_8 = route13[::-1] + route12_9[::-1]
            current_state = konum13
            kat = -1
            print("Optimal Route:", route13_8)
            route13_9 = route13
            current_state = konum10
            print("Optimal Route:", route13_9)
            route14 = route4[::-1]
            print("Optimal Route:", route14)
            capacity_values[5, 3] -= 1           
            islemsayisi += 1
            konum14 = konum3
            current_state = konum14
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route14 = route4[::-1]
            print("Optimal Route:", route14)
            capacity_values[5, 3] -= 1           
            islemsayisi += 1
            konum14 = konum3
            current_state = konum14
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route14 = route4[::-1]
        print("Optimal Route:", route14)
        capacity_values[5, 3] -= 1           
        islemsayisi += 1
        konum14 = konum3
        current_state = konum14
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#7. Siparişe Gidilmesi
if islemsayisi == 8:
    next_order_number = 7
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route15 = route
    print("Optimal Route:", route15)
    print(current_state)
    konum15 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#7. Siparişin İstasyona Bırakılması
if toplanansiparis == 7 and islemsayisi == 8:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route15_9 = []
            else:
                route15_9 = kutuhareket
                print("Optimal Route:", route15_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
                
    capacity_values[current_state[0], current_state[1]] -= 1             
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route16 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route16)
    print(current_state)
    konum16 = current_state
    print("------------------------------------------------------------------------")
#7. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 3. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 9 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route16_8 = route16[::-1] + route15_9[::-1]
            current_state = konum15
            kat = -1
            print("Optimal Route:", route16_8)
            route16_9 = route16
            current_state = konum16
            print("Optimal Route:", route16_9)
            route17 = route6[::-1]
            print("Optimal Route:", route17)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum17 = konum5
            current_state = konum17
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route17 = route6[::-1]
            print("Optimal Route:", route17)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum17 = konum5
            current_state = konum17
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route17 = route6[::-1]
        print("Optimal Route:", route17)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum17 = konum5
        current_state = konum17
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#8. Siparişe Gidilmesi
if islemsayisi == 10:
    next_order_number = 8
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route18 = route
    print("Optimal Route:", route18)
    print(current_state)
    konum18 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#8. Siparişin İstasyona Bırakılması
if toplanansiparis == 8 and islemsayisi == 10:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route18_9 = []
            else:
                route18_9 = kutuhareket
                print("Optimal Route:", route18_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route19 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route19)
    print(current_state)
    konum19 = current_state
    print("------------------------------------------------------------------------")
#8. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 4. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 11 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route19_8 = route19[::-1] + route18_9[::-1]
            current_state = konum18
            kat = -1
            print("Optimal Route:", route19_8)
            route19_9 = route19
            current_state = konum19
            print("Optimal Route:", route19_9)
            route20 = route8[::-1]
            print("Optimal Route:", route20)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum20 = konum7
            current_state = konum20
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route20 = route8[::-1]
            print("Optimal Route:", route20)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum20 = konum7
            current_state = konum20
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route20 = route8[::-1]
        print("Optimal Route:", route20)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum20 = konum7
        current_state = konum20
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#9. Siparişe Gidilmesi
if islemsayisi == 12:
    next_order_number = 9
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route21 = route
    print("Optimal Route:", route21)
    print(current_state)
    konum21 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#9. Siparişin İstasyona Bırakılması
if toplanansiparis == 9 and islemsayisi == 12:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route21_9 = []
            else:
                route21_9 = kutuhareket
                print("Optimal Route:", route21_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route22 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route22)
    print(current_state)
    konum22 = current_state
    print("------------------------------------------------------------------------")
#9. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 5. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 13 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route22_8 = route22[::-1] + route21_9[::-1]
            current_state = konum21
            kat = -1
            print("Optimal Route:", route22_8)
            route22_9 = route22
            current_state = konum22
            print("Optimal Route:", route22_9)
            route23 = route10[::-1]
            print("Optimal Route:", route23)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum23 = konum9
            current_state = konum23
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route23 = route10[::-1]
            print("Optimal Route:", route23)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum23 = konum9
            current_state = konum23
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route23 = route10[::-1]
        print("Optimal Route:", route23)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum23 = konum9
        current_state = konum23
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#10. Siparişe Gidilmesi
if islemsayisi == 14:
    next_order_number = 10
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route24 = route
    print("Optimal Route:", route24)
    print(current_state)
    konum24 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#10. Siparişin İstasyona Bırakılması
if toplanansiparis == 10 and islemsayisi == 14:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route24_9 = []
            else:
                route24_9 = kutuhareket
                print("Optimal Route:", route24_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route25 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route25)
    print(current_state)
    konum25 = current_state
    print("------------------------------------------------------------------------")
#10. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 6. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 15 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route25_8 = route25[::-1] + route24_9[::-1]
            current_state = konum24
            kat = -1
            print("Optimal Route:", route25_8)
            route25_9 = route25
            current_state = konum25
            print("Optimal Route:", route25_9)
            route26 = route13[::-1]
            print("Optimal Route:", route26)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum26 = konum12
            current_state = konum26
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route26 = route13[::-1]
            print("Optimal Route:", route26)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum26 = konum12
            current_state = konum26
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route26 = route13[::-1]
        print("Optimal Route:", route26)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum26 = konum12
        current_state = konum26
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#11. Siparişe Gidilmesi
if islemsayisi == 16:
    next_order_number = 11
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route27 = route
    print("Optimal Route:", route27)
    print(current_state)
    konum27 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#11. Siparişin İstasyona Bırakılması
if toplanansiparis == 11 and islemsayisi == 16:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route27_9 = []
            else:
                route27_9 = kutuhareket
                print("Optimal Route:", route27_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route28 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route28)
    print(current_state)
    konum28 = current_state
    print("------------------------------------------------------------------------")
#11. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 7. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 17 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route28_8 = route28[::-1] + route27_9[::-1]
            current_state = konum27
            kat = -1
            print("Optimal Route:", route28_8)
            route28_9 = route28
            current_state = konum28
            print("Optimal Route:", route28_9)
            route29 = route16[::-1]
            print("Optimal Route:", route29)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum29 = konum15
            current_state = konum29
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route29 = route16[::-1]
            print("Optimal Route:", route29)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum29 = konum15
            current_state = konum29
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route29 = route16[::-1]
        print("Optimal Route:", route29)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum29 = konum15
        current_state = konum29
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#12. Siparişe Gidilmesi
if islemsayisi == 18:
    next_order_number = 12
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route30 = route
    print("Optimal Route:", route30)
    print(current_state)
    konum30 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#12. Siparişin İstasyona Bırakılması
if toplanansiparis == 12 and islemsayisi == 18:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route30_9 = []
            else:
                route30_9 = kutuhareket
                print("Optimal Route:", route30_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route31 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route31)
    print(current_state)
    konum31 = current_state
    print("------------------------------------------------------------------------")
#12. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 8. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 19 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route31_8 = route31[::-1] + route30_9[::-1]
            current_state = konum30
            kat = -1
            print("Optimal Route:", route31_8)
            route31_9 = route31
            current_state = konum31
            print("Optimal Route:", route31_9)
            route32 = route19[::-1]
            print("Optimal Route:", route32)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum32 = konum18
            current_state = konum32
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route32 = route19[::-1]
            print("Optimal Route:", route32)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum32 = konum18
            current_state = konum32
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route32 = route19[::-1]
        print("Optimal Route:", route32)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum32 = konum18
        current_state = konum32
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#13. Siparişe Gidilmesi
if islemsayisi == 20:
    next_order_number = 13
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route33 = route
    print("Optimal Route:", route33)
    print(current_state)
    konum33 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#13. Siparişin İstasyona Bırakılması
if toplanansiparis == 13 and islemsayisi == 20:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route33_9 = []
            else:
                route33_9 = kutuhareket
                print("Optimal Route:", route33_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route34 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route34)
    print(current_state)
    konum34 = current_state
    print("------------------------------------------------------------------------")
#13. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 9. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 21 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route34_8 = route34[::-1] + route33_9[::-1]
            current_state = konum33
            kat = -1
            print("Optimal Route:", route34_8)
            route34_9 = route34
            current_state = konum34
            print("Optimal Route:", route34_9)
            route35 = route22[::-1]
            print("Optimal Route:", route35)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum35 = konum21
            current_state = konum35
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------") 
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route35 = route22[::-1]
            print("Optimal Route:", route35)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum35 = konum21
            current_state = konum35
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------") 
    else:
        route35 = route22[::-1]
        print("Optimal Route:", route35)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum35 = konum21
        current_state = konum35
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#14. Siparişe Gidilmesi
if islemsayisi == 22:
    next_order_number = 14
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route36 = route
    print("Optimal Route:", route36)
    print(current_state)
    konum36 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#14. Siparişin İstasyona Bırakılması
if toplanansiparis == 14 and islemsayisi == 22:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route36_9 = []
            else:
                route36_9 = kutuhareket
                print("Optimal Route:", route36_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route37 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route37)
    print(current_state)
    konum37 = current_state
    print("------------------------------------------------------------------------")
#14. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 10. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 23 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route37_8 = route37[::-1] + route36_9[::-1]
            current_state = konum36
            kat = -1
            print("Optimal Route:", route37_8)
            route37_9 = route37
            current_state = konum37
            print("Optimal Route:", route37_9)
            route38 = route25[::-1]
            print("Optimal Route:", route38)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum38 = konum24
            current_state = konum38
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route38 = route25[::-1]
            print("Optimal Route:", route38)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum38 = konum24
            current_state = konum38
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route38 = route25[::-1]
        print("Optimal Route:", route38)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum38 = konum24
        current_state = konum38
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#15. Siparişe Gidilmesi
if islemsayisi == 24:
    next_order_number = 15
    next_state = next_location(next_order_number)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route39 = route
    print("Optimal Route:", route39)
    print(current_state)
    konum39 = current_state
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#15. Siparişin İstasyona Bırakılması
if toplanansiparis == 15 and islemsayisi == 24:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            if kutuyok == 1:
                route39_9 = []
            else:
                route39_9 = kutuhareket
                print("Optimal Route:", route39_9)
                
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards_control[current_state[0], current_state[1]] -= 1
        if rewards_kat1[current_state[0], current_state[1]] == 1:
            rewards_kat1[current_state[0], current_state[1]] = 0
        elif rewards_kat2[current_state[0], current_state[1]] == 2:
            rewards_kat2[current_state[0], current_state[1]] = 0
        elif rewards_kat3[current_state[0], current_state[1]] == 3:
            rewards_kat3[current_state[0], current_state[1]] = 0
        elif rewards_kat4[current_state[0], current_state[1]] == 4:
            rewards_kat4[current_state[0], current_state[1]] = 0
        elif rewards_kat5[current_state[0], current_state[1]] == 5:
            rewards_kat5[current_state[0], current_state[1]] = 0
         
    capacity_values[current_state[0], current_state[1]] -= 1 
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    route40 = route
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print("Optimal Route:", route40)
    print(current_state)
    konum40 = current_state
    print("------------------------------------------------------------------------")
#15. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 11. Siparişin Kutusunun Bırakılması
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 25 and capacity_values[5, 3] == 5:
    if kat == 1:
        if kutuyok == 0:
            route40_8 = route40[::-1] + route39_9[::-1]
            current_state = konum39
            kat = -1
            print("Optimal Route:", route40_8)
            route40_9 = route40
            current_state = konum40
            print("Optimal Route:", route40_9)
            route41 = route28[::-1]
            print("Optimal Route:", route41)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum41 = konum27
            current_state = konum41
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            route41 = route28[::-1]
            print("Optimal Route:", route41)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum41 = konum27
            current_state = konum41
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    else:
        route41 = route28[::-1]
        print("Optimal Route:", route41)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum41 = konum27
        current_state = konum41
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")

if siparissayisi == 20 and islemsayisi == 26 or siparissayisi25 == 1:
    #16. Siparişe Gidilmesi
    if islemsayisi == 26:
        next_order_number = 16
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route42 = route
        print("Optimal Route:", route42)
        print(current_state)
        konum42 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #16. Siparişin İstasyona Bırakılması
    if toplanansiparis == 16 and islemsayisi == 26:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route42_9 = []
                else:
                    route42_9 = kutuhareket
                    print("Optimal Route:", route42_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route43 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route43)
        print(current_state)
        konum43 = current_state
        print("------------------------------------------------------------------------")
    #16. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 12. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 27 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route43_8 = route43[::-1] + route42_9[::-1]
                current_state = konum42
                kat = -1
                print("Optimal Route:", route43_8)
                route43_9 = route43
                current_state = konum43
                print("Optimal Route:", route43_9)
                route44 = route31[::-1]
                print("Optimal Route:", route44)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum44 = konum30
                current_state = konum44
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route44 = route31[::-1]
                print("Optimal Route:", route44)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum44 = konum30
                current_state = konum44
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route44 = route31[::-1]
            print("Optimal Route:", route44)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum44 = konum30
            current_state = konum44
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #17. Siparişe Gidilmesi
    if islemsayisi == 28:
        next_order_number = 18
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route45 = route
        print("Optimal Route:", route45)
        print(current_state)
        konum45 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #17. Siparişin İstasyona Bırakılması
    if toplanansiparis == 17 and islemsayisi == 28:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route45_9 = []
                else:
                    route45_9 = kutuhareket
                    print("Optimal Route:", route45_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route46 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route46)
        print(current_state)
        konum46 = current_state
        print("------------------------------------------------------------------------")
    #17. İstasyonun Kutusunun Dönülmesi, İstasyona Dönülmesi, 13. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 29 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route46_8 = route46[::-1] + route45_9[::-1]
                current_state = konum45
                kat = -1
                print("Optimal Route:", route46_8)
                route46_9 = route46
                current_state = konum46
                print("Optimal Route:", route46_9)
                route47 = route34[::-1]
                print("Optimal Route:", route47)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum47 = konum33
                current_state = konum47
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route47 = route34[::-1]
                print("Optimal Route:", route47)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum47 = konum33
                current_state = konum47
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route47 = route34[::-1]
            print("Optimal Route:", route47)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum47 = konum33
            current_state = konum47
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")           
    #18. Siparişe Gidilmesi
    if islemsayisi == 30:
        next_order_number = 18
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route48 = route
        print("Optimal Route:", route48)
        print(current_state)
        konum48 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #18. Siparişin İstasyona Bırakılması
    if toplanansiparis == 18 and islemsayisi == 30:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route48_9 = []
                else:
                    route48_9 = kutuhareket
                    print("Optimal Route:", route48_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route49 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route49)
        print(current_state)
        konum49 = current_state
        print("------------------------------------------------------------------------")
    #18. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 14. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 31 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route49_8 = route49[::-1] + route48_9[::-1]
                current_state = konum48
                kat = -1
                print("Optimal Route:", route49_8)
                route49_9 = route49
                current_state = konum49
                print("Optimal Route:", route49_9)
                route50 = route37[::-1]
                print("Optimal Route:", route50)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum50 = konum36
                current_state = konum50
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route50 = route37[::-1]
                print("Optimal Route:", route50)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum50 = konum36
                current_state = konum50
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route50 = route37[::-1]
            print("Optimal Route:", route50)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum50 = konum36
            current_state = konum50
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #19. Siparişe Gidilmesi
    if islemsayisi == 32:
        next_order_number = 19
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route51 = route
        print("Optimal Route:", route51)
        print(current_state)
        konum51 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #19. Siparişin İstasyona Bırakılması
    if toplanansiparis == 19 and islemsayisi == 32:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route51_9 = []
                else:
                    route51_9 = kutuhareket
                    print("Optimal Route:", route51_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route52 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route52)
        print(current_state)
        konum52 = current_state
        print("------------------------------------------------------------------------")
    #19. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 15. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 33 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route52_8 = route52[::-1] + route51_9[::-1]
                current_state = konum51
                kat = -1
                print("Optimal Route:", route52_8)
                route52_9 = route52
                current_state = konum52
                print("Optimal Route:", route52_9)
                route53 = route40[::-1]
                print("Optimal Route:", route53)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum53 = konum39
                current_state = konum53
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route53 = route40[::-1]
                print("Optimal Route:", route53)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum53 = konum39
                current_state = konum53
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route53 = route40[::-1]
            print("Optimal Route:", route53)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum53 = konum39
            current_state = konum53
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #20. Siparişe Gidilmesi
    if islemsayisi == 34:
        next_order_number = 20
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route54 = route
        print("Optimal Route:", route54)
        print(current_state)
        konum54 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #20. Siparişin İstasyona Bırakılması
    if toplanansiparis == 20 and islemsayisi == 34:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route54_9 = []
                else:
                    route54_9 = kutuhareket
                    print("Optimal Route:", route54_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route55 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route55)
        print(current_state)
        konum55 = current_state
        print("------------------------------------------------------------------------")
    #20. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 16. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 35 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route55_8 = route55[::-1] + route54_9[::-1]
                current_state = konum54
                kat = -1
                print("Optimal Route:", route55_8)
                route55_9 = route55
                current_state = konum55
                print("Optimal Route:", route55_9)
                route56 = route43[::-1]
                print("Optimal Route:", route56)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum56 = konum42
                current_state = konum56
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route56 = route43[::-1]
                print("Optimal Route:", route56)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum56 = konum42
                current_state = konum56
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route56 = route43[::-1]
            print("Optimal Route:", route56)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum56 = konum42
            current_state = konum56
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
 
if siparissayisi == 25 and islemsayisi == 36:
    #21. Siparişe Gidilmesi
    if islemsayisi == 36:
        next_order_number = 21
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route57 = route
        print("Optimal Route:", route57)
        print(current_state)
        konum57 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #21. Siparişin İstasyona Bırakılması
    if toplanansiparis == 21 and islemsayisi == 36:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route57_9 = []
                else:
                    route57_9 = kutuhareket
                    print("Optimal Route:", route57_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route58 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route58)
        print(current_state)
        konum58 = current_state
        print("------------------------------------------------------------------------")
    #21. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 17. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 37 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route58_8 = route58[::-1] + route57_9[::-1]
                current_state = konum57
                kat = -1
                print("Optimal Route:", route58_8)
                route58_9 = route58
                current_state = konum58
                print("Optimal Route:", route58_9)
                route59 = route46[::-1]
                print("Optimal Route:", route59)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum59 = konum45
                current_state = konum59
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route59 = route46[::-1]
                print("Optimal Route:", route59)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum59 = konum45
                current_state = konum59
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route59 = route46[::-1]
            print("Optimal Route:", route59)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum59 = konum45
            current_state = konum59
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #22. Siparişe Gidilmesi
    if islemsayisi == 38:
        next_order_number = 22
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route60 = route
        print("Optimal Route:", route60)
        print(current_state)
        konum60 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #22. Siparişin İstasyona Bırakılması
    if toplanansiparis == 22 and islemsayisi == 38:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route60_9 = []
                else:
                    route60_9 = kutuhareket
                    print("Optimal Route:", route60_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route61 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route61)
        print(current_state)
        konum61 = current_state
        print("------------------------------------------------------------------------")
    #22. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 18. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 39 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route61_8 = route61[::-1] + route60_9[::-1]
                current_state = konum60
                kat = -1
                print("Optimal Route:", route61_8)
                route61_9 = route61
                current_state = konum61
                print("Optimal Route:", route61_9)
                route62 = route49[::-1]
                print("Optimal Route:", route62)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum62 = konum48
                current_state = konum62
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route62 = route49[::-1]
                print("Optimal Route:", route62)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum62 = konum48
                current_state = konum62
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------") 
        else:
            route62 = route49[::-1]
            print("Optimal Route:", route62)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum62 = konum48
            current_state = konum62
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")          
    #23. Siparişe Gidilmesi
    if islemsayisi == 40:
        next_order_number = 23
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route63 = route
        print("Optimal Route:", route63)
        print(current_state)
        konum63 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #23. Siparişin İstasyona Bırakılması
    if toplanansiparis == 23 and islemsayisi == 40:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route63_9 = []
                else:
                    route63_9 = kutuhareket
                    print("Optimal Route:", route63_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route64 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route64)
        print(current_state)
        konum64 = current_state
        print("------------------------------------------------------------------------")
    #23. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 19. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 41 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route64_8 = route64[::-1] + route63_9[::-1]
                current_state = konum63
                kat = -1
                print("Optimal Route:", route64_8)
                route64_9 = route64
                current_state = konum64
                print("Optimal Route:", route64_9)
                route65 = route52[::-1]
                print("Optimal Route:", route65)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum65 = konum51
                current_state = konum65
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route65 = route52[::-1]
                print("Optimal Route:", route65)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum65 = konum51
                current_state = konum65
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route65 = route52[::-1]
            print("Optimal Route:", route65)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum65 = konum51
            current_state = konum65
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #24. Siparişe Gidilmesi
    if islemsayisi == 42:
        next_order_number = 24
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route66 = route
        print("Optimal Route:", route66)
        print(current_state)
        konum66 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #24. Siparişin İstasyona Bırakılması
    if toplanansiparis == 24 and islemsayisi == 42:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route66_9 = []
                else:
                    route66_9 = kutuhareket
                    print("Optimal Route:", route66_9)
                    
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route67 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route67)
        print(current_state)
        konum67 = current_state
        print("------------------------------------------------------------------------")
    #24. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 20. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 43 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route67_8 = route67[::-1] + route66_9[::-1]
                current_state = konum66
                kat = -1
                print("Optimal Route:", route67_8)
                route67_9 = route67
                current_state = konum67
                print("Optimal Route:", route67_9)
                route68 = route55[::-1]
                print("Optimal Route:", route68)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum68 = konum54
                current_state = konum68
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route68 = route55[::-1]
                print("Optimal Route:", route68)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum68 = konum54
                current_state = konum68
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route68 = route55[::-1]
            print("Optimal Route:", route68)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum68 = konum54
            current_state = konum68
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #25. Siparişe Gidilmesi
    if islemsayisi == 44:
        next_order_number = 25
        next_state = next_location(next_order_number)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route69 = route
        print("Optimal Route:", route69)
        print(current_state)
        konum69 = current_state
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #25. Siparişin İstasyona Bırakılması
    if toplanansiparis == 25 and islemsayisi == 44:
        if rewards_kat1[current_state[0], current_state[1]] == 0:
            if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
                kat = 1
                kutuhareket = kutu(current_state)
                if kutuyok == 1:
                    route69_9 = []
                else:
                    route69_9 = kutuhareket
                    print("Optimal Route:", route69_9)
        
        if rewards_control[current_state[0], current_state[1]] == 1:
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards_control[current_state[0], current_state[1]] -= 1
            if rewards_kat1[current_state[0], current_state[1]] == 1:
                rewards_kat1[current_state[0], current_state[1]] = 0
            elif rewards_kat2[current_state[0], current_state[1]] == 2:
                rewards_kat2[current_state[0], current_state[1]] = 0
            elif rewards_kat3[current_state[0], current_state[1]] == 3:
                rewards_kat3[current_state[0], current_state[1]] = 0
            elif rewards_kat4[current_state[0], current_state[1]] == 4:
                rewards_kat4[current_state[0], current_state[1]] = 0
            elif rewards_kat5[current_state[0], current_state[1]] == 5:
                rewards_kat5[current_state[0], current_state[1]] = 0
             
        capacity_values[current_state[0], current_state[1]] -= 1 
        next_state = (5, 3)
        fark = get_difference(current_state, next_state)
        route, current_state = hareket(current_state, fark)
        route70 = route
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print("Optimal Route:", route70)
        print(current_state)
        konum70 = current_state
        print("------------------------------------------------------------------------")
    #25. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 21. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 45 and capacity_values[5, 3] == 5:
        if kat == 1:
            if kutuyok == 0:
                route70_8 = route70[::-1] + route69_9[::-1]
                current_state = konum69
                kat = -1
                print("Optimal Route:", route70_8)
                route70_9 = route70
                current_state = konum70
                print("Optimal Route:", route70_9)
                route71 = route58[::-1]
                print("Optimal Route:", route71)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum71 = konum57
                current_state = konum71
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
            if kutuyok == 1:
                kutuyok = 0
                kat = -1
                route71 = route58[::-1]
                print("Optimal Route:", route71)
                capacity_values[5, 3] -= 1
                islemsayisi += 1
                konum71 = konum57
                current_state = konum71
                capacity_values[current_state[0], current_state[1]] += 1
                print(current_state)
                print("------------------------------------------------------------------------")
        else:
            route71 = route58[::-1]
            print("Optimal Route:", route71)
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum71 = konum57
            current_state = konum71
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
      
if islemsayisi == (siparissayisi*2) - 4:
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)       
    if siparissayisi == 15:
        route42 = route
        print("Optimal Route:", route42)
        print(current_state)
        konum42 = current_state
    if siparissayisi == 20:
        route57 = route
        print("Optimal Route:", route57)
        print(current_state)
        konum57 = current_state
    if siparissayisi == 25:
        route72 = route
        print("Optimal Route:", route72)
        print(current_state)
        konum72 = current_state
    print("------------------------------------------------------------------------")
        
#22. Siparişin Kutusunun Bırakılması(25) / 17. Siparişin Bırakılması(20) / 12. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 4:
    if siparissayisi == 15:
        route43 = route31[::-1]
        print("Optimal Route:", route43)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum43 = konum30
        current_state = konum43
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route58 = route46[::-1]
        print("Optimal Route:", route58)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum58 = konum45
        current_state = konum58
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 25:
        route73 = route61[::-1]
        print("Optimal Route:", route73)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum73 = konum60
        current_state = konum73
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
        
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 3:
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)        
    if siparissayisi == 15:
        route44 = route
        print("Optimal Route:", route44)
        print(current_state)
        konum44 = current_state
    if siparissayisi == 20:
        route59 = route
        print("Optimal Route:", route59)
        print(current_state)
        konum59 = current_state
    if siparissayisi == 25:
        route74 = route
        print("Optimal Route:", route74)
        print(current_state)
        konum74 = current_state
    print("------------------------------------------------------------------------")
        
#23. Siparişin Kutusunun Bırakılması(25) / 18. Siparişin Bırakılması(20) / 13. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 3:
    if siparissayisi == 15:
        route45 = route34[::-1]
        print("Optimal Route:", route45)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum45 = konum33
        current_state = konum45
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route60 = route49[::-1]
        print("Optimal Route:", route60)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum60 = konum48
        current_state = konum60
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 25:
        route75 = route64[::-1]
        print("Optimal Route:", route75)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum75 = konum63
        current_state = konum75
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
        
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 2:
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    if siparissayisi == 15:
        route46 = route
        print("Optimal Route:", route46)
        print(current_state)
        konum46 = current_state
    if siparissayisi == 20:
        route61 = route
        print("Optimal Route:", route61)
        print(current_state)
        konum61 = current_state
    if siparissayisi == 25:
        route76 = route
        print("Optimal Route:", route76)
        print(current_state)
        konum76 = current_state
    print("------------------------------------------------------------------------")
        
#24. Siparişin Kutusunun Bırakılması(25) / 19. Siparişin Bırakılması(20) / 14. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 2:
    if siparissayisi == 15:
        route47 = route37[::-1]
        print("Optimal Route:", route47)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum47 = konum36
        current_state = konum47
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route62 = route52[::-1]
        print("Optimal Route:", route62)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum62 = konum51
        current_state = konum62
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 25:
        route77 = route67[::-1]
        print("Optimal Route:", route77)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum77 = konum66
        current_state = konum77
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
        
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 1:
    next_state = (5, 3)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    if siparissayisi == 15:
        route48 = route
        print("Optimal Route:", route48)
        print(current_state)
        konum48 = current_state
    if siparissayisi == 20:
        route63 = route
        print("Optimal Route:", route63)
        print(current_state)
        konum63 = current_state
    if siparissayisi == 25:
        route78 = route
        print("Optimal Route:", route78)
        print(current_state)
        konum78 = current_state
    print("------------------------------------------------------------------------")
        
#25. Siparişin Kutusunun Bırakılması(25) / 20. Siparişin Bırakılması(20) / 15. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 1:
    if siparissayisi == 15:
        route49 = route40[::-1]
        print("Optimal Route:", route49)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum49 = konum39
        current_state = konum49
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route64 = route55[::-1]
        print("Optimal Route:", route64)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum64 = konum54
        current_state = konum64
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 25:
        route79 = route70[::-1]
        print("Optimal Route:", route79)
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum79 = konum69
        current_state = konum79
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
        
# Şarj istasyonuna geri dönülmesi
if islemsayisi == siparissayisi*2 and capacity_values[5,3] == 0:
    next_state = (0, 0)
    fark = get_difference(current_state, next_state)
    route, current_state = hareket(current_state, fark)
    if siparissayisi == 15:    
        route50 = route
        print("Optimal Route:", route50)
        print(current_state)
        konum50 = current_state
    if siparissayisi == 20:
        route65 = route
        print("Optimal Route:", route65)
        print(current_state)
        konum65 = current_state
    if siparissayisi == 25:
        route80 = route
        print("Optimal Route:", route80)
        print(current_state)
        konum80 = current_state
    print("------------------------------------------------------------------------")
    
optimal_route = []
adım_sayısı = 0

if 'route1' in globals():
    optimal_route.extend(route1)
    adım_sayısı += len(route1) - 1
if 'route1_9' in globals():
    optimal_route.extend(route1_9)
    adım_sayısı += len(route1_9) - 1
if 'route2' in globals():
    optimal_route.extend(route2)
    adım_sayısı += len(route2) - 1
if 'route2_1' in globals():
    optimal_route.extend(route2_1)
    adım_sayısı += len(route2_1) - 1
if 'route3' in globals():
    optimal_route.extend(route3)
    adım_sayısı += len(route3) - 1
if 'route3_1' in globals():
    optimal_route.extend(route3_1)       
    adım_sayısı += len(route3_1) - 1
if 'route4' in globals():
    optimal_route.extend(route4)
    adım_sayısı += len(route4) - 1
if 'route4_9' in globals():
    optimal_route.extend(route4_9)
    adım_sayısı += len(route4_9) - 1
if 'route5' in globals():
    optimal_route.extend(route5)
    adım_sayısı += len(route5) - 1
if 'route5_9' in globals():
    optimal_route.extend(route5_9)
    adım_sayısı += len(route5_9) - 1
if 'route6' in globals():
    optimal_route.extend(route6)
    adım_sayısı += len(route6) - 1
if 'route6_9' in globals():
    optimal_route.extend(route6_9)
    adım_sayısı += len(route6_9) - 1
if 'route7' in globals():
    optimal_route.extend(route7)
    adım_sayısı += len(route7) - 1
if 'route7_9' in globals():
    optimal_route.extend(route7_9)
    adım_sayısı += len(route7_9) - 1
if 'route8' in globals():
    optimal_route.extend(route8)
    adım_sayısı += len(route8) - 1
if 'route8_9' in globals():
    optimal_route.extend(route8_9)
    adım_sayısı += len(route8_9) - 1
if 'route9' in globals():
    optimal_route.extend(route9)
    adım_sayısı += len(route9) - 1
if 'route9_9' in globals():
    optimal_route.extend(route9_9)
    adım_sayısı += len(route9_9) - 1
if 'route10' in globals():
    optimal_route.extend(route10)
    adım_sayısı += len(route10) - 1
if 'route10_8' in globals():
    optimal_route.extend(route10_8)
    adım_sayısı += len(route10_8) - 1
if 'route10_9' in globals():
    optimal_route.extend(route10_9)
    adım_sayısı += len(route10_9) - 1
if 'route11' in globals():
    optimal_route.extend(route11)
    adım_sayısı += len(route11) - 1
if 'route12' in globals():
    optimal_route.extend(route12)
    adım_sayısı += len(route12) - 1
if 'route12_9' in globals():
    optimal_route.extend(route12_9)
    adım_sayısı += len(route12_9) - 1
if 'route13' in globals():
    optimal_route.extend(route13)
    adım_sayısı += len(route13) - 1
if 'route13_8' in globals():
    optimal_route.extend(route13_8)
    adım_sayısı += len(route13_8) - 1
if 'route13_9' in globals():
    optimal_route.extend(route13_9)
    adım_sayısı += len(route13_9) - 1
if 'route14' in globals():
    optimal_route.extend(route14)
    adım_sayısı += len(route14) - 1
if 'route15' in globals():
    optimal_route.extend(route15)
    adım_sayısı += len(route15) - 1
if 'route15_9' in globals():
    optimal_route.extend(route15_9)
    adım_sayısı += len(route15_9) - 1
if 'route16' in globals():
    optimal_route.extend(route16)
    adım_sayısı += len(route16) - 1
if 'route16_8' in globals():
    optimal_route.extend(route16_8)
    adım_sayısı += len(route16_8) - 1
if 'route16_9' in globals():
    optimal_route.extend(route16_9)
    adım_sayısı += len(route16_9) - 1
if 'route17' in globals():
    optimal_route.extend(route17)
    adım_sayısı += len(route17) - 1
if 'route18' in globals():
    optimal_route.extend(route18)
    adım_sayısı += len(route18) - 1
if 'route18_9' in globals():
    optimal_route.extend(route18_9)
    adım_sayısı += len(route18_9) - 1
if 'route19' in globals():
    optimal_route.extend(route19)
    adım_sayısı += len(route19) - 1
if 'route19_8' in globals():
    optimal_route.extend(route19_8)
    adım_sayısı += len(route19_8) - 1
if 'route19_9' in globals():
    optimal_route.extend(route19_9)
    adım_sayısı += len(route19_9) - 1
if 'route20' in globals():
    optimal_route.extend(route20)
    adım_sayısı += len(route20) - 1
if 'route21' in globals():
    optimal_route.extend(route21)
    adım_sayısı += len(route21) - 1
if 'route21_9' in globals():
    optimal_route.extend(route21_9)
    adım_sayısı += len(route21_9) - 1
if 'route22' in globals():
    optimal_route.extend(route22)
    adım_sayısı += len(route22) - 1
if 'route22_8' in globals():
    optimal_route.extend(route22_8)
    adım_sayısı += len(route22_8) - 1
if 'route22_9' in globals():
    optimal_route.extend(route22_9)
    adım_sayısı += len(route22_9) - 1
if 'route23' in globals():
    optimal_route.extend(route23)
    adım_sayısı += len(route23) - 1
if 'route24' in globals():
    optimal_route.extend(route24)
    adım_sayısı += len(route24)- 1
if 'route24_9' in globals():
    optimal_route.extend(route24_9)
    adım_sayısı += len(route24_9)- 1
if 'route25' in globals():
    optimal_route.extend(route25)
    adım_sayısı += len(route25)- 1
if 'route25_8' in globals():
    optimal_route.extend(route25_8)
    adım_sayısı += len(route25_8)- 1
if 'route25_9' in globals():
    optimal_route.extend(route25_9)
    adım_sayısı += len(route25_9)- 1
if 'route26' in globals():
    optimal_route.extend(route26)
    adım_sayısı += len(route26)- 1
if 'route27' in globals():
    optimal_route.extend(route27)
    adım_sayısı += len(route27)- 1
if 'route27_9' in globals():
    optimal_route.extend(route27_9)
    adım_sayısı += len(route27_9)- 1
if 'route28' in globals():
    optimal_route.extend(route28)
    adım_sayısı += len(route28)- 1
if 'route28_8' in globals():
    optimal_route.extend(route28_8)
    adım_sayısı += len(route28_8)- 1
if 'route28_9' in globals():
    optimal_route.extend(route28_9)
    adım_sayısı += len(route28_9)- 1
if 'route29' in globals():
    optimal_route.extend(route29)
    adım_sayısı += len(route29)- 1
if 'route30' in globals():
    optimal_route.extend(route30)
    adım_sayısı += len(route30)- 1
if 'route30_9' in globals():
    optimal_route.extend(route30_9)
    adım_sayısı += len(route30_9)-1
if 'route31' in globals():
    optimal_route.extend(route31)
    adım_sayısı += len(route31)-1
if 'route31_8' in globals():
    optimal_route.extend(route31_8)
    adım_sayısı += len(route31_8)-1
if 'route31_9' in globals():
    optimal_route.extend(route31_9)
    adım_sayısı += len(route31_9)-1
if 'route32' in globals():
    optimal_route.extend(route32)
    adım_sayısı += len(route32)-1
if 'route33' in globals():
    optimal_route.extend(route33)
    adım_sayısı += len(route33)-1
if 'route33_9' in globals():
    optimal_route.extend(route33_9)
    adım_sayısı += len(route33_9)-1
if 'route34' in globals():
    optimal_route.extend(route34)
    adım_sayısı += len(route34)-1
if 'route34_8' in globals():
    optimal_route.extend(route34_8)
    adım_sayısı += len(route34_8)-1
if 'route34_9' in globals():
    optimal_route.extend(route34_9)
    adım_sayısı += len(route34_9)-1
if 'route35' in globals():
    optimal_route.extend(route35)
    adım_sayısı += len(route35)-1
if 'route36' in globals():
    optimal_route.extend(route36)
    adım_sayısı += len(route36)-1
if 'route36_9' in globals():
    adım_sayısı += len(route36_9)-1
    optimal_route.extend(route36_9)
if 'route37' in globals():
    optimal_route.extend(route37)
    adım_sayısı += len(route37)-1
if 'route37_8' in globals():
    optimal_route.extend(route37_8)
    adım_sayısı += len(route37_8)-1
if 'route37_9' in globals():
    optimal_route.extend(route37_9)
    adım_sayısı += len(route37_9)-1
if 'route38' in globals():
    optimal_route.extend(route38)
    adım_sayısı += len(route38)-1
if 'route39' in globals():
    optimal_route.extend(route39)
    adım_sayısı += len(route39)-1
if 'route39_9' in globals():
    optimal_route.extend(route39_9)
    adım_sayısı += len(route39_9)-1
if 'route40' in globals():
    optimal_route.extend(route40)
    adım_sayısı += len(route40)-1
if 'route40_8' in globals():
    optimal_route.extend(route40_8)
    adım_sayısı += len(route40_8)-1
if 'route40_9' in globals():
    optimal_route.extend(route40_9)
    adım_sayısı += len(route40_9)-1
if 'route41' in globals():
    optimal_route.extend(route41)
    adım_sayısı += len(route41)-1
if 'route42' in globals():
    optimal_route.extend(route42)
    adım_sayısı += len(route42)-1
if 'route42_9' in globals():
    optimal_route.extend(route42_9)
    adım_sayısı += len(route42_9)-1
if 'route43' in globals():
    optimal_route.extend(route43)
    adım_sayısı += len(route43)-1
if 'route43_8' in globals():
    optimal_route.extend(route43_8)
    adım_sayısı += len(route43_8)-1
if 'route43_9' in globals():
    optimal_route.extend(route43_9)
    adım_sayısı += len(route43_9)-1
if 'route44' in globals():
    optimal_route.extend(route44)
    adım_sayısı += len(route44)-1
if 'route45' in globals():
    optimal_route.extend(route45)
    adım_sayısı += len(route45)-1
if 'route45_9' in globals():
    optimal_route.extend(route45_9)
    adım_sayısı += len(route45_9)-1
if 'route46' in globals():
    optimal_route.extend(route46)
    adım_sayısı += len(route46)-1
if 'route46_8' in globals():
    optimal_route.extend(route46_8)
    adım_sayısı += len(route46_8)-1
if 'route46_9' in globals():
    optimal_route.extend(route46_9)
    adım_sayısı += len(route46_9)-1
if 'route47' in globals():
    optimal_route.extend(route47)
    adım_sayısı += len(route47)-1
if 'route48' in globals():
    optimal_route.extend(route48)
    adım_sayısı += len(route48)-1
if 'route48_9' in globals():
    optimal_route.extend(route48_9)
    adım_sayısı += len(route48_9)-1
if 'route49' in globals():
    optimal_route.extend(route49)
    adım_sayısı += len(route49)-1
if 'route49_8' in globals():
    optimal_route.extend(route49_8)
    adım_sayısı += len(route49_8)-1
if 'route49_9' in globals():
    optimal_route.extend(route49_9)
    adım_sayısı += len(route49_9)-1
if 'route50' in globals():
    optimal_route.extend(route50)
    adım_sayısı += len(route50)-1
if 'route51' in globals():
    optimal_route.extend(route51)
    adım_sayısı += len(route51)-1
if 'route51_9' in globals():
    optimal_route.extend(route51_9)
    adım_sayısı += len(route51_9)-1
if 'route52' in globals():
    optimal_route.extend(route52)
    adım_sayısı += len(route52)-1
if 'route52_8' in globals():
    optimal_route.extend(route52_8)
    adım_sayısı += len(route52_8)-1
if 'route52_9' in globals():
    optimal_route.extend(route52_9)
    adım_sayısı += len(route52_9)-1
if 'route53' in globals():
    optimal_route.extend(route53)
    adım_sayısı += len(route53)-1
if 'route54' in globals():
    optimal_route.extend(route54)
    adım_sayısı += len(route54)-1
if 'route54_9' in globals():
    optimal_route.extend(route54_9)
    adım_sayısı += len(route54_9)-1
if 'route55' in globals():
    optimal_route.extend(route55)
    adım_sayısı += len(route55)-1
if 'route55_8' in globals():
    optimal_route.extend(route55_8)
    adım_sayısı += len(route55_8)-1
if 'route55_9' in globals():
    optimal_route.extend(route55_9)
    adım_sayısı += len(route55_9)-1
if 'route56' in globals():
    optimal_route.extend(route56)
    adım_sayısı += len(route56)-1
if 'route57' in globals():
    optimal_route.extend(route57)
    adım_sayısı += len(route57)-1
if 'route57_9' in globals():
    optimal_route.extend(route57_9)
    adım_sayısı += len(route57_9)-1
if 'route58' in globals():
    optimal_route.extend(route58)
    adım_sayısı += len(route58)-1
if 'route58_8' in globals():
    optimal_route.extend(route58_8)
    adım_sayısı += len(route58_8)-1
if 'route58_9' in globals():
    optimal_route.extend(route58_9)
    adım_sayısı += len(route58_9)-1
if 'route59' in globals():
    optimal_route.extend(route59)
    adım_sayısı += len(route59)-1
if 'route60' in globals():
    optimal_route.extend(route60)
    adım_sayısı += len(route60)-1
if 'route60_9' in globals():
    optimal_route.extend(route60_9)
    adım_sayısı += len(route60_9)-1
if 'route61' in globals():
    optimal_route.extend(route61)
    adım_sayısı += len(route61)-1
if 'route61_8' in globals():
    optimal_route.extend(route61_8)
    adım_sayısı += len(route61_8)-1
if 'route61_9' in globals():
    optimal_route.extend(route61_9)
    adım_sayısı += len(route61_9)-1
if 'route62' in globals():
    optimal_route.extend(route62)
    adım_sayısı += len(route62)-1
if 'route63' in globals():
    optimal_route.extend(route63)
    adım_sayısı += len(route63)-1
if 'route63_9' in globals():
    optimal_route.extend(route63_9)
    adım_sayısı += len(route63_9)-1
if 'route64' in globals():
    optimal_route.extend(route64)
    adım_sayısı += len(route64)-1
if 'route64_8' in globals():
    optimal_route.extend(route64_8)
    adım_sayısı += len(route64_8)-1
if 'route64_9' in globals():
    optimal_route.extend(route64_9)
    adım_sayısı += len(route64_9)-1
if 'route65' in globals():
    optimal_route.extend(route65)
    adım_sayısı += len(route65)-1
if 'route66' in globals():
    optimal_route.extend(route66)
    adım_sayısı += len(route66)-1
if 'route66_9' in globals():
    optimal_route.extend(route66_9)
    adım_sayısı += len(route66_9)-1
if 'route67' in globals():
    optimal_route.extend(route67)
    adım_sayısı += len(route67)-1
if 'route67_8' in globals():
    optimal_route.extend(route67_8)
    adım_sayısı += len(route67_8)-1
if 'route67_9' in globals():
    optimal_route.extend(route67_9)
    adım_sayısı += len(route67_9)-1
if 'route68' in globals():
    optimal_route.extend(route68)
    adım_sayısı += len(route68)-1
if 'route69' in globals():
    optimal_route.extend(route69)
    adım_sayısı += len(route69)-1
if 'route69_9' in globals():
    optimal_route.extend(route69_9)
    adım_sayısı += len(route69_9)-1
if 'route70' in globals():
    optimal_route.extend(route70)
    adım_sayısı += len(route70)-1
if 'route70_8' in globals():
    optimal_route.extend(route70_8)
    adım_sayısı += len(route70_8)-1
if 'route70_9' in globals():
    optimal_route.extend(route70_9)
    adım_sayısı += len(route70_9)-1
if 'route71' in globals():
    optimal_route.extend(route71)
    adım_sayısı += len(route71)-1
if 'route72' in globals():
    optimal_route.extend(route72)
    adım_sayısı += len(route72)-1
if 'route73' in globals():
    optimal_route.extend(route73)
    adım_sayısı += len(route73) - 1
if 'route74' in globals():
    optimal_route.extend(route74)
    adım_sayısı += len(route74) - 1
if 'route75' in globals():
    optimal_route.extend(route75)
    adım_sayısı += len(route75) - 1
if 'route76' in globals():
    optimal_route.extend(route76)
    adım_sayısı += len(route76) - 1
if 'route77' in globals():
    optimal_route.extend(route77)
    adım_sayısı += len(route77) - 1
if 'route78' in globals():
    optimal_route.extend(route78)
    adım_sayısı += len(route78) - 1
if 'route79' in globals():
    optimal_route.extend(route79)
    adım_sayısı += len(route79) - 1
if 'route80' in globals():
    optimal_route.extend(route80)
    adım_sayısı += len(route80) - 1

print("Optimum Route:", optimal_route)
print("Adım Sayısı", adım_sayısı)