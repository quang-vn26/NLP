## Bài tập tuần 2:

Nội dung: Thu thập dữ liệu từ trang web, thực hiện các bước tiền xử lý (Pre-processing) và đếm tần số xuất hiện của mỗi từ.

Các bước cụ thể:
    1. Chọn một bài viết (tiếng Anh) trên vnexpress (bài có bình luận). Ví dụ: https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html

    2. Thu thập nội dung của bài viết trên trang web bằng Python (Chỉ lấy tag chứa bài viết) và các bình luận (nội dung bình luận, thời gian bình luận, tên người bình luận)
Hướng dẫn: (Đọc thêm ở đây https://www.nltk.org/book/ch03.html)
Sử dụng thư viện: BeautifulSoup
>>> from bs4 import BeautifulSoup
>>> getHTML = BeautifulSoup(html, 'html.parser')
>>> getdivX = getHTML.find(“div”, {“id”: “abc”}) → Lấy div có ID
>>> getdivY = getHTML.find(“div”, {“class”: “abc”}) → Lấy div có class
>>> getdivS = getHTML.find_all(“div”, {“class”:”xyz”}) → Lấy tất cả thẻ div có class=xyz
>>> Lặp: for d in getdivS: print(d.text)...

    3. Xóa bỏ các Tag HTML
>>> getdivX.text()) để lấy phần text (bỏ các tag HTML)
>>> import re
>>> txt = re.sub('<a.*?>|</a> ', ' ', getdivX) → Thay thế các thẻ liên kết (<a…> và </a>) bằng một chuỗi khác hoặc bằng ‘ ’ để xóa

    4. Lowercasting, xóa stop-words, xóa các ký tự phân cách - remove punctuation (, . / ( ) + * ? ! …), kiểm tra chính tả...
    5. Nhận dạng ngôn ngữ của bài viết là gì (Tiếng Anh/Tiếng Việt)
    6. Tách các từ và hiển thị Danh sách các từ
    word_tokenize...
    7. Đếm số lần xuất hiện của các từ/Tần suất xuất hiện
    >>> s.count("python") #Đếm số từ “python” xuất hiện trong s
    >>> len(s) #Đếm số từ có trong s
    8. Sử dụng các kỹ thuật Stemming + Lemmatization để lấy danh sách các từ gốc. So sánh kết quả của 2 kỹ thuật này.
    9. Lưu nội dung của Bài báo và Danh sách các bình luận vào 1 file trên máy tính
>>> f = open('mytext.txt', "w") #a: append; w: write
>>> f.write('abc')
>>> f.close()
>>
>>10. Từ nội dung bài báo, hãy tách thành các câu.

