import os
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#import tensorflow
import cv2
import numpy as np
import sys
import os
import tensorflow as tf
import Chapter3 as c3
import Chapter04 as c4
import Chapter05 as c5
import Chapter9 as c9
import streamlit as st
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import pandas as pd
from PIL import Image
@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img
#import ThucHanhXuLyAnh as codeChapter

st.set_page_config(page_title='Xử lý ảnh', page_icon="🎥", layout='wide')

css = """
    <style>
        div.stTitle {
            text-align: center;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)


def onOpeningClosing():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c9.OpeningClosing(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
def onOpeningClosing():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c9.OpeningClosing(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
def onNegative():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.Negative(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))



def onLogarit():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.Logarit(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        # cv2.namedWindow("ImageOut", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("ImageOut", imgout)

def onPower():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.Power(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        # cv2.namedWindow("ImageOut", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("ImageOut", imgout)

def onPiecewiseLinear():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.PiecewiseLinear(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistogram():
        global imgout
        imgout = np.zeros((imgin.shape[0], 256, 3), np.uint8) + 255
        c3.Histogram(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistogramEqualization():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        # c3.HistogramEqualization(imgin,imgout)
        cv2.equalizeHist(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onLocalHistogram():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.LocalHistogram(imgin, imgout)
        cv2.namedWindow("ImageOut", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("ImageOut", imgout)

def onHistogramStatistics():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.HistogramStatistics(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onSmoothing():
        global imgout
        imgout = c3.Smoothing(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onSmoothingGauss():
        global imgout
        imgout = c3.SmoothingGauss(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onMedianFilter():
        global imgout
        imgout = np.zeros(imgin.shape, np.uint8)
        c3.MedianFilter(imgin, imgout)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onSharpen():
        global imgout
        imgout = c3.Sharpen(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onUnSharpMasking():
        global imgout
        imgout = c3.UnSharpMasking(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onGradient():
        global imgout
        imgout = c3.Gradient(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

    #Chapter 4
        
def onSpectrum():
    global imgout
    imgout = c4.Spectrum(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onFrequencyFilter():
        global imgout
        imgout = c4.FrequencyFilter(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        

def onDrawFilter():
        global imgout
        imgout = c4.DrawNotchRejectFilter()
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onRemoveMoire():
        global imgout
        imgout = c4.RemoveMoire(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        
        
        
        
#Chapter 5

def onCreateMotionNoise():
        global imgout
        imgout = c5.CreateMotionNoise(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        

def onDenoiseMotion():
        global imgout
        imgout = c5.DenoiseMotion(imgin)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDenoisestMotion():
        global imgout
        temp = cv2.medianBlur(imgin, 7)
        imgout = c5.DenoiseMotion(temp)
        img_array = np.array(imgout)
        cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))


    #Chapter 9
def onErosion():
    global imgout
    imgout = c9.Erosion(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDilation():
    imgout = c9.Dilation(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))

def onBoundary():
    imgout = c9.Boundary(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))

def onHoleFill():
    imgout = c9.HoleFill(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))

def onMyConnectedComponent():
    imgout = c9.MyConnectedComponent(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))

def onConnectedComponent():
    imgout = c9.ConnectedComponent(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))

def onCountRice():
    imgout = c9.CountRice(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR))


selected = option_menu(
    menu_title="Image Processing", 
    menu_icon="cast",
    options=["Chapter 3", "Chapter 4","Chapter 5", "Chapter 9"], 
    icons=['person lines fill', 'laptop','sun', 'file'], 
    
    default_index=0, 
    orientation="horizontal",
    styles={
                
                "icons": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "font-family": "Arial, sans-serif",
                    "text-align": "left",
                    
                },
                "nav-link-selected": {"background-color": "orange"},"font-family": "Arial, sans-serif",
            },
            )
    




    

if selected == 'Chapter 3':
    st.title(" Biến đổi độ sáng và lọc trong không gian")
    st.markdown(css, unsafe_allow_html=True)
    col1, col2 = st.columns([0.3,0.7], gap="large")
    st.markdown("&nbsp;")
    with col1:

        option =  st.selectbox("Function", ("None", "Negative", 'Logarit', "Power", "Piecewise Linear", "Histogram", "Histogram Equalization",
                                            "Local Histogram", "Histogram Statistics", "Smoothing", "Median Filter", "Sharpen", "Un Sharp Masking",
                                            "Gradient"))
        if option == "None":
            st.write("Vui lòng chọn option!")
        else:
            st.write("")
        uploaded_file = st.file_uploader("Upload Image")
        if uploaded_file is not None:
            st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
            st.write("Tên của ảnh: ", uploaded_file.name)
            st.write("---------------------------------------------------------------")
        if option == "Negative":
            st.write("A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
            st.write("The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
        elif option == "Logarit":
            st.write("The dynamic range of an image can be compressed by replacing each pixel value with its logarithm. This has the effect that low intensity pixel values are enhanced. ")
            st.write("Applying a pixel logarithm operator to an image can be useful in applications where the dynamic range may too large to be displayed on a screen (or to be recorded on a film in the first place).")
        elif option == "Power":
            st.write("The exponential and `raise to power' operators are two anamorphosis operators which can be applied to grayscale images. Like the logarithmic transform, they are used to change the dynamic range of an image. ")
            st.write("However, in contrast to the logarithmic operator, they enhance high intensity pixel values.")
        elif option == "Piecewise Linear":
            st.write("Piece-wise Linear Transformation is type of gray level transformation that is used for image enhancement. It is a spatial domain method.")
            st.write("It is used for manipulation of an image so that the result is more suitable than the original for a specific application.")
        elif option == "Histogram":
            st.write("Histograms Introduction. In digital image processing, the histogram is used for graphical representation of a digital image.")
            st.write("A graph is a plot by the number of pixels for each tonal value. Nowadays, image histogram is present in digital cameras. Photographers use them to see the distribution of tones captured.")
        elif option == "Histogram Equalization":
            st.write("Histogram Equalization is a computer image processing technique used to improve contrast in images ")
            st.write("It accomplishes this by effectively spreading out the most frequent intensity values, i.e. stretching out the intensity range of the image.")
        elif option == "Local Histogram":
            st.write("In digital image processing, the histogram is used for graphical representation of a digital image. A graph is a plot by the number of pixels for each tonal value. ")
            st.write("Nowadays, image histogram is present in digital cameras. Photographers use them to see the distribution of tones captured.")
        elif option == "Histogram Statistics":
            st.write("An image histogram is a type of histogram that acts as a graphical representation of the tonal distribution in a digital image.")
            st.write("In an image processing context, the histogram of an image normally refers to a histogram of the pixel intensity values.")
        elif option == "Smoothing":
            st.write("Smoothing is used to reduce noise or to produce a less pixelated image. Most smoothing methods are based on low-pass filters, ")
            st.write("But you can also smooth an image using an average or median value of a group of pixels (a kernel) that moves through the image.")
        elif option == "Sharpen":
            st.write("Image sharpening is an effect applied to digital images to give them a sharper appearance. ")
            st.write("Sharpening enhances the definition of edges in an image. The dull images are those which are poor at the edges. There is not much difference in background and edges.")
        elif option == "Un Sharp Masking":
            st.write("Unsharp masking (USM) is an image sharpening technique, first implemented in darkroom photography, but now commonly used in digital image processing software.")
            st.write("Its name derives from the fact that the technique uses a blurred, or unsharp, negative image to create a mask of the original image.")
        elif option == "Gradient":
            st.write("An image gradient is a directional change in the intensity or color in an image. The gradient of the image is one of the fundamental building blocks in image processing")
            st.write("For example, the Canny edge detector uses image gradient for edge detection.")
        elif option == "Median Filter":
            st.write("The median filter is the filtering technique used for noise removal from images and signals.")
            st.write("Median filter is very crucial in the image processing field as it is well known for the preservation of edges during noise removal.")
        else:
            st.write("")

        with col2:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption='Input', use_column_width=True)
                img_array = np.array(image)
                cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
                    
                imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
            else:
                image = Image.open('nen-trang-47.jpg')
                st.image(image, caption='Input', use_column_width=True)
            if option == "Negative":
                onNegative()
            elif option == "Logarit":
                onLogarit()
            elif option == "Power":
                onPower()
            elif option == "Piecewise Linear":
                onPiecewiseLinear()
            elif option == "Histogram":
                onHistogram()
            elif option == "Histogram Equalization":
                onHistogramEqualization()
            elif option == "Local Histogram":
                onLocalHistogram()
            elif option == "Histogram Statistics":
                onHistogramStatistics()
            elif option == "Smoothing":
                onSmoothing()
            elif option == "Sharpen":
                onSharpen()
            elif option == "Un Sharp Masking":
                onUnSharpMasking()
            elif option == "Gradient":
                onGradient()
            elif option == "Median Filter":
                onMedianFilter()
            else:
                st.write("")

    with col2:
        if option == "None":
            image = Image.open('nen-trang-47.jpg')
            st.image(image, caption='Output', use_column_width=True)
        else:
            image = Image.open('out1.jpg')
            st.image(image, caption='Output', use_column_width=True)


if selected == 'Chapter 4':
    st.title("Lọc trong miền tần số")
    col1, col2 = st.columns([0.3,0.7], gap="large")
    st.markdown("&nbsp;")
    with col1:
        option = st.selectbox("Function",("None", "Spectrum", "Frequency Filter", "Draw Filter", "Remove Moire"))
        if option == "None":
            st.write("Vui lòng chọn option!")
        else:
            st.write("")
        uploaded_file = st.file_uploader("Upload Image")
        if uploaded_file is not None:
            st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
            st.write("Tên của ảnh: ", uploaded_file.name)
            st.write("---------------------------------------------------------------")
        if option == "Spectrum":
            st.write("A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
            st.write("The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
        elif option == "Frequency Filter":
            st.write("The dynamic range of an image can be compressed by replacing each pixel value with its logarithm. This has the effect that low intensity pixel values are enhanced. ")
            st.write("Applying a pixel logarithm operator to an image can be useful in applications where the dynamic range may too large to be displayed on a screen (or to be recorded on a film in the first place).")            
        elif option == "Draw Filter":
            st.write("The exponential and `raise to power' operators are two anamorphosis operators which can be applied to grayscale images. Like the logarithmic transform, they are used to change the dynamic range of an image. ")
            st.write("However, in contrast to the logarithmic operator, they enhance high intensity pixel values.")
        elif option == "Remove Moire":
            st.write("The exponential and `raise to power' operators are two anamorphosis operators which can be applied to grayscale images. Like the logarithmic transform, they are used to change the dynamic range of an image. ")
            st.write("However, in contrast to the logarithmic operator, they enhance high intensity pixel values.")
        else:
            st.write("")
        with col2:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption='Input', use_column_width=True)
                img_array = np.array(image)
                cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
                imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
            else:
                image = Image.open('nen-trang-47.jpg')
                st.image(image, caption='Input', use_column_width=True)
            if option == "Spectrum":
                onSpectrum()
            elif option == "Frequency Filter":
                onFrequencyFilter()
            elif option == "Draw Filter":
                onDrawFilter()
            elif option == "Remove Moire":
                onRemoveMoire()
            else:
                st.write("")

        with col2:
            if option == "None":
                image = Image.open('nen-trang-47.jpg')
                st.image(image, caption='Output', use_column_width=True)
            else:
                image = Image.open('out1.jpg')
                st.image(image, caption='Output', use_column_width=True)



if selected == 'Chapter 5':
    st.title("Xử lý ảnh hình thái")
    
    col1, col2 = st.columns([0.3, 0.7], gap="large")
    with col1:
        option = st.selectbox("Function", ("None", "Erosion", "Dilation", "Opening Closing", "Boundary", "HoleFill",
                                           "My Connected Component", "Connected Component", "Count Rice"))
        if option == "None":
            st.write("Vui lòng chọn option!")
        else:
            st.write("")
        uploaded_file = st.file_uploader("Upload Image")
        if uploaded_file is not None:
            st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
            st.write("Tên của ảnh: ", uploaded_file.name)
            st.write("---------------------------------------------------------------")
            image = Image.open(uploaded_file)
           
            img_array = np.array(image)
           
           
        
        
        if option == "Erosion":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
        elif option == "Dilation":
                    st.write(
                        "The dynamic range of an image can be compressed by replacing each pixel value with its logarithm. This has the effect that low intensity pixel values are enhanced. ")
                    st.write(
                        "Applying a pixel logarithm operator to an image can be useful in applications where the dynamic range may too large to be displayed on a screen (or to be recorded on a film in the first place).")
        elif option == "Opening Closing":
                    st.write(
                        "The exponential and `raise to power' operators are two anamorphosis operators which can be applied to grayscale images. Like the logarithmic transform, they are used to change the dynamic range of an image. ")
                    st.write("However, in contrast to the logarithmic operator, they enhance high intensity pixel values.")
        elif option == "Boundary":
                    st.write(
                        "Piece-wise Linear Transformation is type of gray level transformation that is used for image enhancement. It is a spatial domain method.")
                    st.write(
                        "It is used for manipulation of an image so that the result is more suitable than the original for a specific application.")
        elif option == "HoleFill":
                    st.write(
                        "Histograms Introduction. In digital image processing, the histogram is used for graphical representation of a digital image.")
                    st.write(
                        "A graph is a plot by the number of pixels for each tonal value. Nowadays, image histogram is present in digital cameras. Photographers use them to see the distribution of tones captured.")
        elif option == "My Connected Component":
                    st.write(
                        "Histogram Equalization is a computer image processing technique used to improve contrast in images ")
                    st.write(
                        "It accomplishes this by effectively spreading out the most frequent intensity values, i.e. stretching out the intensity range of the image.")
        elif option == "Connected Component":
                    st.write(
                        "In digital image processing, the histogram is used for graphical representation of a digital image. A graph is a plot by the number of pixels for each tonal value. ")
                    st.write(
                        "Nowadays, image histogram is present in digital cameras. Photographers use them to see the distribution of tones captured.")
        elif option == "Count Rice":
                    st.write(
                        "An image histogram is a type of histogram that acts as a graphical representation of the tonal distribution in a digital image.")
                    st.write(
                        "In an image processing context, the histogram of an image normally refers to a histogram of the pixel intensity values.")
        else:
                    st.write("")
    with col2:
        if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    st.image(image, caption='Input', use_column_width=True)
                    img_array = np.array(image)
                    cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
                    imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
        else:
                    image = Image.open('nen-trang-47.jpg')
                    st.image(image, caption='Input', use_column_width=True)
        if option == "Erosion":
            onErosion()
        elif option == "Dilation":
            onDilation()
        elif option == "Opening Closing":
            onOpeningClosing()
        elif option == "Boundary":
                    onBoundary()
        elif option == "HoleFill":
                    onHoleFill()
        elif option == "My Connected Component":
                    onMyConnectedComponent()
        elif option == "Connected Component":
                    onConnectedComponent()
        elif option == "Count Rice":
                    onCountRice()
        else:
                    st.write("")
    with col2:
        if option == "None":
                    image = Image.open('nen-trang-47.jpg')
                    st.image(image, caption='Output', use_column_width=True)
        else:
                    image = Image.open('out1.jpg')
                    st.image(image, caption='Output', use_column_width=True)
    
    
    
if selected == 'Chapter 9':
    st.title("Khôi phục ảnh")
    col1, col2 = st.columns([0.3,0.7], gap="large")
    st.markdown("&nbsp;")
    with col1:
        option = st.selectbox("Function",("None", "CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"))
        if option == "None":
            st.write("Vui lòng chọn option!")
        else:
            st.write("")
        uploaded_file = st.file_uploader("Upload Image")
        if uploaded_file is not None:
            st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
            st.write("Tên của ảnh: ", uploaded_file.name)
            st.write("---------------------------------------------------------------")
            
        if option == "CreateMotionNoise":
            st.write("A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
            st.write("The appearance change from lightest to darkest and darkest to lightest is basically done in a grayscale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")

        elif option == "DenoiseMotion":
            st.write("The dynamic range of an image can be compressed by replacing each pixel value with its logarithm. This has the effect that low-intensity pixel values are enhanced.")
            st.write("Applying a pixel logarithm operator to an image can be useful in applications where the dynamic range may be too large to be displayed on a screen or to be recorded on film in the first place.")

        elif option == "DenoisestMotion":
            st.write("The exponential and 'raise to power' operators are two anamorphosis operators that can be applied to grayscale images. Like the logarithmic transform, they are used to change the dynamic range of an image.")
            st.write("However, in contrast to the logarithmic operator, they enhance high-intensity pixel values.")

        else:
            st.write("")
        with col2:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption='Input', use_column_width=True)
                img_array = np.array(image)
                cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
                imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
            else:
                image = Image.open('nen-trang-47.jpg')
                st.image(image, caption='Input', use_column_width=True)
            if option == "CreateMotionNoise":
                onCreateMotionNoise()
            elif option == "DenoiseMotion":
                onDenoiseMotion()
            elif option == "DenoisestMotion":
                onDenoisestMotion()

            else:
                st.write("")

        with col2:
            if option == "None":
                image = Image.open('nen-trang-47.jpg')
                st.image(image, caption='Output', use_column_width=True)
            else:
                image = Image.open('out1.jpg')
                st.image(image, caption='Output', use_column_width=True)



