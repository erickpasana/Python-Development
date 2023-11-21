from tkinter import *
import requests


# def get_quote():
#     API = "https://api.kanye.rest"
#     response = requests.get(url=API)
#     canvas.itemconfig(quote_text, text=response)
#     response.raise_for_status()


def get_quote():
    API = "https://api.kanye.rest"
    # Use a try-except block to handle errors
    try:
        # Make a GET request to the API
        response = requests.get(url=API)
        # Raise an exception if the status code is not 200
        response.raise_for_status()
        # Get the data as a Python dictionary
        data = response.json()
        # Get the quote as a string
        quote = data['quote']
        # Update the text of the quote_text item on the canvas
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException as e:
        # Print or display the HTTP error message
        print(e)
        canvas.itemconfig(quote_text, text="An HTTP error occurred.")
    except json.decoder.JSONDecodeError as e:
        # Print or display the JSON error message
        print(e)
        canvas.itemconfig(quote_text, text="A JSON error occurred.")
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()