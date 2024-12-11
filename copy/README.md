## Copy 應用

### 方法
利用 pop 來判斷  
1. Reference (x2 = x1) 與 Copy (x2 = x1.copy()) 之間的差異  
2. Copy (x2 = x1.copy()) 與 DeepCopy (x2 = x1.deepcopy()) 之間的差異

### 結論
1. Reference 完全與複製前的陣列是完全相同的指標，他指向複製前的陣列（所以任何元素改變都會被影響）。
2. Copy 指向複製前的陣列內的每一個元素，但若陣列1之中有另一個陣列2，則指向陣列2，並非指向陣列2內的所有元素（所以改變陣列2的內容會被影響）。
3. DeepCopy 完全與複製前的陣列不同的指標，他指向每一個元素個體（所以任何元素改變都不會被影響）。

### 上課投影片
![圖片](https://github.com/chingyen06/Computer-Programming-1/blob/main/copy/img.png)
