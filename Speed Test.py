from tkinter import * 
import speedtest

root = Tk()
root.configure(bg = "coral")
root.title("Internet Speed Test")
root.geometry("500x300")

label = Label(root, text = "Internet Speed Check", font = ("Lucida Sans", 20, "bold", "italic"), fg = "gray", bg = "coral")
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

label_download = Label(root, text = "Download Speed ↓", font = ("Segeo Print", 18, "bold"), fg = "medium sea green", bg = "coral")
label_download.place(relx = 0.25, rely = 0.5, anchor  = CENTER)

label_upload = Label(root, text = "Upload Speed ↑", font = ("Segoe Print", 18, "bold"), fg = "medium orchid", bg = "coral")
label_upload.place(relx = 0.75, rely = 0.5, anchor = CENTER)

label_download_speed = Label(root, font = ("Yu Gothic Light", 14, "bold"), bg = "coral")
label_download_speed.place(relx = 0.25, rely = 0.6, anchor = CENTER)

label_upload_speed = Label(root, font = ("Yu Gothic Light", 14, "bold"), bg = "coral")
label_upload_speed.place(relx = 0.75, rely = 0.6, anchor = CENTER)

def speedCheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['text'] = str(upload_speed) + "mbps"

btn_speed = Button(root, text = "Check Speed", command = speedCheck, bg = "CadetBlue1", fg = "White", relief = FLAT)
btn_speed.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()