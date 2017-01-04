import tkinter as tk

class GUI:
    """
    simple gui to display the data from the bed file
    """
    # default size and width
    WIDTH = 700
    HEIGHT = 300

    # display format
    format = "sequence %d: %s length: %d"
    headline_format = "found %d sequences:"

    # the dictionary of chromosomes and sequences
    solution = None

    # the window
    top = None
    # chromosome list box
    list_chromosome = None
    # list of sequences
    list_seq = None

    def __init__(self, lines):

        self.solution = lines

        # open the window
        self.top = tk.Tk()
        # set the window to not resizable
        self.top.resizable(width=False, height=False)
        # add the list box
        self.list_chromosome = tk.Listbox(self.top)
        i = 0
        for key in self.solution.keys():
            self.list_chromosome.insert(i, key)
            i += 1
        self.list_chromosome.pack(side=tk.LEFT, fill=tk.BOTH)
        # make the list box listen to picks
        self.list_chromosome.bind("<<ListboxSelect>>", self.on_select)
        # add the sequence list
        self.list_seq = tk.Text(self.top)
        self.list_seq.pack()
        # show the window
        self.top.mainloop()

    def on_select(self, event):
        """
        when an item is changed change the content of the text
        :param event:
        :return:
        """
        # get the selection and clear the text
        widget = event.widget
        self.list_seq.config(state=tk.NORMAL)
        self.list_seq.delete('1.0', tk.END)
        index = int(widget.curselection()[0])
        value = widget.get(index)
        # add some basic data:
        self.list_seq.insert(tk.END, self.headline_format % (len(self.solution[value])))
        self.list_seq.insert(tk.END, '\n')
        # add the data from the lists in the correct format
        for i in range(len(self.solution[value])):
            line_format = self.make_format(self.solution[value][i],i)
            self.list_seq.insert(tk.END, line_format)
            self.list_seq.insert(tk.END, '\n')

        # disable text editing
        self.list_seq.config(state=tk.DISABLED)

    def make_format(self, line, index):
        """
        change the given data from one line into the desired format
        :param line:
        :param index:
        :return:
        """
        start = line[0]
        end = line[1]
        diff = end - start
        return self.format % (index, "(%s , %s)" % (start, end), diff)


if __name__ == '__main__':
    gui = GUI()