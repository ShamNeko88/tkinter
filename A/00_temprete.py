"""
テンプレート
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
      pass
        

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()