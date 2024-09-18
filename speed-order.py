import time
name_array = ["Greninja", "Mewtwo", "M_Rayquaza", "Seperior", "M_Lucario", "Lugia", "Zoroark", "Garchomp", "M_Charizard_X", "M_Gardevoir", "Charizard", "Typhlosion", "Xerneas", "Yveltal", "Mimikyu", "Kyurem", "Rayquaza", "M_Garchomp", "Giratina", "Lucario", "Suicune", "Arbok", "Chandelure", "Gardevoir", "Empoleon", "Torterra", "M_Mawile", "Mawile", "Golisopod"]
stat_array = [132, 130, 115, 113, 112, 110, 105, 102, 100, 100, 100, 100, 99, 99, 96, 95, 95, 92, 90, 90, 85, 80, 80, 80, 60, 56, 50, 50, 40]


print("Welcome to the Pokemon VRC Speed Order!")
while True:
      pokemon_amount = input("Enter the amount of pokemon: (2/4): ")
      if pokemon_amount == '2':
            input_1 = input("Name the first Pokemon: ")
            input_2 = input("Name the second Pokemon: ")
            if stat_array[name_array.index(input_1)] > stat_array[name_array.index(input_2)]:
                  print(input_1, "is faster than", input_2, "!")
            elif stat_array[name_array.index(input_1)] < stat_array[name_array.index(input_2)]:
                  print(input_1, "is slower than", input_2, "!")
            elif stat_array[name_array.index(input_1)] == stat_array[name_array.index(input_2)]:
                  print(input_1, "is the same speed as", input_2, "!")
      next_calculation = input("Let's do another calculation? (yes/no): ")
      if next_calculation == 'yes':
            continue
      if next_calculation == 'no':
            print("Goodbye!")
            time.sleep(1)
            break