# Chương 8
kingdoms = ['Bacteria', 'Protozoa', 'Chromista',
'Plantaee', 'Fungi','Animaliaa']
print("kingdoms: ", kingdoms)
#1a
print("kingdoms[0] : ", kingdoms[0])
#1b
print("kingdoms[5] : ", kingdoms[5])
#1c
print("kingdoms[:3]: ", kingdoms[:3])
#1d
print("kingdoms[2:5]: ", kingdoms[2:5])
#1e 
print("kingdoms[4:]: ", kingdoms[4:])
#1f
print("kingdoms[1:0]: ", kingdoms[1:0])

#2a
print("kingdoms[-6]: ", kingdoms[-6])
#2b
print("kingdoms[-1]: ", kingdoms[-1])
#2c
print("kingdoms[-6:-3]: ", kingdoms[-6:-3])
#2d
print("kingdoms[-4:-1]: ", kingdoms[-4:-1])
#2e
print("kingdoms[-2:]: ", kingdoms[-2:])
#2f
print("kingdoms[-1:-2]: ", kingdoms[-1:-2])

print("--------/////--------")
#3 Create list of appointments:
appointments = ['9:20', '10:30', '14:00', '15:00', 
'15:30']
print(appointments)
#3a Add them 16:20 to the end of the list
appointments.append('16:30')
print(appointments)
#3b Use the + operator to add '16:30' 
appointments += ['16:30']
print(appointments)
#3c The approach in (a) modifies the list. 
#3c The one in (b) creates a new list.


print("--------/////--------")
#4 Create list of ids:
ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)
#4a Remove 3382 from the list. I use remove()
ids.remove(3382)
print(ids)
#4b  Get the index of 9362. I use index()
index_9362 = ids.index(9362)
print('index of 9362: ',index_9362)
#4c Insert 4499 in the list after 9362
ids.insert(index_9362 + 1, 4499)
print('Add 4499 after 9362: ',ids)
#4d Extend the list by adding [5566, 1830] 
ids.extend([5566, 1830])
print('Add 5566, 1830: ',ids)
#4e  Reverse the list.
ids.reverse()
print('Reversed List:', ids)
#4f  Sort the list.
ids.sort()
print('Sorted list: ', ids)


print("--------/////--------")
#5a a list contains the atomic numbers of the six alkaline earth metals
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
print('alkaline_earth_metals: ',alkaline_earth_metals)
#5b index contains radium’s atomic number. 2 ways 
positive_index = alkaline_earth_metals[5]
print('index contains radium’s atomic number: ', positive_index)
negative_index = alkaline_earth_metals[-1]
print('index contains radium’s atomic number: ', negative_index)
#5c  how many items there are in alkaline_earth_metals?
print('length of alkaline_earth_metals: ', len(alkaline_earth_metals))
#5d the highest atomic number in alkaline_earth_metals
print('the highest atomic number: ', max(alkaline_earth_metals))

print("--------/////--------")
#6a a list of temperatures
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print('temps: ', temps)
#6b sort temps in ascending order
temps.sort()
print('Sorted temps: ', temps)
#6c Using slicing
cool_temps = temps[0:2]
warm_temps = temps[2:]
print('cool_temps: ',cool_temps)
print('warm_temps: ', warm_temps)
#6d Using list arithmetic
temps_in_celsius = cool_temps + warm_temps
print('temps_in_celsius: ', temps_in_celsius)


print("--------/////--------")
#7 Return True if and only if first item of the list is the same as the last
def same_first_last(L) :
    return L[0] == L[-1]
print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))
print(same_first_last(['Duong', 'Binh', 'Cuong', 'Duong']))

print("--------/////--------")
#8 Return True if and only if the length of L1 is longer than the length of L2
def is_longer(L1, L2):
    return len(L1) > len(L2)
print(is_longer([1, 2, 3], [4, 5]))
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))
print(is_longer(['Cao Khanh Duong'],['Cao','Khanh','Duong']))

print("--------/////--------")
#9  values = [0,[0,[0,values,2],2],2]
values = [0,1,2]
values[1] = values
print(values)

print("--------/////--------")
#10 
units =  [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units)
#10a the first inner list]
print('the first inner list: ', units[0])
#10b the last inner list
print('the last inner list', units[-1])
#10c The string 'km'
print('units[0][0]: ', units[0][0])
#10d The string 'kg'
print('units[1][0]: ',  units[1][0])
#10e The list ['miles', 'league']
print('units[0][1:]: ', units[0][1:])
#10f The list ['kg', 'pound']
print('units[1][0:2]: ', units[1][0:2])

print("--------/////--------")
#11 Repeat the previous exercise using negative indices.
#11a the first inner list]
print('the first inner list: ', units[-2])
#11b the last inner list
print('the last inner list', units[-1])
#11c The string 'km'
print('units[-2][-3]: ', units[-2][-3])
#11d The string 'kg'
print('units[-1][-3]: ',  units[-1][-3])
#11e The list ['miles', 'league']
print('units[-2][-2:]: ', units[-2][-2:])
#11f The list ['kg', 'pound']
print('units[-1][:-1]: ', units[-1][0:-1])