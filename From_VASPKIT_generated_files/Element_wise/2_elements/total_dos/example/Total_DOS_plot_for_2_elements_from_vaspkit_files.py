#!/usr/bin/env python
# coding: utf-8


#This function can be used to plot total DOS (up+down) for 2 elements from the file generated using vaspkit package. 
#It works with the file named "LDOS_ELEMENTS_DW.dat" and "LDOS_ELEMENTS_UP.dat".

def total_dos_for_2_elements(filename_up, filename_dw):
    file_up = open(str(filename_up),'r') #data contained for up states
    file_dw = open(str(filename_dw),'r') #data contained for down states
    
    lines_up = file_up.readlines()
    lines_dw = file_dw.readlines()
    energy_array, ele_1_dw_array, ele_1_up_array, ele_2_dw_array, ele_2_up_array = [], [], [], [], []

    #for positive dos values
    counter = -1 #just a counter
    for line in lines_up:
        counter = counter + 1
        a = line.strip().split() #striping and spliting the lines to extract energy and dos information 
        if counter == 0: #extarcting the name of the elements from the first line of the file
            first_ele = a[2]
            second_ele = a[3]

        if counter != 0: #Extracting relevant information and appending them into arrays
            energy = float(a[0])
            energy_array.append(energy)
            
            #extracting up dos for 1st element
            ele_1_up = float(a[1])
            ele_1_up_array.append(ele_1_up)
            #extracting up dos for 2nd element
            ele_2_up = float(a[2])
            ele_2_up_array.append(ele_2_up)
    
    #for negative dos values
    counter = -1
    for line in lines_dw:
        counter = counter + 1
        a = line.strip().split()
        if counter != 0:
            
            #extracting up dos for 1st element
            ele_1_dw = float(a[1])
            ele_1_dw_array.append(ele_1_dw)
            #extracting up dos for 2nd element
            ele_2_dw = float(a[2])
            ele_2_dw_array.append(ele_2_dw)
    
    #converting negative dos to postive dos for adding up
    ele_1_dw_array = [i*-1 for i in ele_1_dw_array] # Multiplying down states with -1 to add later with up states dos
    ele_2_dw_array = [i*-1 for i in ele_2_dw_array]
    
    #adding_up_the_dos
    from operator import add
    total_dos_ele_1 = [sum(x) for x in zip(ele_1_dw_array, ele_1_up_array)] #Adding the up and down states 
    total_dos_ele_2 = [sum(x) for x in zip(ele_2_dw_array, ele_2_up_array)]
    
    #ploting the dos
    import matplotlib.pyplot as plt
    
    #fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5)) #for both the elements
    fig, ax = plt.subplots(2)
    
    #ploting for diff element
    ax[0].plot(energy_array, total_dos_ele_1, color = 'blue', label = str(first_ele))
    ax[1].plot(energy_array, total_dos_ele_2, color = 'red', label = str(second_ele))

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
    plt.savefig('Total_DOS_plot_for_2_elements.pdf')
    return()
    
total_dos_for_2_elements('LDOS_ELEMENTS_UP.dat', 'LDOS_ELEMENTS_DW.dat')            
            
            
            

