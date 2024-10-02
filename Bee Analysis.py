# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:33:07 2023

@author: Souren Prakash
"""

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns

bee_fi = r"C:\Users\Souren Prakash\OneDrive\Desktop\Bee Project\save_the_bees.csv"
gdp_fi = r"C:\Users\Souren Prakash\OneDrive\Desktop\Bee Project\USA GDP Growth 1961-2021.xlsx"
carbon_data = r"C:\Users\Souren Prakash\OneDrive\Desktop\Bee Project\IEA_EDGAR_CO2_1970_2022.xlsx"

#bee data including states and colonies
bee_data = pd.read_csv(bee_fi)

#carbon emission data
carbon_data = pd.read_excel(carbon_data)

#shows GDP of the USA over close to 80 years
gdp_data = pd.read_excel(gdp_fi)

#selected_state = 'California'



def format_gdp_data(gdp_data):
    gdp_data = gdp_data[(gdp_data['Year'] >= 2015) & (gdp_data['Year'] <= 2021)]
    return gdp_data

def colo_amount(data, state, quarter):
    """

    :param data: data frame, specifically bee data
    :param state: the state of focus
    :param quarter: the quarter wanted to focus on
    :return: shows a single trend line
    """
    state_names = data['state'].unique()

    if state not in state_names :
        print('State not found ')
    else:
        state_data = data.loc[data['state'] == state]
        selected_data = state_data.loc[state_data['quarter'] == quarter]

    print (selected_data)
    x = selected_data['year']
    y = selected_data['num_colonies']
    print(data['num_colonies'].dtype)
    plt.plot(x, y, color='red')

    plt.xlabel('years')
    plt.ylabel(f'number of Colonies in {state}')
    plt.show()

    
def larger_trend_col_amount(data, selected_state):
    """
    :param data: A dataframe, this works specifically for bee data
    :param selected_state: state of focus to see the trend lines for each quarter

    :return: returns a plot with the colony trend for each year
    """

    print(data['state'])
    if selected_state not in data['state'].unique():
        print("state not found")
        return
    else:
    #seperating data based on state
        bee_data_state = data.loc[data['state']== selected_state]
        
        ax = plt.subplot()
        
        for year in bee_data_state['year'].unique():
            year_data = bee_data_state.loc[bee_data_state['year'] == year]
            ax.plot(year_data['quarter'], year_data['num_colonies'], label =f'{year}')
            
        ax.set_xlabel("Quarters")
        ax.set_ylabel("Number of Colonies")
        ax.set_title(f'Number of Colonies Each Quarter in {selected_state}')
        
        plt.legend(bee_data_state['year'].unique())         
        plt.show()
        
        
    

        

    


def loss_of_population_line_graph(bee_data, selected_state):
    """
    :param bee_data: bee dataset which is cleaned
    :param selected_state: the state which we want to focus on
    :return: plot of data which includes every year in the dataset along with all quarter data
    per year
    """
    
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
        print("There is a postive correlation between number of colonies and the GDP")
    
def heat_map(data):
    sns.heatmap(data, cmpa='coolwarm', annot=True)

    plt.show()


#def sankey_for_bee_data(data):


def main():


    colo_amount(bee_data, 'New York', 3)
    Selected_state ='New York'
    Selected_quarter = 3
    #Selected_state =  input("Which State would you like to focus on? ")
    #Selected_quarter =  input("Which quarter would you like to focus on? ")

    


    #looking at trends of bee colony data for all years and quarters
    larger_trend_col_amount(bee_data, Selected_state)


    #pie_chart(bee_data)
    correlation_co_of_GDP_and_pop(gdp_data, bee_data)


    limit_gdp_data = format_gdp_data(gdp_data)
    #heat_map(bee_data)


if __name__=="__main__":
    main()

            
            
            