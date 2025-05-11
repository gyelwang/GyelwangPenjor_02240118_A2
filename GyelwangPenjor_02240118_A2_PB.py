
class PokemonCardBinder:
    def __init__(self):
        self.binder = {}
        self.max_entries = 1025

    def get_slot(self, pokedex_no):
        pos = pokedex_no - 1 
        return pos // 64 + 1, (pos % 64) // 8 + 1, (pos % 8) + 1

    def add_entry(self):
        try:
            num = int(input("Enter Pokedex number (1–1025): "))
            if num < 1 or num > self.max_entries:
                print("Invalid number.")
                return
            if num in self.binder:
                page, row, col = self.binder[num]
                print(f"Already exists -> Page {page}, Row {row}, Column {col}")
            else:
                slot = self.get_slot(num)
                self.binder[num] = slot
                print(f"Added -> Page {slot[0]}, Row {slot[1]}, Column {slot[2]}")
                if len(self.binder) == self.max_entries:
                    print("You've collected them all!")
        except ValueError:
            print("Please enter a valid number.")

    def reset_binder(self):
        confirm = input("Type 'CONFIRM' to clear all data: ")
        if confirm == "CONFIRM":
            self.binder.clear()
            print("Binder reset complete.")

    def show_binder(self):
        print("\nYour Binder:")
        if not self.binder:
            print("It's currently empty.")
        else:
            for num in sorted(self.binder):
                p, r, c = self.binder[num]
                print(f"#{num}: Page {p}, Row {r}, Column {c}")
        print(f"Total cards: {len(self.binder)} / {self.max_entries}")
        print(f"Completion: {round(len(self.binder) / self.max_entries * 100, 1)}%")

    def play(self):
        while True:
            print("\nPokémon Binder Manager")
            print("1. Add card")
            print("2. Clear binder")
            print("3. View binder")
            print("4. Exit")
            option = input("Choose: ")

            if option == "1":
                self.add_entry()
            elif option == "2":
                self.reset_binder()
            elif option == "3":
                self.show_binder()
            elif option == "4":
                print("Exiting binder manager.")
                break
            else:
                print("Invalid option.")


                
PokemonCardBinder().play()
