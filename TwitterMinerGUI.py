from Tkinter import *

import TwitterAnalyzer


def quitProgram(self):
    root.destroy()

def analyze(self):
    results = TwitterAnalyzer.analyzeTrends(first_country,second_country)
    output_results.config(state=NORMAL)
    output_results.delete(1.0,END)
    output_results.insert(END,results)
    output_results.see(END)
    output_results.config(state=DISABLED)

############# GUI CODE ################

#------------ constant values --------------#
buttons_width = 20

buttonimb_x = "2m"
buttonimb_y = "1m"

buttoncontainerimb_x = "3m"
buttoncontainerimb_y = "2m"
buttoncontainerintimb_x = "3m"
buttoncontainerintimb_y = "1m"
#-------------------------------------------#

root = Tk()

selector_container = Frame(root, width = 300, height = 200)
selector_container.pack(
    side = TOP,
    fill = BOTH,
    expand = YES
    )

button_container = Frame(root)
button_container.pack(
    ipadx = buttoncontainerintimb_x,
    ipady = buttoncontainerintimb_y,
    padx = buttoncontainerimb_x,
    pady = buttoncontainerimb_y
    )

output_container = Frame(root, width = 300, height = 200)
output_container.pack(
    side = BOTTOM,
    fill = BOTH,
    expand = YES
    )

first_country = Entry(selector_container)
first_country.pack(side = TOP)
first_country.delete(0, END)
first_country.insert(0, "World")

second_country = Entry(selector_container)
second_country.pack(side = TOP)
second_country.delete(0, END)
second_country.insert(0, "Italy")


analyze_button = Button(button_container)
analyze_button.configure(
    text = "Find Common Trends",
    width = buttons_width,
    padx = buttoncontainerimb_x,
    pady = buttoncontainerimb_y
    )
analyze_button.pack(side = LEFT)
analyze_button.focus_force()
analyze_button.bind("<Button-1>", analyze)
analyze_button.bind("<Return>", analyze)

output_results = Text(output_container)
output_results.pack(
    side = BOTTOM,
    fill = BOTH,
    expand = YES
    )
output_results.configure(state=DISABLED)

exit_button = Button(button_container)
exit_button.configure(
    text = "Exit",
    width = buttons_width,
    padx = buttoncontainerimb_x,
    pady = buttoncontainerimb_y
    )
exit_button.pack(side = RIGHT)
exit_button.bind("<Button-1>", quitProgram)
exit_button.bind("<Return>", quitProgram)

root.mainloop()
#######################################
