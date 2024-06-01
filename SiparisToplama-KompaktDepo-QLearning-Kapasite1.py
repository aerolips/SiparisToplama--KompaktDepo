import numpy as np
import pandas as pd

environment_rows = 6
environment_columns = 6

alpha = 0.8
gamma = 0.9
epsilon = 1
epsilon_decay = 0.000001
num_episodes = 10000

actions = ['up', 'right', 'down', 'left']
q_values = np.zeros((environment_rows, environment_columns, 4))

rewards = np.full((environment_rows, environment_columns), -1)
rewards_control = np.full((environment_rows, environment_columns), 0)
rewards_kat1 = np.full((environment_rows, environment_columns), 0)
rewards_kat2 = np.full((environment_rows, environment_columns), 0)
rewards_kat3 = np.full((environment_rows, environment_columns), 0)
rewards_kat4 = np.full((environment_rows, environment_columns), 0)
rewards_kat5 = np.full((environment_rows, environment_columns), 0)
rewards[1, 0] = -1000
rewards[2, 0] = -1000
rewards[3, 0] = -1000
rewards[4, 0] = -1000
rewards[5, 0] = -1000
rewards[5, 1] = -1000
rewards[5, 2] = -1000
rewards[5, 4] = -1000
rewards[5, 5] = -1000

csv_data = pd.read_csv("C:/Users/Ali Gündüz/Desktop/25siparis12.csv")
siparissayisi25 = 1
siparissayisi = 25

for index, row in csv_data.iterrows():
    satir = int(row['satir'])
    sutun = int(row['sutun'])
    urunsayisi = int(row['urunsayisi'])
    rewards_kat1[satir,sutun] = int(row['rewards_kat1'])
    rewards_kat2[satir,sutun] = int(row['rewards_kat2'])
    rewards_kat3[satir,sutun] = int(row['rewards_kat3'])
    rewards_kat4[satir,sutun] = int(row['rewards_kat4'])
    rewards_kat5[satir,sutun] = int(row['rewards_kat5'])
    rewards_control[satir, sutun] = urunsayisi
    
for i in range(environment_rows):
    for j in range(environment_columns):
        if rewards_control[i, j] > 0:
            rewards[i, j] = 50

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

capacity_values[0,0] = -1000
            
for i in range(6):
    for j in range(6):
        if rewards[i][j] == -1000:
            capacity_values[i][j] = -1000
            
def get_starting_location():
    current_row_index = 0
    current_column_index = 0
    return current_row_index, current_column_index

def get_next_action(current_row_index, current_column_index, epsilon):
    if current_row_index == 5 and current_column_index == 3:
        return 0
    if current_row_index == 0 and current_column_index == 0:
        return 1
    if np.random.random() < epsilon:
        return np.random.randint(4)
    else:
        return np.argmax(q_values[current_row_index, current_column_index])
    
