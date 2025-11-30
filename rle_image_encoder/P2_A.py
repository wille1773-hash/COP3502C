import console_gfx

def display_menu():
    print("\nRLE Menu\n"
    "--------")
    print('''0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
''')
    
def main():
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of the file to load: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data is loaded.")
        elif option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)

if __name__ == "__main__":
    main()

    