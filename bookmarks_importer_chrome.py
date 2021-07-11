import chrome_bookmarks
import sys
#OS	path
#Linux		~/.config/google-chrome/Default/Bookmarks
#macOS		~/Library/Application Support/Google/Chrome/Default/Bookmarks
#Windows	~\AppData\Local\Google\Chrome\User Data\Default\Bookmark

for url in chrome_bookmarks.urls:
    print(url.url, url.name)


#for folder in chrome_bookmarks.folders:
    #print(folder.name)
#file=open('bookmarks.txt','w')