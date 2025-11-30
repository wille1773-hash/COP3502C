from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return len(self.pakuri_list)

    def get_species_array(self):
        if len(self.pakuri_list) == 0:
            return None
        else:
            return [pakuri.get_species() for pakuri in self.pakuri_list]
     
    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda x: x.get_species())

    def add_pakuri(self, species):
        for p in self.pakuri_list:
            if p.get_species() == species:
                return False
        if len(self.pakuri_list) >= self.capacity:
            return False
        new_pakuri = Pakuri(species)
        self.pakuri_list.append(new_pakuri)
        return True

    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