def get_next_location(current_row_index, current_column_index, action_index):
    new_row_index = current_row_index
    new_column_index = current_column_index
  
    if actions[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif actions[action_index] == 'right' and current_column_index < environment_columns - 1:
        new_column_index += 1
    elif actions[action_index] == 'down' and current_row_index < environment_rows - 1:
        new_row_index += 1
    elif actions[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1
             
    return new_row_index, new_column_index

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
                             
    elif rewards_kat2[current_state[0], current_state[1]] == 0 and rewards_kat3[current_state[0], current_state[1]] == 0 and rewards_kat4[current_state[0], current_state[1]] == 0 and rewards_kat5[current_state[0], current_state[1]] == 5:
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
 
def q_learning(current_state, rewards, immediate_reward):
    epsilon = 1
    for episode in range(num_episodes):        
        is_terminal = False
        while not is_terminal:
            action = get_next_action(current_state[0], current_state[1], epsilon)
            next_state = get_next_location(current_state[0], current_state[1], action)
            reward = rewards[next_state[0], next_state[1]]
            max_next_action = np.argmax(q_values[next_state[0], next_state[1]])
            q_values[current_state[0], current_state[1], action] = q_values[current_state[0], current_state[1], action] + alpha * (reward + gamma * q_values[next_state[0], next_state[1], max_next_action] - q_values[current_state[0], current_state[1], action])
            current_state = next_state
            if reward == immediate_reward or rewards[current_state[0], current_state[1]] == -1000:
                is_terminal = True
            
            if epsilon > 0.1:
                epsilon -= epsilon_decay
        
    return q_values

def follow_optimal_policy(current_state, rewards, immediate_reward):
    total_reward = np.float64(0)
    route = [current_state]
    while True:
        action = get_next_action(current_state[0], current_state[1], 0.0001)
        next_state = get_next_location(current_state[0], current_state[1], action)
        reward = rewards[next_state[0], next_state[1]]
        total_reward += reward
        current_state = next_state
        route.append(current_state)
        
        if reward >= immediate_reward or rewards[current_state[0], current_state[1]] == -1000:            
            break
    return total_reward, route, current_state
    
current_state = get_starting_location()
islemsayisi = 0
toplanansiparis = 0
kat = 0
# 1. Siparişin Konumuna Gidilmesi
if current_state[0] == 0 and current_state[1] == 0:
    immediate_reward = 50
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state, rewards, immediate_reward)
    route1 = route
    print("Optimal Route:", route1)
    print("Total Reward:", total_reward)
    print(current_state)
    konum1 = current_state
    print(rewards[current_state[0], current_state[1]])
    visited_50_reward = True
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
# 1. Siparişin İstasyona Teslim Edilmesi             
if rewards[current_state[0], current_state[1]] == 50 and visited_50_reward == True:
    if rewards_kat1[current_state[0], current_state[1]] == 0:
        if rewards_kat2[current_state[0], current_state[1]] == 2 or rewards_kat3[current_state[0], current_state[1]] == 3 or rewards_kat4[current_state[0], current_state[1]] == 4 or rewards_kat5[current_state[0], current_state[1]] == 5:
            kat = 1
            kutuhareket = kutu(current_state)
            route1_9 = kutuhareket
            print("Optimal Route:", route1_9)
    
    visited_50_reward = False
    if rewards_control[current_state[0], current_state[1]] == 1:
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] == 50:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route2 = route  
    print("Optimal Route:", route2)
    print("Total Reward:", total_reward)
    print(current_state)
    konum2 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])  
    print("------------------------------------------------------------------------")
# 2. Siparişin Konumuna Gidilmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 1:
    if kat == 1:
        if kutuyok == 0:
            rewards[current_state[0], current_state[1]] = -1
            route2_1 = route2[::-1] + route1_9[::-1]
            current_state = konum1
            kat = -1
            print("Optimal Route:", route2_1)
            
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 60
                                                   
            immediate_reward = 60
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route3 = route
            print("Optimal Route:", route3)
            print("Total Reward:", total_reward)
            print(current_state)
            konum3 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------") 
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            rewards[current_state[0], current_state[1]] = -1    
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 60
                                                   
            immediate_reward = 60
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route3 = route
            print("Optimal Route:", route3)
            print("Total Reward:", total_reward)
            print(current_state)
            konum3 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")       
    elif kat == 0:
        rewards[current_state[0], current_state[1]] = -1    
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 60
                                               
        immediate_reward = 60
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route3 = route
        print("Optimal Route:", route3)
        print("Total Reward:", total_reward)
        print(current_state)
        konum3 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#2. Siparişin İstasyona Götürülmesi
