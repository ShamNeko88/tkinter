"""
バインドメソッド
イベント（ユーザー操作）と処理（アクション）を紐づける
P82
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
        # ウィジェット変数
        self.msg = tk.StringVar()
        self.msg.set("") 

        def print_keysym(event):
            self.keysym = event.keysym
            self.msg.set(f"{self.keysym}")
            
        # ラベル作成
        self.label1 = tk.Label(self.master, text="あなたが押したキーは\nキーは", font=("MS ゴシック", "24", "bold"))
        self.label1.pack()

        # もう一個作成
        self.label2 = tk.Label(self.master, textvariable=self.msg, font=("MS ゴシック", "24", "bold"))
        self.label2.bind("<Any-KeyPress>", print_keysym)
        self.label2.pack()
        self.label2.focus_set()



if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()