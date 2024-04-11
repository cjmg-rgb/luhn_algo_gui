import tkinter as tk

root = tk.Tk()
root.title("Credit Card Verification")
main_frame = tk.Frame(root).grid(column=0, row=0)


def cipher(card_number):

    card_number_translation = str.maketrans({" ": "", "-": ""})
    translated_credit_card = card_number.translate(card_number_translation)

    mult_by_1 = translated_credit_card[1::2]
    mult_by_2 = translated_credit_card[::2]

    total = 0
    text = ""
    color = ""

    for num in mult_by_1:
        total += int(num)

    for num in mult_by_2:
        temp_num = str(int(num) * 2)
        if len(temp_num) > 1:
            total += int(temp_num[0]) + int(temp_num[1])
        else:
            total += int(temp_num)

    print(total)

    if total % 10 == 0:
        text = "VALID!"
        print(int(str(total)[0]) + int(str(total)[1]) % 10)
    elif not int(str(total)[0]) + int(str(total)[1]) % 10:
        print("Test")
        text = "VALID!"
    else:
        text = "INVALID!"

    color = "green" if text == "VALID!" else "red"

    tk.Label(main_frame, foreground=color, text=f"Your card is {text}", font=("Arial", 14)).grid(pady=10, padx=10, row=1, column=1)

def main():

    tk.Label(main_frame, text="Credit Card Number", font=("Arial", 14)).grid(pady=10, padx=10, row=0, column=0)
    tk.Label(main_frame, text="Luhn Algorithm:", font=("Arial", 14)).grid(padx=10, pady=10, row=1, column=0, sticky=tk.E)

    entry = tk.Entry(main_frame, borderwidth=3, font=("Arial", 16), justify="center")
    entry.grid(pady=10, padx=10, row=0, column=1)

    tk.Button(main_frame, command= lambda : cipher(entry.get()), text="validate", padx=10, pady=5, font=("Arial", 16), foreground="white", background="#107ed9").grid(pady=10, padx=10, row=2, column=1)

    root.mainloop()


if __name__ == '__main__':
    main()