if rewards[current_state[0], current_state[1]] >= 60 and toplanansiparis == 2:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 60:
                rewards[a][b] = -2
                
    immediate_reward = 1000
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route4 = route
    print("Optimal Route:", route4)
    print("Total Reward:", total_reward)
    print(current_state)
    konum4 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#2. Siparişin Kutusunun Düzeltilmesi ve 3. Siparişe Gitmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 2 and islemsayisi == 2:
    if kat == 1:
        if kutuyok == 0:
            rewards[current_state[0], current_state[1]] = -1
            route4_9 = route4[::-1] + route3_1[::-1]
            current_state = konum3
            kat = -1
            print("Optimal Route:", route4_9)
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 70
            immediate_reward = 70
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route5 = route
            print("Optimal Route:", route5)
            print("Total Reward:", total_reward)
            print(current_state)
            konum5 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
           kutuyok = 0
           kat = -1
           rewards[current_state[0], current_state[1]] = -1
           for a in range(6):
                   if rewards_control[4, a] > 0:
                           rewards[4][a] = 450                   
           for b in range(6):
                   if rewards_control[3, b] > 0:
                           rewards[3][b] = 400
           for c in range(6):
                   if rewards_control[2, c] > 0:
                           rewards[2][c] = 350
           for d in range(6):
                   if rewards_control[1, d] > 0:
                           rewards[1][d] = 300
           for e in range(6):
                   if rewards_control[0, e] > 0:
                           rewards[0][e] = 70
           immediate_reward = 70
           current_state = [current_state[0], current_state[1]]
           q_values = q_learning(current_state, rewards, immediate_reward)
           total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
           route5 = route
           print("Optimal Route:", route5)
           print("Total Reward:", total_reward)
           print(current_state)
           konum5 = current_state
           print(rewards[current_state[0], current_state[1]])   
           toplanansiparis += 1
           print("------------------------------------------------------------------------")   
    else:
        rewards[current_state[0], current_state[1]] = -1
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 70
        immediate_reward = 70
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route5 = route
        print("Optimal Route:", route5)
        print("Total Reward:", total_reward)
        print(current_state)
        konum5 = current_state
        print(rewards[current_state[0], current_state[1]])   
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#3. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 70 and toplanansiparis == 3:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 70:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route6 = route  
    print("Optimal Route:", route6)
    print("Total Reward:", total_reward)
    print(current_state)
    konum6 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#3. Siparişin Kutusunun Düzeltilmesi Gerekiyorsa Düzeltilmesi ve 4. Siparişe Gidilmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 3 and islemsayisi == 3:
    if kat == 1:
        if kutuyok == 0:
            rewards[current_state[0], current_state[1]] = -1
            route6_9 = route6[::-1] + route5_9[::-1]
            current_state = konum5
            kat = -1
            print("Optimal Route:", route6_9)
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 80
            immediate_reward = 80
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route7 = route
            print("Optimal Route:", route7)
            print("Total Reward:", total_reward)
            print(current_state)
            konum7 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            rewards[current_state[0], current_state[1]] = -1
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 80
            immediate_reward = 80
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route7 = route
            print("Optimal Route:", route7)
            print("Total Reward:", total_reward)
            print(current_state)
            konum7 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
    else:
        rewards[current_state[0], current_state[1]] = -1
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 80
        immediate_reward = 80
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route7 = route
        print("Optimal Route:", route7)
        print("Total Reward:", total_reward)
        print(current_state)
        konum7 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#4. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 80 and toplanansiparis == 4:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 80:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route8 = route  
    print("Optimal Route:", route8)
    print("Total Reward:", total_reward)
    print(current_state)
    konum8 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#4. Siparişin Kutusunun Düzeltilmesi Gerekiyorsa Düzeltilmesi ve 5. Siparişe Gidilmesi
if current_state[0] == 5 and current_state[1] == 3 and capacity_values[5,3] == 4 and islemsayisi == 4:
    if kat == 1:
        if kutuyok == 0:
            rewards[current_state[0], current_state[1]] = -1
            route8_9 = route8[::-1] + route7_9[::-1]
            current_state = konum7
            kat = -1
            print("Optimal Route:", route8_9)
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 90
            immediate_reward = 90
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route9 = route
            print("Optimal Route:", route9)
            print("Total Reward:", total_reward)
            print(current_state)
            konum9 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            kat = -1
            rewards[current_state[0], current_state[1]] = -1
            for a in range(6):
                    if rewards_control[4, a] > 0:
                            rewards[4][a] = 450                   
            for b in range(6):
                    if rewards_control[3, b] > 0:
                            rewards[3][b] = 400
            for c in range(6):
                    if rewards_control[2, c] > 0:
                            rewards[2][c] = 350
            for d in range(6):
                    if rewards_control[1, d] > 0:
                            rewards[1][d] = 300
            for e in range(6):
                    if rewards_control[0, e] > 0:
                            rewards[0][e] = 90
            immediate_reward = 90
            current_state = [current_state[0], current_state[1]]
            q_values = q_learning(current_state, rewards, immediate_reward)
            total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
            route9 = route
            print("Optimal Route:", route9)
            print("Total Reward:", total_reward)
            print(current_state)      
            konum9 = current_state
            print(rewards[current_state[0], current_state[1]])
            toplanansiparis += 1
            print("------------------------------------------------------------------------")        
    else:
        rewards[current_state[0], current_state[1]] = -1
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 90
        immediate_reward = 90
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route9 = route
        print("Optimal Route:", route9)
        print("Total Reward:", total_reward)
        print(current_state)      
        konum9 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
