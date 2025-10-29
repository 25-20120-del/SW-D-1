# 완성본
import tkinter as tk
from tkinter import ttk
import csv
import os

root = tk.Tk()
root.title("도서 조회 및 추천 프로그램")
root.geometry("800x600")
root.configure(bg="white")
widgets = []

text="검색할 도서명을 입력하세요"
novels = []
given_star = 0


class Novel:
    def __init__(self,name,view,star,stargiver,imagefile):
        self.name = name
        self.view = int(view)
        self.star = float(star)
        self.stargiver = float(stargiver)
        self.imagefile = imagefile


def clear_widgets():
    for widget in widgets:
        widget.destroy()
    widgets.clear()


def main_screen():
    clear_widgets()
    
    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True)
    widgets.append(frame)

    title_label = tk.Label(frame, text="📚 정민's 도서", 
                           font=("맑은 고딕", 24, "bold"), bg="white")
    title_label.pack(pady=20)
    widgets.append(title_label)

    input_label = tk.Label(frame, text="검색", font=("맑은 고딕", 12), bg="white")
    input_label.pack()
    widgets.append(input_label)

    search_Text = tk.Entry(frame, width=30, font=("맑은 고딕", 12))
    search_Text.pack(pady=5)
    search_Text.insert(0, text)
    widgets.append(search_Text)

    btn_frame = tk.Frame(frame, bg="white")
    btn_frame.pack(pady=5)
    widgets.append(btn_frame)

    search_btn = tk.Button(btn_frame, text="검색", width=12, 
                           command=lambda: find(search_Text.get().strip(),"book_list.csv"))
    search_btn.grid(row=0, column=0, padx=10)
    widgets.append(search_btn)

    show_ranking("book_list.csv", frame)


def find(find_novle, filename):
    file = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(file)
    find_str="F"
    for line in reader:
        if not line:
            continue
        name, view, star, stargiver, imagefile = line
        novel_obj = Novel(name, view, star, stargiver, imagefile)
        if novel_obj.name == find_novle:
            find_str="T"
            view_update(filename, find_novle)
            show_novel(filename, novel_obj)
    file.close()
    if find_str=="F":
        main_screen()


def view_update(filename, find_novle):
    novels.clear()
    sum_views = 0
    file = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(file)
    for line in reader:
        if not line:
            continue
        name, view, star, stargiver, imagefile = line
        novel_obj = Novel(name, view, star, stargiver, imagefile)
        if novel_obj.name == find_novle:
            novel_obj.view += 1
        sum_views += novel_obj.view
        novels.append(novel_obj)
    file.close()
    update(filename, sum_views)


def update(filename, sum_views):
    n = len(novels)
    for i in range(n-1):
        for j in range(n-1-i):
            g1 = (novels[j].view/sum_views)*50 + novels[j].star*10
            g2 = (novels[j+1].view/sum_views)*50 + novels[j+1].star*10
            if g1 < g2:
                novels[j], novels[j+1] = novels[j+1], novels[j]

    file = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(file)
    for obj in novels:
        writer.writerow([obj.name,obj.view,obj.star,obj.stargiver,obj.imagefile])
    file.close()


def give_star(filename, obj):
    global given_star
    clear_widgets()

    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True)
    widgets.append(frame)

    title_label = tk.Label(frame, text="⭐ 별점 주기 ⭐", font=("맑은 고딕", 20, "bold"), bg="white")
    title_label.pack(pady=20)
    widgets.append(title_label)

    now_myStar = tk.Label(frame, text=f"{given_star}", font=("맑은 고딕", 30, "bold"), bg="white")
    now_myStar.pack(pady=10)
    widgets.append(now_myStar)

    star_frame = tk.Frame(frame, bg="white")
    star_frame.pack(pady=10)
    widgets.append(star_frame)

    up_btn = tk.Button(star_frame, text="⬆", font=("맑은 고딕", 20), 
                       command=lambda: up(filename,obj))
    up_btn.grid(row=0, column=0, padx=20)
    widgets.append(up_btn)

    down_btn = tk.Button(star_frame, text="⬇", font=("맑은 고딕", 20), 
                         command=lambda: down(filename,obj))
    down_btn.grid(row=0, column=1, padx=20)
    widgets.append(down_btn)

    ok_btn = tk.Button(frame, text="확인", width=20, 
                       command=lambda: star_update(filename,obj,given_star))
    ok_btn.pack(pady=5)
    widgets.append(ok_btn)

    home_btn = tk.Button(frame, text="홈으로 가기", width=20, command=main_screen)
    home_btn.pack(pady=5)
    widgets.append(home_btn)


