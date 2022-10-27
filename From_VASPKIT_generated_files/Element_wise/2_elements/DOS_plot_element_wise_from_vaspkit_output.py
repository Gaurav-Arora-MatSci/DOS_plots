#!/usr/bin/env python
# coding: utf-8

# In[31]:


#This function can be used to plot total DOS for 2 elements with minor tweeks from the 
#files generated from vaspkit when extractning element dos
def plot_dos_element_wise(filename_up, filename_dw):
    file_up = open(str(filename_up),'r')
    file_dw = open(str(filename_dw), 'r')
    
    lines_up = file_up.readlines()
    lines_dw = file_dw.readlines()
    energy_array, ele_1_dw_array, ele_1_up_array, ele_2_dw_array, ele_2_up_array = [], [], [], [], []

    #for positive dos values
    counter = -1
    for line in lines_up:
        counter = counter + 1
        a = line.strip().split()
        if counter != 0:
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
    ele_1_dw_array = [i*-1 for i in ele_1_dw_array]
    ele_2_dw_array = [i*-1 for i in ele_2_dw_array]
    
    #adding_up_the_dos
    from operator import add
    total_dos_ele_1 = [sum(x) for x in zip(ele_1_dw_array, ele_1_up_array)]
    total_dos_ele_2 = [sum(x) for x in zip(ele_2_dw_array, ele_2_up_array)]
    
    #ploting the dos
    import matplotlib.pyplot as plt
    
    #fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5)) #for both the elements
    fig, ax2 = plt.subplots(figsize = (5,5))
    
    #ploting for diff element
    #ax1.plot(energy_array, total_dos_ele_1)
    ax2.plot(energy_array, total_dos_ele_2, color = 'red')
    ax2.axvline(x = 0,linestyle = '--',color = 'black')
    ax2.axhline(y = 0,linestyle = '--',color = 'black')
    ax2.set_xlabel('Energy (eV)', fontsize = 14)
    ax2.set_ylabel('Density of states', fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    ax2.set_xlim(-5.2,5.2) 
    ax2.set_ylim(-0.4,20)  
    plt.grid()
    plt.tight_layout()
    plt.savefig('DOS_plot_for_element_2.pdf')
    return()
    
plot_dos_element_wise('LDOS_ELEMENTS_UP.dat', 'LDOS_ELEMENTS_DW.dat')            
            
            
            

