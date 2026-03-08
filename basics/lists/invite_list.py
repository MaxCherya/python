people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# Send invitations to the first three people in the list
for person in people[:3]:
    print(f"Dear {person}, you are invited to the party!")

cancelled_people = ['Charlie', 'David']
# Remove cancelled people from the invitation list
for person in cancelled_people:
    if person in people:
        people.remove(person)
# Send updated invitations to the remaining people in the list
for person in people:
    print(f"Dear {person}, you are still invited to the party!")

new_people = ['Frank', 'Grace']
# Add new people to the invitation list
people.extend(new_people)
# Send invitations to the updated list of people
for person in people:
    print(f"Dear {person}, you are invited to the party!")

only_space_for_two_more = [people[0], people[1]]
# Inform the remaining people about the limited space
for person in people[2:]:
    print(f"Dear {person}, unfortunately, we can only invite two more people to the party. We apologize for the inconvenience.")