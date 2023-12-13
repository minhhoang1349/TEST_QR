from PIL import Image, ImageTk
import tkinter as tk
import requests
import urllib.request


#so tien can thanh toan
cost=str(input("cost= "))

head_url="https://img.vietqr.io/image/ocb-0004100038288007-HgRYJqu.png?amount="
tail_url="&addInfo=Thanh%20toan%20he%20thong%20in%20tu%20phuc%20vu&accountName=Nguyen%20Minh%20Hoang"

url=head_url+cost+tail_url
urllib.request.urlretrieve(url, "local.png")

root=tk.Tk()
image = tk.PhotoImage(file = "local.png")
label=tk.Label(root, image=image)
label.pack()
def close():
        label.destroy()
        button.destroy()
        root.destroy()
        
button=tk.Button(root,text="Payment Completed",command=close)
button.pack()        

        
root.mainloop()
