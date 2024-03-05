# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:33:07 2023

@author: Souren Prakash
"""

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
bee_fi = r"C:\Users\Souren Prakash\OneDrive\Desktop\Bee Project\save_the_bees.csv"
gdp_fi = r"C:\Users\Souren Prakash\OneDrive\Desktop\Bee Project\USA GDP Growth 1961-2021.xlsx"


#first we will create a data array 
bee_data = pd.read_csv(bee_fi)

gdp_data = pd.read_excel(gdp_fi)

#selected_state = 'California'



def colony_amount_over_years(bee_data, selected_state, selected_quarter):
    
    # In case the state is not found in the data set or if a invalid name was 
    #input
    if selected_state not in bee_data['state'].unique():
        print("state not found")
        return
    else:
    #seperating data based on state
        bee_data = bee_data.loc[bee_data['state']== selected_state]
    
    #seperating data based on quarter, only looking at the fourth quarter for 
    # the year 
        bee_data = bee_data.loc[bee_data['quarter']== selected_quarter]
    
        print(bee_data)
    #making the line graphs, setting year as the x and colony number for y
        x = bee_data['year']
        y = bee_data['num_colonies']
    
        plt.plot( x, y, color = 'red')
        
        
        plt.xlabel('Years')
        plt.ylabel(f'Number of Colonies in {selected_state}')
        plt.show()
        
        """
        Objective of this function is create dataset that will be plotted to
        find the amount of colonies overtime for a specfic state
        """

    
    
    
def larger_trend_col_amount(bee_data, selected_state):
    

    print(bee_data['state'])
    if selected_state not in bee_data['state'].unique():
        print("state not found")
        return
    else:
    #seperating data based on state
        bee_data_state = bee_data.loc[bee_data['state']== selected_state]
        
        ax = plt.subplot()
        
        for year in bee_data_state['year'].unique():
            year_data = bee_data_state.loc[bee_data_state['year'] == year]
            ax.plot(year_data['quarter'], year_data['num_colonies'], label =f'{year}')
            
        ax.set_xlabel("Quarters")
        ax.set_ylabel("Number of Colonies")
        ax.set_title(f'Number of Colonies Each Quarter in {selected_state}')
        
        plt.legend(bee_data_state['year'].unique())         
        plt.show()
        
        
    

        

    


"""def loss_of_population_line_graph(bee_data):
    
    print(bee_data['state'])
    if selected_state not in bee_data['state'].unique():
        print("state not found")
        return
    else:
    #seperating data based on state
        bee_data_state = bee_data.loc[bee_data['state']== selected_state]
        
        ax = plt.subplot()
        
        for year in bee_data_state['year'].unique():
            year_data = bee_data_state.loc[bee_data_state['year'] == year]
            ax.plot(year_data['quarter'], year_data['num_colonies'], label =f'{year}')
            
        ax.set_xlabel("Quarters")
        ax.set_ylabel("Number of Colonies")
        ax.set_title(f'Number of Colonies Each Quarter in {selected_state}')
        
        plt.legend(bee_data_state['year'].unique())         
        plt.show()"""
    
   
            
def pie_chart(bee_data):
        #selecting year 
        selected_year = 2021
        
        final_data = bee_data.loc[bee_data['year'] == selected_year]

        
        #selecting quarter of the year
        final_data = final_data.loc[final_data['quarter']== 4]
        
        #removal of United States datapoint 
        removal = final_data['state']=='United States'
        
        final_data = final_data[~removal]
        plt.figure(figsize =(20,20))
        plt.pie(final_data['num_colonies'], labels = final_data['state'], autopct='%1.1f%%')
        
        plt.title("Precent of Bee Colonies Allocated in Each State in the United States")

        plt.show()
            




def correlation_co_of_GDP_and_pop(gdp_data, bee_data):
    
    #need to ensure the data years line up, so making sure both arrays range from
    #2016 to 2021
    
    gdp_data = gdp_data[(gdp_data['Year'] >= 2015) & (gdp_data['Year']<= 2021)]

    bee_data = bee_data[(bee_data['year'] >= 2015) & (bee_data['year'] <= 2021)]

    bee_data = bee_data.loc[bee_data['quarter'] == 4]
    bee_data =bee_data.loc[bee_data['state'] == 'United States']
    
    gdp_data = gdp_data['GDP'].replace("[\$,B]",'',regex=True).astype(float)
    
    
    #print(gdp_data)
    #print(bee_data['num_colonies'])
    #print(gdp_data)
    
   # print("/n", bee_data.head)
    bee_pop_corr = np.corrcoef(bee_data['num_colonies'], gdp_data)
    
    bee_loss_corr = np.corrcoef(bee_data['lost_colonies'], gdp_data)
    
    print(bee_loss_corr)
    
    #print(bee_data.columns)
    
    #print(bee_pop_corr)
    if bee_pop_corr[0][1] > 0:
        print("There is a postive correlation between number of colonies and the amount of GDP")
    
    

    
        

def main():
    
    Selected_state =  input("Which State would you like to focus on? ")
    Selected_quarter =  input("Which quarter would you like to focus on? ")
    
    colony_amount_over_years(bee_data, Selected_state)
    
    #larger_trend_col_amount(bee_data)
    #pie_chart(bee_data)
    #correlation_co_of_GDP_and_pop(gdp_data, bee_data)



if __name__=="__main__":
    main()

            
            
            