#5. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 90 and toplanansiparis == 5:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 90:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route10 = route
    print("Optimal Route:", route10)
    print("Total Reward:", total_reward)
    print(current_state)
    konum10 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#1. Siparişin Kutusunu Yerine Bırakma
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 5 and capacity_values[5, 3] == 5:
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum11 = konum1
            current_state = konum11
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
        if kutuyok == 1:
            kutuyok = 0
            route11 = route2[::-1]
            kat = -1
            print("Optimal Route:", route11)
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum11 = konum1
        current_state = konum11
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#6. Siparişe Gidilmesi
if islemsayisi == 6:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 100
    immediate_reward = 100
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route12 = route
    print("Optimal Route:", route12)
    print("Total Reward:", total_reward)
    print(current_state)
    konum12 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#6. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 100 and toplanansiparis == 6:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 100:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route13 = route
    print("Optimal Route:", route13)
    print("Total Reward:", total_reward)
    print(current_state)
    konum13 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum14 = konum3
        current_state = konum14
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#7. Siparişe Gidilmesi
if islemsayisi == 8:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 110
    immediate_reward = 110
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route15 = route
    print("Optimal Route:", route15)
    print("Total Reward:", total_reward)
    print(current_state)
    konum15 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#7. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 110 and toplanansiparis == 7:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 110:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route16 = route
    print("Optimal Route:", route16)
    print("Total Reward:", total_reward)
    print(current_state)
    konum16 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#7. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 3. Siparişin Kutusunun Yerine Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum17 = konum5
        current_state = konum17
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#8. Siparişe Gidilmesi
if islemsayisi == 10:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 120
    immediate_reward = 120
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route18 = route
    print("Optimal Route:", route18)
    print("Total Reward:", total_reward)
    print(current_state)
    konum18 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#8. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 120 and toplanansiparis == 8:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 120:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route19 = route
    print("Optimal Route:", route19)
    print("Total Reward:", total_reward)
    print(current_state)
    konum19 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#8. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 4. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum20 = konum7
        current_state = konum20
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#9. Siparişe Gidilmesi
if islemsayisi == 12:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 130
    immediate_reward = 130
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route21 = route
    print("Optimal Route:", route21)
    print("Total Reward:", total_reward)
    print(current_state)
    konum21 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#9. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 130 and toplanansiparis == 9:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 130:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route22 = route
    print("Optimal Route:", route22)
    print("Total Reward:", total_reward)
    print(current_state)
    konum22 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#9. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 5. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum23 = konum9
        current_state = konum23
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#10. Siparişe Gidilmesi
if islemsayisi == 14:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 140
    immediate_reward = 140
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route24 = route
    print("Optimal Route:", route24)
    print("Total Reward:", total_reward)
    print(current_state)
    konum24 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#10. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 140 and toplanansiparis == 10:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 140:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route25 = route
    print("Optimal Route:", route25)
    print("Total Reward:", total_reward)
    print(current_state)
    konum25 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#10. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 6. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum26 = konum12
        current_state = konum26
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#11. Siparişe Gidilmesi
if islemsayisi == 16:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 150
    immediate_reward = 150
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route27 = route
    print("Optimal Route:", route27)
    print("Total Reward:", total_reward)
    print(current_state)
    konum27 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#11. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 150 and toplanansiparis == 11:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 150:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route28 = route
    print("Optimal Route:", route28)
    print("Total Reward:", total_reward)
    print(current_state)
    konum28 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#11. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 7. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum29 = konum15
        current_state = konum29
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#12. Siparişe Gidilmesi
if islemsayisi == 18:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 160
    immediate_reward = 160
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route30 = route
    print("Optimal Route:", route30)
    print("Total Reward:", total_reward)
    print(current_state)
    konum30 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#12. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 160 and toplanansiparis == 12:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 160:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route31 = route
    print("Optimal Route:", route31)
    print("Total Reward:", total_reward)
    print(current_state)
    konum31 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#12. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 8. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum32 = konum18
        current_state = konum32
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#13. Siparişe Gidilmesi
if islemsayisi == 20:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 170
    immediate_reward = 170
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route33 = route
    print("Optimal Route:", route33)
    print("Total Reward:", total_reward)
    print(current_state)
    konum33 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#13. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 170 and toplanansiparis == 13:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 170:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route34 = route
    print("Optimal Route:", route34)
    print("Total Reward:", total_reward)
    print(current_state)
    konum34 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#13. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 9. Siparişin Kutusunun Bırakılması
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
           rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum35 = konum21
        current_state = konum35
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#14. Siparişe Gidilmesi
if islemsayisi == 22:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 180
    immediate_reward = 180
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route36 = route
    print("Optimal Route:", route36)
    print("Total Reward:", total_reward)
    print(current_state)
    konum36 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#14. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 180 and toplanansiparis == 14:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 180:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route37 = route
    print("Optimal Route:", route37)
    print("Total Reward:", total_reward)
    print(current_state)
    konum37 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#14. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 10. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum38 = konum24
        current_state = konum38
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
        print("------------------------------------------------------------------------")
