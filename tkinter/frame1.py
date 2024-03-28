"""
フレームウィジェットの作成
"""

import tkinter as tk

# rootインスタンス作成と設定（親）
root = tk.Tk()
root.geometry("400x300") # サイズの設定
root.title("フレームウィジェットテスト") # タイトルの設定

# フレームの作成
frame1 = tk.Frame(
    root,
    background="green", # 背景色
    borderwidth=5, # ボーダーの幅
    relief="sunken", # ボーダーの浮彫
    width=400, # 幅
    height=300 # 高さ
)
frame1.pack() # 配置





root.mainloop()