#Course: CIS 103
#Instructor: Md Ali
#Student: Sahar Iqbal
#Date: 09/20/2024

# Task: 01 Unique Visitors Tracking:

# Creates a set called `visitors` with names:
Visitors = {'Alice', 'Bob', 'Charlie', 'Diana', 'Edward'}
print(Visitors)

#Add Two new visitors, 'Fiona' and 'George'
Visitors.add('Fiona')
Visitors.add('George')
print("After Adding New visitors:", Visitors)

#'Charlie' visits the website again. Now add 'Charlie' again to the set
Visitors.add('Charlie')
print("After adding Charlie again:", Visitors)    # (adding him again has no effect, it will remains same)

# Remove 'Diana' from the set
Visitors.remove('Diana')
print("After Remove Diana from the set:", Visitors)

# Create a set of Unique visitors
unique_visitors = set("Visitors")

# Calculate total numbers of unique visitors
total_unique_visitors = len(unique_visitors)

# Print the total number of unique visitors
print("Total number of unique visitors:", total_unique_visitors)










