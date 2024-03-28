"""
ウィジェット変数の取り扱い
P43
"""
"""
テンプレート
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("ウィンドウのタイトル")
        master.geometry("300x200")
        self.propagate(False) # フレーム内部のウィジェットにフレームの大きさを合わせるかどうか決める        
        
        # ウィジェット変数を生成
        self.name_var = tk.StringVar(value="山田　太郎")
        self.age_var = tk.IntVar(value=20)
        self.agreement_var = tk.BooleanVar(value=False)

        # フレームの配置
        self.pack()

        # ウィジェット配置
        self.create_widgets()

    # ウィジェット配置するメソッド
    def create_widgets(self):
        # 氏名
        self.name = tk.Entry(self.master, textvariable= self.name_var)
        self.name.pack()

        # 年齢
        self.age = tk.Spinbox(self.master, textvariable=self.age_var, from_=0, to=120)
        self.age.pack()

        # 同意
        self.agreement = tk.Checkbutton(self.master, text="同意します！！！", variable=self.agreement_var)
        self.agreement.pack()

        # ボタンフレーム
        self.buttonframe = tk.Frame(self.master)
        self.buttonframe.pack()

        # sampleボタン
        self.sample = tk.Button(self.buttonframe, text="入力例を表示^_^", command=self.inputSampleValue)
        self.sample.pack(side="left")

        # 確認ボタン
        self.varify = tk.Button(self.buttonframe, text="確認", command=self.outputValue)
        self.varify.pack(side="left")

    # inputSampleValue定義
    def inputSampleValue(self):
        self.name_var.set(value="鈴木　一郎")
        self.age_var.set(value=31)
        self.agreement_var.set(value=False)
    
    # outputValue定義
    def outputValue(self):
        print(self.name_var.get())
        print(self.age_var.get())
        print(self.agreement_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()