#15. Siparişin İstasyona Bırakılması
if islemsayisi == 24:
    for a in range(6):
            if rewards_control[4, a] > 0:
                    rewards[4][a] = 450                   
    for b in range(6):
            if rewards_control[3, b] > 0:
                    rewards[3][b] = 400
    for c in range(6):
            if rewards_control[2, c] > 0:
                    rewards[2][c] = 350
    for d in range(6):
            if rewards_control[1, d] > 0:
                    rewards[1][d] = 300
    for e in range(6):
            if rewards_control[0, e] > 0:
                    rewards[0][e] = 190
    immediate_reward = 190
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    route39 = route
    print("Optimal Route:", route39)
    print("Total Reward:", total_reward)
    print(current_state)
    konum39 = current_state
    print(rewards[current_state[0], current_state[1]])
    toplanansiparis += 1
    print("------------------------------------------------------------------------")
#15. Siparişin İstasyona Bırakılması
if rewards[current_state[0], current_state[1]] >= 190 and toplanansiparis == 15:
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
        rewards[current_state[0], current_state[1]] = -1
        rewards_control[current_state[0], current_state[1]] = 0
        rewards_kat1[current_state[0], current_state[1]] = 0
        rewards_kat2[current_state[0], current_state[1]] = 0
        rewards_kat3[current_state[0], current_state[1]] = 0
        rewards_kat4[current_state[0], current_state[1]] = 0
        rewards_kat5[current_state[0], current_state[1]] = 0
    elif rewards_control[current_state[0], current_state[1]] > 1:
        rewards[current_state[0], current_state[1]] = -2
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
            
    for a in range(6):
        for b in range(6):
            if rewards[a][b] >= 190:
                rewards[a][b] = -2
    capacity_values[current_state[0], current_state[1]] -= 1
    rewards[5, 3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
    route40 = route
    print("Optimal Route:", route40)
    print("Total Reward:", total_reward)
    print(current_state)
    konum40 = current_state
    if current_state[0] == 5 and current_state[1] == 3:
        capacity_values[5,3] += 1
        islemsayisi += 1
    print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
#15. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 11. Siparişin Kutusunun Bırakılması
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
            rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        rewards[current_state[0], current_state[1]] = -1
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
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 200
        immediate_reward = 200
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route42 = route
        print("Optimal Route:", route42)
        print("Total Reward:", total_reward)
        print(current_state)
        konum42 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #16. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 200 and toplanansiparis == 16:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 200:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route43 = route
        print("Optimal Route:", route43)
        print("Total Reward:", total_reward)
        print(current_state)
        konum43 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
        print("------------------------------------------------------------------------")
    #16. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 12. Siparişin Kutusunun Bırakılması
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum44 = konum30
            current_state = konum44
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #17. Siparişe Gidilmesi
    if islemsayisi == 28:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 210
        immediate_reward = 210
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route45 = route
        print("Optimal Route:", route45)
        print("Total Reward:", total_reward)
        print(current_state)
        konum45 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #17. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 210 and toplanansiparis == 17:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 210:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route46 = route
        print("Optimal Route:", route46)
        print("Total Reward:", total_reward)
        print(current_state)
        konum46 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
        print("------------------------------------------------------------------------")
    #17. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 13. Siparişin Kutusunun Bırakılması
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum47 = konum33
            current_state = konum47
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #18. Siparişe Gidilmesi
    if islemsayisi == 30:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 220
        immediate_reward = 220
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route48 = route
        print("Optimal Route:", route48)
        print("Total Reward:", total_reward)
        print(current_state)
        konum48 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #18. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 220 and toplanansiparis == 18:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 220:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route49 = route
        print("Optimal Route:", route49)
        print("Total Reward:", total_reward)
        print(current_state)
        konum49 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum50 = konum36
            current_state = konum50
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #19. Siparişe Gidilmesi
    if islemsayisi == 32:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 230
        immediate_reward = 230
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route51 = route
        print("Optimal Route:", route51)
        print("Total Reward:", total_reward)
        print(current_state)
        konum51 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #19. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 230 and toplanansiparis == 19:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 230:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route52 = route
        print("Optimal Route:", route52)
        print("Total Reward:", total_reward)
        print(current_state)
        konum52 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum53 = konum39
            current_state = konum53
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #20. Siparişe Gidilmesi
    if islemsayisi == 34:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 240
        immediate_reward = 240
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route54 = route
        print("Optimal Route:", route54)
        print("Total Reward:", total_reward)
        print(current_state)
        konum54 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #20. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 240 and toplanansiparis == 20:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 240:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route55 = route
        print("Optimal Route:", route55)
        print("Total Reward:", total_reward)
        print(current_state)
        konum55 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
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
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 250
        immediate_reward = 250
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route57 = route
        print("Optimal Route:", route57)
        print("Total Reward:", total_reward)
        print(current_state)
        konum57 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #21. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 250 and toplanansiparis == 21:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 250:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route58 = route
        print("Optimal Route:", route58)
        print("Total Reward:", total_reward)
        print(current_state)
        konum58 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum59 = konum45
            current_state = konum59
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #22. Siparişe Gidilmesi
    if islemsayisi == 38:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 260
        immediate_reward = 260
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route60 = route
        print("Optimal Route:", route60)
        print("Total Reward:", total_reward)
        print(current_state)
        konum60 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #22. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 260 and toplanansiparis == 22:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 260:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route61 = route
        print("Optimal Route:", route61)
        print("Total Reward:", total_reward)
        print(current_state)
        konum61 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
        print("------------------------------------------------------------------------")
    #22. Siparişin Kutusunun Düzeltilmesi, İstasyona Dönülmesi, 18. Siparişin Kutusunun Bırakılması
    if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == 39 and capacity_values[5, 3] == 5 and siparissayisi == 25:
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum62 = konum48
            current_state = konum62
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #23. Siparişe Gidilmesi
    if islemsayisi == 40:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 270
        immediate_reward = 270
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route63 = route
        print("Optimal Route:", route63)
        print("Total Reward:", total_reward)
        print(current_state)
        konum63 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #23. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 270 and toplanansiparis == 23:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 270:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route64 = route
        print("Optimal Route:", route64)
        print("Total Reward:", total_reward)
        print(current_state)
        konum64 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum65 = konum51
            current_state = konum65
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #24. Siparişe Gidilmesi
    if islemsayisi == 42:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 280
        immediate_reward = 280
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route66 = route
        print("Optimal Route:", route66)
        print("Total Reward:", total_reward)
        print(current_state)
        konum66 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #24. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 280 and toplanansiparis == 24:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 280:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route67 = route
        print("Optimal Route:", route67)
        print("Total Reward:", total_reward)
        print(current_state)
        konum67 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum68 = konum54
            current_state = konum68
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    #25. Siparişe Gidilmesi
    if islemsayisi == 44:
        for a in range(6):
                if rewards_control[4, a] > 0:
                        rewards[4][a] = 450                   
        for b in range(6):
                if rewards_control[3, b] > 0:
                        rewards[3][b] = 400
        for c in range(6):
                if rewards_control[2, c] > 0:
                        rewards[2][c] = 350
        for d in range(6):
                if rewards_control[1, d] > 0:
                        rewards[1][d] = 300
        for e in range(6):
                if rewards_control[0, e] > 0:
                        rewards[0][e] = 290
        immediate_reward = 290
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
        route69 = route
        print("Optimal Route:", route69)
        print("Total Reward:", total_reward)
        print(current_state)
        konum69 = current_state
        print(rewards[current_state[0], current_state[1]])
        toplanansiparis += 1
        print("------------------------------------------------------------------------")
    #25. Siparişin İstasyona Bırakılması
    if rewards[current_state[0], current_state[1]] >= 290 and toplanansiparis == 25:
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
            rewards[current_state[0], current_state[1]] = -1
            rewards_control[current_state[0], current_state[1]] = 0
            rewards_kat1[current_state[0], current_state[1]] = 0
            rewards_kat2[current_state[0], current_state[1]] = 0
            rewards_kat3[current_state[0], current_state[1]] = 0
            rewards_kat4[current_state[0], current_state[1]] = 0
            rewards_kat5[current_state[0], current_state[1]] = 0
        elif rewards_control[current_state[0], current_state[1]] > 1:
            rewards[current_state[0], current_state[1]] = -2
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
                
        for a in range(6):
            for b in range(6):
                if rewards[a][b] >= 290:
                    rewards[a][b] = -2
        capacity_values[current_state[0], current_state[1]] -= 1
        rewards[5, 3] = 1000
        immediate_reward = 1000
        current_state = [current_state[0], current_state[1]]
        q_values = q_learning(current_state, rewards, immediate_reward)
        total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)    
        route70 = route
        print("Optimal Route:", route70)
        print("Total Reward:", total_reward)
        print(current_state)
        konum70 = current_state
        if current_state[0] == 5 and current_state[1] == 3:
            capacity_values[5,3] += 1
            islemsayisi += 1
        print(rewards[current_state[0], current_state[1]])
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
                rewards[current_state[0], current_state[1]] = -1
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
                rewards[current_state[0], current_state[1]] = -1
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
            rewards[current_state[0], current_state[1]] = -1
            capacity_values[5, 3] -= 1
            islemsayisi += 1
            konum71 = konum57
            current_state = konum71
            capacity_values[current_state[0], current_state[1]] += 1
            print(current_state)
            print("------------------------------------------------------------------------")
    
