"""
ストップウォッチ
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("ストップウォッチ")
        master.geometry("400x160")

        # 変数定義
        self.startTime = 0.0 # 開始時間
        self.elapseTime = 0.0 # 経過時間
        # 実行内容
        self.pack()
        self.create_widgets() # ウィジェット配置

    # ウィジェット配置するメソッド
    def create_widgets(self):
      # canvasウィジェットを作成
      self.canvas = tk.Canvas(self.master, width=380, height=80, bg="lightgreen")
      self.canvas.place(x=10, y=10)

      # 経過時間を表示
      self.canvas.create_text(380, 40, text=round(self.elapseTime, 1), font=("MS ゴシック体", "24", "bold"), tag="Time", anchor="e")
    
      # スタートボタン
      startButton = tk.Button(self.master, text="スタート", font=("MS ゴシック体", "18", "bold"))
      startButton.place(x=10, y=100)

      # ストップボタン
      stopButton = tk.Button(self.master, text="ストップ", font=("MS ゴシック体", "18", "bold"))
      stopButton.place(x=140, y=100)
      
      # リセットボタン
      resetButton = tk.Button(self.master, text="リセット", font=("MS ゴシック体", "18", "bold"))
      resetButton.place(x=270, y=100)

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()