"""
オブジェクト指向
"""
import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("ウィンドウのタイトル")
        master.geometry("400x300")

        # フレームの設定
        self.config(bg="green", background="green", width=200, height=100) # 設定

        self.propagate(False) # フレーム内部のウィジェットにフレームの大きさを合わせるかどうか決める
        
        # フレームの配置
        self.pack()

        # ウィジェット配置
        self.create_widgets()

    # ウィジェット配置するメソッド
    def create_widgets(self):
        # ラベル作成
        self.label1 = tk.Label(self, text="これはラベルです")
        self.label1.pack()
        
        # エントリーの作成
        self.entry = tk.Entry(self)
        self.entry.insert(tk.END, "これはエントリーです")
        self.entry.pack()

        # ボタンを作成
        self.button1 = tk.Button(self.master, text="これはボタンです。緑のフレームを削除", command=self.del_widgets)
        self.button1.pack()
    
    # ウィジェット削除
    def del_widgets(self):
      # self.destroy()
      self.forget()
        

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Frame1(master=root)
    f1.mainloop()