"""
ストップウォッチ
"""
import tkinter as tk
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # tk.Frameのコンストラクタ呼び出し

        master.title("ストップウォッチ")
        master.geometry("400x160")

        # 変数定義
        self.startTime = 0.0 # 開始時間
        self.elapseTime = 0.0 # 経過時間
        self.after_id = 0 # after_id変数を定義

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
      startButton = tk.Button(self.master, text="スタート", font=("MS ゴシック体", "18", "bold"), command=self.startButtonClicked)
      startButton.place(x=10, y=100)

      # ストップボタン
      stopButton = tk.Button(self.master, text="ストップ", font=("MS ゴシック体", "18", "bold"), command=self.stopButtonClicked)
      stopButton.place(x=140, y=100)
      
      # リセットボタン
      resetButton = tk.Button(self.master, text="リセット", font=("MS ゴシック体", "18", "bold"), command=self.resetButtonClicked)
      resetButton.place(x=270, y=100)
    
    # スタートボタンが押された時の処理
    def startButtonClicked(self):
        self.startTime = time.time() - self.elapseTime # startTime変数に開始時間を代入
        self.updateTime() # updateTime関数を実行

    # 表示時間の更新処理
    def updateTime(self):
        self.canvas.delete("Time") # 表示時間を削除
        self.elapseTime = time.time() - self.startTime # 経過時間を代入
        self.canvas.create_text(380, 40, text=round(self.elapseTime, 1), font=("MS ゴシック体", "24", "bold"), tag="Time", anchor="e") # 経過時間を表示
        self.after_id = self.after(10, self.updateTime)
    
    # ストップボタンが押された時の処理
    def stopButtonClicked(self):
        self.after_cancel(self.after_id) # updateTime関数の再帰処理を終了

    # リセットボタンが押された時の処理
    def resetButtonClicked(self):
        self.startTime = time.time() # startTime変数に現在時刻を代入
        self.elapseTime = 0.0 # elapsedTime変数を初期化
        self.canvas.delete("Time") # 表示時間を消去
        self.canvas.create_text(380, 40, text=round(self.elapseTime, 1), font=("MS ゴシック体", "24", "bold"), tag="Time", anchor="e") # 時間0.0を表示 

if __name__ == "__main__":
    root = tk.Tk()
    f1 = Application(master=root)
    f1.mainloop()