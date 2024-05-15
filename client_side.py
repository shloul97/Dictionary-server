import socket
import tkinter as tk

# Function to define word
def define_word(command):

    port = int(port_entry.get())
    word = word_entry.get().strip()
    addr = addr_entry.get().strip()

    
    
    if word:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client_socket.connect((addr, port))

            if command == 'define':
                client_socket.send(f"define {word}".encode())
                definition = client_socket.recv(1024).decode()
                status_label.config(text=definition)
                client_socket.close()

            elif command == 'add':
                defe = definition_entry.get().strip()
                if defe:
                    client_socket.send(f"add {word}:{defe}".encode())
                    
                    replay = client_socket.recv(1024).decode()
                    status_label.config(text=replay)

                    client_socket.close()
                else:
                    status_label.config(text="You must add a definition")

        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Please enter a word.")


root = tk.Tk()
root.title("Dictionary Client")

addr_label = tk.Label(root, text="Address:")
addr_label.pack()
addr_entry = tk.Entry(root)
addr_entry.pack()

port_label = tk.Label(root, text="Port:")
port_label.pack()
port_entry = tk.Entry(root)
port_entry.pack()

word_label = tk.Label(root, text="Word:")
word_label.pack()
word_entry = tk.Entry(root)
word_entry.pack()

definition_label = tk.Label(root, text="Definition:")
definition_label.pack()
definition_entry = tk.Entry(root)
definition_entry.pack()

define_button = tk.Button(root, text="Define", command= lambda: define_word('define'))
define_button.pack()

define_button = tk.Button(root, text="Add", command= lambda: define_word('add'))
define_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()


root.geometry("700x350")
root.mainloop()