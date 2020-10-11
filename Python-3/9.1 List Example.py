list1=[1,2,4,5,7]
list2=[30,40]  
list3=list1+list2
print(list3);
print('minimum value in list :',min(list3));
print('maximim value in list ',max(list3));
list3.sort();
print('Sorted value in list ',list3);
list3.reverse();
print('Reverse value in list ',list3);

list3.insert(2,78);
print('After inserting  value in list ',list3);
list3.remove(78);
print('After remove value in list ',list3);
list3.append(50);
print('After append value in list ',list3);

print('Counting  value in list ',list3.count(40));


