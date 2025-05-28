class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self,name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet is not of type pet")
        pet.owner = self
    
    def print_pets(self):
        if not self.pets():
            print(f"{self.name} has no pets.")
        else:
            print(f"{self.name}'s pets:")
            for pet in self.pets():
                print(f"Pet name: {pet.name}, Pet type: {pet.pet_type}")
    

    def get_sorted_pets(self):
      owned_pets = self.pets()
      if not all(isinstance(pet, Pet) for pet in owned_pets):
          raise TypeError("All pets must be Pet instances")
      return sorted(owned_pets, key = lambda pet: pet.name)