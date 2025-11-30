adult_bf2 = float(11.17)
adult_af2 = float(12.45)
child_bf2 = float(8)
child_af2 = float(9.68)
total_cost = float(0)
print('''
Available movies today:
A)12 Strong:    1)2:30	2)4:40	3)7:50	4)10:50
B)Coco:	        1)12:40	2)3:45
C)The Post:	1)12:45	2)3:35	3)7:05	4)9:55''')
movie_choice = input("Movie choice:   ")
if movie_choice not in ["A","B","C"]:
    print("Invalid option; please restart app...")
else:
    showtime = int(input("Showtime:     "))
    if movie_choice == "A" and showtime not in (1,2,3,4):
        print("Invalid option; please restart app...")
    elif movie_choice == "B" and showtime not in (1, 2):
        print("Invalid option; please restart app...")
    elif movie_choice == "C" and showtime not in (1, 2, 3, 4):
        print("Invalid option; please restart app...")
    else:
        adult = int(input("Adult tickets:  "))
        kid = int(input("Kid tickets:    "))
        if adult + kid > 30:
            print("Invalid option; please restart app...")
        else:
            if (movie_choice == "B" or movie_choice == "C") and showtime == 1:
                total_cost = (adult * adult_bf2) + (kid * child_bf2)
                print(f"Total cost:     ${total_cost:.2f}")
            else:
                total_cost = (adult * adult_af2) + (kid * child_af2)
                print(f"Total cost:     ${total_cost:.2f}")




    


