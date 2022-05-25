import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# First data source is the Lost, Found, and Adoptable Pets dataset
lfa = pd.read_csv('LostFoundAdoptable.csv')

# Subset data base on species, sex, and record
PetData = (lfa[['animal_type', 'Animal_Gender', 'Record_Type']])

# Subset data based on species
CatData = PetData[PetData['animal_type'].str.contains('Cat')]
DogData = PetData[PetData['animal_type'].str.contains('Dog')]

# Subset data based on adoptability
AdoptableCat = CatData[CatData['Record_Type'] == 'ADOPTABLE']
AdoptableDog = DogData[DogData['Record_Type'] == 'ADOPTABLE']

# Cat Adoptability Proportion
CatAdoptProp = (len(AdoptableCat) / len(CatData)) * 100

# Dog Adoptability Proportion
DogAdoptProp = (len(AdoptableDog) / len(DogData)) * 100

# z-Test between dog and cat adoptability
adopt = [len(AdoptableCat), len(AdoptableDog)]
n = [len(DogData), len(CatData)]
print(proportions_ztest(adopt, n))