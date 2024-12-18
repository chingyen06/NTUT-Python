35. 理想大學  
  
已知有多間學校，且每間學校都會有自己特殊的屬性，學生們希望可以透過輸入自己想要的屬性，來篩選自己想要的學校，請寫一個程式來幫助學生們解決這個問題。  
  
每一大學可以擁有的 8 種屬性:  
GF(Good Food) :代表附近有美食。  
BC(Big Campus):代表有大校園。  
NC(Next to City):代表鄰近有大城市。  
CT(Convenient Transportation):代表交通方便。  
NS(Next to Sea):代表靠海。  
NM(Next to Mountain):代表依山。  
HL(Has Lake):代表校園有湖。  
NL(Near Landscape):代表附近有風景區。  
  
【輸入說明】  
第一行：輸入整數N (3 <= N <= 5)，代表總共有N間學校  
第二~N+1行：每行輸入學校名稱以及該學校擁有的屬性，學校名稱、每個屬性  
                         間以一個空白隔開。  
第N+2行：輸入整數M (1 <= M <= 4)，代表有幾組想要的屬性  
第N+3~N+M+3行：每一行有一組查詢。查詢條件為校園屬性組成,每個校園屬  
                                  性為 2 個字元。用 + 號區格的條件代表"或" 的關係,沒有 +  
                                  區隔的條件代表 "且" 的關係。  
                                  屬性間及 + 之間有 1 個空白間隔。例如: BC NS + CT HL 代  
                                  表需找出【大校園且靠海】,或【交通方便且校園有湖】的  
                                  所有大學名稱。  
                                  其格式如下:  
                                  XX YY + AA BB  
                                  意思為屬性條件為: XX 且 YY,或是 AA 且 BB。  
第N+M+4行：輸入整數b (0 <= b <= 1)，決定輸出的方式  
  
範例輸入說明:  
3 (總共有5間學校)  
NSYSU NC CT NS NM (學校名稱為NSYSU，擁有的屬性為NC、CT、NS、NM)  
NTU BC NC CT NS (學校名稱為NTU，擁有的屬性為BC、NC、CT、NS)  
NCCU BC NL HL (學校名稱為NCCU，擁有的屬性為BC、NL、HL)  
2 (總共有2組查詢)  
BC NS + CT HL (有大校園且靠海 或 交通方便且校園有湖)  
BC + NS (有大校園 或 靠海)  
0 (輸出以當b=0時候的方式輸出)  
  
【輸出說明】  
根據每一組的查詢數性條件，各自輸出符合的大學名稱  
  
輸出格式：  
當b=0時,代表輸出能符合條件的大學。例如:條件 NS BC NC + CT HL,大學名稱及屬性為NTUT NC BC NS ,則 NTUT 符合條件。假如大學名稱及屬性為NTU CT，則NTU不符合條件，此外如果有多間學校符合，則依學校輸入順序輸出，中間以空白隔開。  
  
當b=1時,代表輸出部分符合且符合最多條件的大學(不需要整組屬性相同，即學生們要求的條件可以拆開來看)。例如:條件 NS BC NC + CT HL,大學名稱及屬性為 NTUT BC NS(符合兩種屬性)、 NTUST BC(符合一種屬性),則輸出NTUT。此外如果符合度最高的學校同時有2間以上，則依學校輸入順序輸出，中間以空白隔開。  
  
範例輸出說明 :  
NTU (符合第一組查詢條件的BC NS，符合有大校園且靠海的屬性條件)  
NSYSU NTU NCCU (NSYSU符合第二組查詢條件的NS(靠海)，NTU符合第二組  
                                     查詢條件的BC(有大校園)，NCCU符合第二組查詢條件的  
                                     BC(有大校園))  
  
【特殊要求】  
請使用 dictionary 儲存資料並完成此題目  
  
【測試資料一】  
輸入：  
5  
NSYSU NC CT NS NM  
NTU BC NC CT NS  
NCCU BC NL HL  
Providence BC NC  
NTHU BC NS  
2  
BC NS + CT HL  
NM + BC NL + BC NC  
0  
  
輸出：  
NTU NTHU  
NSYSU NTU NCCU Providence  
  
【測試資料二】  
輸入：  
3  
NTHU GF HL  
NCTU NM GF BC  
NCKU CT GF NS  
3  
HL + BC NL + CT BC  
NM HL + CT + GF NS  
NM  
0  
  
輸出：  
NTHU  
NCKU  
NCTU  
  
  
  
  
【測試資料三】  
輸入：  
4  
NCU CT NM  
NUU BC GF NL NM CT  
NTOU GF NL NM  
NTNU HL NC  
2  
BC  
HL BC + NS GF + NL + NM  
1  
  
輸出：  
NUU  
NUU  
  
【測試資料四】  
輸入：  
3  
NTUE CT NM HL NC  
NHCUE NS  
NTCU NS NC  
3  
NS + BC HL  
CT  
BC GF NC NS NL  
1  
  
輸出：  
NTUE NHCUE NTCU  
NTUE  
NTCU  
  
【隱藏測試資料一】  
輸入：  
3  
NCUE GF NL NM  
NSYSU NS  
NCCU CT BC NM HL NC  
2  
HL NL + CT BC + NM GF  
NL + NL CT HL  
0  
  
輸出：  
NCUE NCCU  
NCUE  
  
  
  
【隱藏測試資料二】  
輸入：  
4  
CCU CT NS GF  
NCNU NS  
NTPU NL HL NM BC  
NUK BC NC NL HL  
3  
NS + CT HL  
HL  
GF NS + NL HL + NM  
0  
  
輸出：  
CCU NCNU  
NTPU NUK  
CCU NTPU NUK  
  
【隱藏測試資料三】  
輸入：  
5  
NQU CT GF HL NL NM  
NTUA HL NL  
TNUA CT NM NL GF NC  
TNNUA BC NL GF  
PCCU NL NM  
2  
GF NM CT  
GF NS + NL  
1  
  
輸出：  
NQU TNUA  
NQU TNUA TNNUA  
  
【隱藏測試資料四】  
輸入：  
3  
FJU NL HL GF NM BC CT  
SCU NM NC CT NS  
USC NS GF NL BC  
4  
NC  
NM NL CT BC HL NS  
NS GF  
NC GF BC  
1  
  
  
  
輸出：  
SCU  
FJU  
USC  
FJU USC  
