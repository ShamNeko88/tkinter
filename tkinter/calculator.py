"""
テンプレート
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("電卓アプリ")
        master.geometry("310x440")

        self.button_number = [ # ボタン
            ["B", "", "C", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]

        # 実行内容
        self.pack() # フレームの配置
        self.create_widgets() # ウィジェット配置
        self.create_button()

    # ウィジェット配置するメソッド
    def create_widgets(self):
        # ディスプレイ用のフレーム
        self.calc_frame = tk.Frame(self.master, width=300, height=60,bg="lightgreen")
        self.calc_frame.propagate(False) # サイズを内側のwidgetsには合わせない
        self.calc_frame.pack(side=tk.TOP, padx=10, pady=20)

        # ボタンのフレーム
        self.button_frame = tk.Frame(self.master, width=300, height=360, bg="gray")
        self.button_frame.propagate(False)
        self.button_frame.pack(side=tk.TOP)
        
        # 変数定義
        self.calc_var = tk.StringVar() # 計算式用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数     

        # 計算式用ディスプレイ
        self.calc_label = tk.Label(self.calc_frame, textvariable=self.calc_var, font=("游ゴシック体", "15", "bold")) # 計算式用のLabel
        self.calc_label.pack(anchor=tk.E) # 右揃えで配置
        
        # 結果用ディスプレイ
        self.ans_label = tk.Label(self.calc_frame, textvariable=self.calc_var, font=("游ゴシック体", "20", "bold"))
        self.ans_label.pack(anchor=tk.E) # 右揃えで配置
        
    # create_buttonメソッドを定義
    def create_button(self):
        for y, row in enumerate(self.button_number): # button_numberリストの各要素を取得
            for x, num in enumerate(row): # button_number リストの各要素内の要素を取得
                button = tk.Button(self.button_frame, text=num, font=("游ゴシック体", "15", "bold"), width=5, height=2)
                button.grid(row=y, column=x) # 列、行を指定して配置

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()