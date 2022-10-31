#!/usr/bin/env python
# coding: utf-8


#This function can be used to plot total DOS and partial dos (up+down) for a whole struture from the file generated using vaspkit package using 11 - 111 commands.

def total_dos_for_a_str(filename):
    file = open(str(filename),'r') #data contained in a file
    
    lines = file.readlines()
    energy_array, str_dw_array, str_up_array = [], [], []

    #for positive dos values
    counter = -1 #just a counter
    for line in lines:
        counter = counter + 1
        a = line.strip().split() #striping and spliting the lines to extract energy and dos information 
        if counter != 0: #Extracting relevant information and appending them into arrays
            energy = float(a[0])
            energy_array.append(energy)
            
            #extracting up dos for a whole structure
            up_dos = float(a[1])
            str_up_array.append(up_dos)
            #extracting down dos for whole structure
            down_dos = float(a[2])
            str_dw_array.append(down_dos)
    
    
    #converting negative dos to postive dos for adding up
    str_dw_array_reversed = [i*-1 for i in str_dw_array] # Multiplying down states with -1 to add later with up states dos
    
    #adding_up_the_dos
    from operator import add
    total_str_dos = [sum(x) for x in zip(str_up_array, str_dw_array_reversed)] #Adding the up and down states 
    
    #ploting the dos
    import matplotlib.pyplot as plt
    
    #fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5)) #for both the elements
    fig, ax = plt.subplots(2)
    
    #ploting for diff element
    ax[0].plot(energy_array, total_str_dos, color = 'black', label = 'Total DOS')
    ax[1].plot(energy_array, str_up_array, color = 'red', label = 'Up states')
    ax[1].plot(energy_array, str_dw_array, color = 'blue', label = 'Down states')

    for i in range(2):
        ax[i].axvline(x = 0,linestyle = '--',color = 'black')
        ax[i].axhline(y = 0,linestyle = '--',color = 'black')
        ax[i].set_xlabel('Energy (eV)', fontsize = 14)
        ax[i].set_ylabel('Density of states', fontsize = 14)
        ax[i].tick_params(axis = "x", labelsize = 12)
        ax[i].tick_params(axis = "y", labelsize = 12)
        ax[i].legend()
        ax[i].grid()
    plt.tight_layout()
    plt.savefig('Total_DOS_plot_for_a_str.pdf')
    return()
    
total_dos_for_a_str('TDOS.dat')            
            
            
            

