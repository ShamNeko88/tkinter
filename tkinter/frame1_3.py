"""
フレームの入れ子
P20
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("ウィンドウのタイトル")
        master.geometry("400x300")


        self.propagate(False) # フレーム内部のウィジェットにフレームの大きさを合わせるかどうか決める
        
        # フレームの配置
        self.pack()

        # ウィジェット配置
        self.create_widgets()

    # ウィジェット配置するメソッド
    def create_widgets(self):
        # 一つ目のフレーム作成
        frame1 = tk.Frame(self.master, relief=tk.RIDGE, bd=2)
        list1 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")]
        for text, color in list1:
            label1 = tk.Label(frame1, text=text, bg=color, font=("20"))
            label1.pack(side=tk.LEFT) # ラベルをframe1に配置
        frame1.place(relx=0.1, rely=0.1) # 1つ目のフレームを配置
        
        # 2つ目のフレームを作製
        frame2 = tk.Frame(self.master, relief=tk.RIDGE, bd=2)
        list2 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")]
        for i, (text, color) in enumerate(list2):
            label1 = tk.Label(frame2, text=text, bg=color, font=("20"))
            label1.grid(row=i//2, column=i%2) # ラベルをframe2に配置
        frame2.place(relx=0.6, rely=0.5) # 1つ目のフレームを配置
        

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()