if islemsayisi == (siparissayisi*2) - 4:
    rewards[5,3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward) 
    if siparissayisi == 25:
        route72 = route
        print("Optimal Route:", route72)
        print("Total Reward:", total_reward)
        print(current_state)
        konum72 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 20: 
        route57 = route
        print("Optimal Route:", route57)
        print("Total Reward:", total_reward)
        print(current_state)
        konum57 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 15:
        route42 = route
        print("Optimal Route:", route42)
        print("Total Reward:", total_reward)
        print(current_state)
        konum42 = current_state
        print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
        
#22. Siparişin Kutusunun Bırakılması(25) / 17. Siparişin Bırakılması(20) / 12. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 4:
    if siparissayisi == 25:
        route73 = route61[::-1]
        print("Optimal Route:", route73)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum73 = konum60
        current_state = konum73
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route58 = route46[::-1]
        print("Optimal Route:", route58)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum58 = konum45
        current_state = konum58
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 15:
        route43 = route31[::-1]
        print("Optimal Route:", route43)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum43 = konum30
        current_state = konum43
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
           
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 3:
    rewards[5,3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    if siparissayisi == 25:
        route74 = route
        print("Optimal Route:", route74)
        print("Total Reward:", total_reward)
        print(current_state)
        konum74 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 20:
        route59 = route
        print("Optimal Route:", route59)
        print("Total Reward:", total_reward)
        print(current_state)
        konum59 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 15:
        route44 = route
        print("Optimal Route:", route44)
        print("Total Reward:", total_reward)
        print(current_state)
        konum44 = current_state
        print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
    
#23. Siparişin Kutusunun Bırakılması(25) / 18. Siparişin Bırakılması(20) / 13. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 3:
    if siparissayisi == 25:
        route75 = route64[::-1]
        print("Optimal Route:", route75)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum75 = konum63
        current_state = konum75
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route60 = route49[::-1]
        print("Optimal Route:", route60)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum60 = konum48
        current_state = konum60
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 15:
        route45 = route34[::-1]
        print("Optimal Route:", route45)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum45 = konum33
        current_state = konum45
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
        
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 2:
    rewards[5,3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)  
    if siparissayisi == 25:
        route76 = route
        print("Optimal Route:", route76)
        print("Total Reward:", total_reward)
        print(current_state)
        konum76 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 20:
        route61 = route
        print("Optimal Route:", route61)
        print("Total Reward:", total_reward)
        print(current_state)
        konum61 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 15:
        route46 = route
        print("Optimal Route:", route46)
        print("Total Reward:", total_reward)
        print(current_state)
        konum46 = current_state
        print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
    
#24. Siparişin Kutusunun Bırakılması(25) / 19. Siparişin Bırakılması(20) / 14. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 2:
    if siparissayisi == 25:
        route77 = route67[::-1]
        print("Optimal Route:", route77)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum77 = konum66
        current_state = konum77
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route62 = route52[::-1]
        print("Optimal Route:", route62)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum62 = konum51
        current_state = konum62
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 15:
        route47 = route37[::-1]
        print("Optimal Route:", route47)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum47 = konum36
        current_state = konum47
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
    
#Sıradaki kutuyu almak için istasyona dönülmesi
if islemsayisi == (siparissayisi*2) - 1:
    rewards[5,3] = 1000
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)   
    if siparissayisi == 25:
        route78 = route
        print("Optimal Route:", route78)
        print("Total Reward:", total_reward)
        print(current_state)
        konum78 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 20:
        route63 = route
        print("Optimal Route:", route63)
        print("Total Reward:", total_reward)
        print(current_state)
        konum63 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 15:
        route48 = route
        print("Optimal Route:", route48)
        print("Total Reward:", total_reward)
        print(current_state)
        konum48 = current_state
        print(rewards[current_state[0], current_state[1]])
    print("------------------------------------------------------------------------")
    
