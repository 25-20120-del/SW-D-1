'''도서(라 쓰고 웹툰이라 읽는) 조회 및 추천 프로그램'''
import tkinter as tk
from tkinter import messagebox 
import list

# 티킨터 세팅
root = tk.Tk() 
root.title("도서 조회 및 추천 프로그램")
root.geometry("800x600")
widgets = []

#소설 클래스




novels=[]
class Novel:
    count = 0

    def __init__(self,name,view,star,genre,commentfile):
        self.name=name
        self.view=view
        self.star=star
        self.commentfile=commentfile
        main_screen()


    def show(self):
        
    
    @classmethod
    def show_count(cls):
        print(f"현재 작품 수: {cls}")



def main_screen():
    clear_widgets()
#
    title_label = tk.Label(root, text="📚 정민's 도서 ", font=("맑은 고딕", 20, "bold"))
    title_label.pack(pady=30)
    widgets.append(title_label)

    search_label = tk.Label(root, text="작품 제목을 입력하세요:")
    search_label.pack()
    widgets.append(search_label)

    search_entry = tk.Entry(root, width=30)
    search_entry.pack(pady=10)
    widgets.append(search_entry)

    search_text = tk.Text(root, text="검색", command=lambda: show_novel(search_entry.get()))
    search_text.pack(pady=5)
    widgets.append(search_text)

   ''' top5_button = tk.Button(root, text="TOP 5 보기", command=show_top5)
    top5_button.pack(pady=10)
    widgets.append(top5_button)'''


def show_novel():
    #위젯 삭제

    # 검색 결과 출력


def show_comment():
    #출력



'''def genre():'''

#위젯 삭제
def clear_widgets(self):
    for widget in widgets:
        widget.destroy()



def show_top5(filename):
    file = open(filename, "r", encoding = "utf-8-sig")
    reader = list.reader(file)
    
    header = next(reader)
    print(header)

    for line in reader:
        name,view,star,genre,commentfile = line
        novel_obj = Novel(name,view,star,genre,commentfile)
        novels.append (novel_obj)

    for m in movies:
        m.display_info()
    
    Movie.show_count
    
    file.close()

    for n in 5:
        print()
    
    

def find ():

def comment():



