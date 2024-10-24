import cv2 as cv
import matplotlib.pyplot as plt


# là thao tác xử lý điểm ảnh trên ảnh có dạng s=(L-1)-r
# trong đó s: điểm ảnh đã xử lý,
#  r:điểm ảnh ban đầu ,
# L: mức xám cực đại(trên mức thang 256)
def Anh_am_tinh(img):
    return 255-img

# biến đổi ảnh bằng hàm logarit là thao tác xử lý điểm ảnh trên ảnh có dạng:
#      s=c*log(1-r)
# s:điểm ảnh đã xử lý
# c:hằng số
# r:điểm ảnh đầu vào
def Bien_doi_Log(img,c):
    return float(c)*cv.log(1.0+img)

def show_kq():
    # định nghĩa một vùng để vẽ ảnh ra (chiều rộng =16,chiều cao =9)
    fig=plt.figure(figsize=(16,9))
    # khai báo các vùng để hiển thị ảnh
    (ax1,ax2,ax3),(ax4,ax5,ax6 )=fig.subplots(2,3)

    # lấy ảnh
    img=cv.imread('anh1.jpg',0)
    # cân bằng hist cho ảnh (kỹ thuật histogram)
    img_equalized=cv.equalizeHist(img)
    # hiển thij ảnh
    ax1.imshow(img,cmap='gray')
    # đặt tiêu đề
    ax1.set_title("anh goc")

    # ảnh âm tính
    y1=Anh_am_tinh(img)
    ax2.imshow(y1,cmap='gray')
    ax2.set_title("Ảnh âm tính")


    # ảnh âbiến đổi log
    y2=Bien_doi_Log(img,1)
    ax3.imshow(y2,cmap='gray')
    ax3.set_title("Ảnh biến đổi log")




    # vẽ híst ảnh gốc trong vùng ax6
    ax4.hist(img)
    ax4.set_title("Histogram ảnh gốc")

    # vẽ ảnh sau khi cân bằng hist trong vùng ax7
    ax5.imshow(img_equalized,cmap='gray')
    ax5.set_title("ảnh cân bằng histogram ")

    # vẽ hít của ảnh sau khi cân bằng híst trong vùng ax8
    ax6.hist(img_equalized)
    ax6.set_title("Histogram ảnh cân bằng")
    plt.show()

if __name__=="__main__":
    show_kq()