def up(filename,obj):
    global given_star
    if given_star < 5:
        given_star += 0.5
    give_star(filename,obj)


def down(filename,obj):
    global given_star
    if given_star > 0:
        given_star -= 0.5
    give_star(filename,obj)


def star_update(filename, obj, my_star):
    novels.clear()
    file = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(file)
    sum_views = 0
    for line in reader:
        if not line:
            continue
        name, view, star, stargiver, imagefile = line
        novel_obj = Novel(name, view, star, stargiver, imagefile)
        if novel_obj.name == obj.name:
            star_giver = float(novel_obj.stargiver) + 1
            average_star = (novel_obj.star * float(novel_obj.stargiver) + my_star) / star_giver
            average_star = round(average_star*2)/2
            novel_obj.star = average_star
            novel_obj.stargiver = star_giver
        sum_views += novel_obj.view
        novels.append(novel_obj)
    file.close()
    update(filename, sum_views)
    main_screen()


def show_novel(filename, obj):
    clear_widgets()

    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True)
    widgets.append(frame)

    # 이미지 크기 통일
    img = tk.PhotoImage(file=obj.imagefile).subsample(2, 2)
    img_label = tk.Label(frame, image=img, bg="white")
    img_label.image = img
    img_label.pack(pady=10)
    widgets.append(img_label)

    title_label = tk.Label(frame, text=obj.name, 
                           font=("맑은 고딕", 22, "bold"), bg="white")
    title_label.pack(pady=10)
    widgets.append(title_label)

    view_label = tk.Label(frame, text=f"조회수: {obj.view}", 
                          font=("맑은 고딕", 16), bg="white")
    view_label.pack(pady=5)
    widgets.append(view_label)

    star_label = tk.Label(frame, text=f"⭐ {obj.star}", 
                          font=("맑은 고딕", 16), bg="white")
    star_label.pack(pady=5)
    widgets.append(star_label)

    btn_frame = tk.Frame(frame, bg="white")
    btn_frame.pack(pady=20)
    widgets.append(btn_frame)

    home_btn = tk.Button(btn_frame, text="홈으로 가기", width=12, command=main_screen)
    home_btn.grid(row=0, column=0, padx=10)
    widgets.append(home_btn)

    star_btn = tk.Button(btn_frame, text="별점 주기", width=12, 
                         command=lambda: give_star(filename,obj))
    star_btn.grid(row=0, column=1, padx=10)
    widgets.append(star_btn)


def show_ranking(filename, frame):
    title = tk.Label(frame, text="📊 랭킹 보기", font=("맑은 고딕", 16, "bold"), bg="white")
    title.pack(pady=10)
    widgets.append(title)

    ranking_list = []
    file = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(file)
    for line in reader:
        if not line:
            continue
        name, view, star, stargiver, imagefile = line
        novel_obj = Novel(name, view, star, stargiver, imagefile)
        ranking_list.append(novel_obj.name)
    file.close()

    combo_items = [f"{i+1}위 {name}" for i, name in enumerate(ranking_list)]

    ranking_combo = ttk.Combobox(frame, values=combo_items, width=30)
    ranking_combo.pack(pady=5)
    widgets.append(ranking_combo)

    def on_select(event):
        selected_text = ranking_combo.get()
        selected_name = selected_text.split(" ",1)[1]
        find(selected_name, filename)

    ranking_combo.bind("<<ComboboxSelected>>", on_select)


main_screen()
root.mainloop()
