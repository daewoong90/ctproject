import streamlit as st
import streamlit.components.v1 as htmlviewer
# Title Msg#1
st.title('This is my Webapp!!')

with open('./index.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()

with open('./index2.html', 'r', encoding='utf-8') as f:
    html2 = f.read()
    f.close()

with open('./index3.html', 'r', encoding='utf-8') as f:
    html3 = f.read()
    f.close()

with open('./index4.html', 'r', encoding='utf-8') as f:
    html4 = f.read()
    f.close()

#     <head>
#         <title> this is my html </title>
#     </head>
#     <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#     </body>
# </html>

# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Video content'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('샘올트먼이 경고한 AI')
        st.video(url)

    with st.expander('Image Content'):
        imgfilepath = './gpt.png'
        st.image(imgfilepath)      

    with st.expander('Content #1 [CT1] 하천 하계망 분석'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html1,height=1100)

    with st.expander('Content #2 [CT2] 카페 입지 선정하기'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html2,height=900)

    with st.expander('Content #3 [AI-X] 기후경관 판독기'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html3,height=950)

    with st.expander('Bonus Content 입지 중심점 찾기'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html4,height=950)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)