#25. Siparişin Kutusunun Bırakılması(25) / 20. Siparişin Bırakılması(20) / 15. Siparişin Bırakılması(15)
if current_state[0] == 5 and current_state[1] == 3 and islemsayisi == (siparissayisi*2) - 1:
    if siparissayisi == 25:
        route79 = route70[::-1]
        print("Optimal Route:", route79)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum79 = konum69
        current_state = konum79
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 20:
        route64 = route55[::-1]
        print("Optimal Route:", route64)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum64 = konum54
        current_state = konum64
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    if siparissayisi == 15:
        route49 = route40[::-1]
        print("Optimal Route:", route49)
        rewards[current_state[0], current_state[1]] = -1
        capacity_values[5, 3] -= 1
        islemsayisi += 1
        konum49 = konum39
        current_state = konum49
        capacity_values[current_state[0], current_state[1]] += 1
        print(current_state)
    print("------------------------------------------------------------------------")
    
# Şarj istasyonuna geri dönülmesi
if islemsayisi == siparissayisi*2 and capacity_values[5,3] == 0:
    rewards[0,0] = 1000
    rewards[5,3] = -1
    immediate_reward = 1000
    current_state = [current_state[0], current_state[1]]
    q_values = q_learning(current_state, rewards, immediate_reward)
    total_reward, route, current_state = follow_optimal_policy(current_state,rewards, immediate_reward)
    if siparissayisi == 25:
        route80 = route
        print("Optimal Route:", route80)
        print("Total Reward:", total_reward)
        print(current_state)
        konum80 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 20:
        route65 = route
        print("Optimal Route:", route65)
        print("Total Reward:", total_reward)
        print(current_state)
        konum65 = current_state
        print(rewards[current_state[0], current_state[1]])
    if siparissayisi == 15:
        route50 = route
        print("Optimal Route:", route50)
        print("Total Reward:", total_reward)
        print(current_state)
        konum50 = current_state
        print(rewards[current_state[0], current_state[1]])
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