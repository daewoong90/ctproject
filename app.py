import streamlit as st
import streamlit.components.v1 as htmlviewer
# Title Msg#1
st.title('AI project Webapp!!')

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()
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
    with st.expander('Content #1 AI 유튜브'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('샘온트먼이 경고한 AI')
        st.video(url)

    with st.expander('Content #2 기후변화 예측 시뮬레이션'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html,height=1000)

    with st.expander('Image Content'):
        imgfilepath = './gpt.png'
        st.info('')
        st.image(imgfilepath)        

    with st.expander('Content #2 기후변화 예측 시뮬레이션'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html,height=1000)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

    with st.expander('Tips..'):
        st.info('Tips..')

    with st.expander('Tips..'):
        st.info('Tips..')

    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)