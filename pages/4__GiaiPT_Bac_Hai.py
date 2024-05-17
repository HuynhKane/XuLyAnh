import streamlit as st
import math

st.set_page_config( page_title='Giải phương trình bậc 2', page_icon="🔢", layout='centered')
st.sidebar.title('Giải phương trình bậc 2')

def gptb2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = 'Phương trình có vô số nghiệm'
            else:
                ket_qua = 'Phương trình vô nghiệm'
        else:
            x = -c/b
            ket_qua = 'Phương trình có một nghiệm  %.2f' % x
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            ket_qua = 'Phương trình vô nghiệm'
        if delta == 0:
            x1 = -b /(2*a)
            ket_qua = 'Phương trình có nghiệm duy nhất x = %.f' %x1; 
        if delta > 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            ket_qua = 'Phương trình có nghiệm x1 = %.f và x2 = %.f' % (x1, x2)
    return ket_qua


def clear_input():
    st.session_state["_a"] = 0
    st.session_state["_b"] = 0
    st.session_state["_c"] = 0

def main():
    #st.subheader('Giải phương trình bậc 2 có dạng: ')
    #st.title('a*x² + b*x + c = 0')

    # Thêm mã JavaScript vào trang web
        

        with st.form(key='columns_in_form', clear_on_submit=False):
            a = st.number_input('Nhập a', key='_a', format="%g", step=1.0)
            b = st.number_input('Nhập b', key='_b', format="%g", step=1.0)
            c = st.number_input('Nhập c', key='_c', format="%g", step=1.0)

            c1, c2 = st.columns(2)
            with c2:
                btn_giai = st.form_submit_button('Giải phương trình')

            with c1:
                
                btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)

        if btn_giai:
            s = gptb2(a, b, c)
            st.markdown( typePT(a,b,c))

            st.markdown('Kết quả: ' + s)
        else:
            st.markdown('Kết quả:')
        
    
    
def typePT(a, b, c):
    result = "Phương trình có dạng: " + str(a) + "x² "
    if b < 0:
        result += str(b) + "x"
    else:
        result += " + " + str(b) + "x " 
    if c < 0:
        result += str(c)
    else:
        result += " + " + str(c)
    
    result += " = 0 "
    return result
if __name__ == "__main__":
    main()