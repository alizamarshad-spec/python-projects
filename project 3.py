import pandas as pd
import os

shelter_A_data = {
    'Pet_Name': ['Max', 'Bella', 'Charlie', 'Lucy', 'Rocky', None],
    'Animal_Type': ['Dog', 'Cat', 'Dog', 'Cat', 'Dog', 'Dog'],
    'Age_Years': [3, 2, 5, 1, 4, None]
}

shelter_B_data = {
    'Pet_Name': ['Daisy', 'Molly', 'Bailey', 'Coco', 'Sadie', 'Buddy'],
    'Animal_Type': ['Dog', 'Cat', 'Dog', 'Cat', 'Dog', 'Dog'],
    'Age_Years': [2, 4, 3, 1, 5, None]
}

df_A = pd.DataFrame(shelter_A_data)
df_B = pd.DataFrame(shelter_B_data)

df_A.to_csv('shelter_A.csv', index=False)
df_B.to_csv('shelter_B.csv', index=False)


class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True
        print(f"{self.name} has been adopted! Status: {self.is_adopted}")


shelter_A = pd.read_csv('shelter_A.csv')
shelter_B = pd.read_csv('shelter_B.csv')
combined = pd.concat([shelter_A, shelter_B], ignore_index=True)

cleaned = combined.dropna()
dogs_only = cleaned[cleaned['Animal_Type'].str.lower() == 'dog']

selected = dogs_only.iloc[0]
pet = RescuePet(selected['Pet_Name'], selected['Animal_Type'], selected['Age_Years'])
pet.process_adoption()

adoption_data = pd.DataFrame([{
    'Pet_Name': pet.name,
    'Animal_Type': pet.species,
    'Age_Years': pet.age,
    'Adoption_Status': pet.is_adopted
}])

file_exists = os.path.isfile('successful_adoptions.csv')
adoption_data.to_csv('successful_adoptions.csv', mode='a', header=not file_exists, index=False)

print("Successfully added {pet.name} to successful_adoptions.csv")
print("shelter_A.csv")
print("shelter_B.csv")