import streamlit as st
#postgresql과 python을 연동하기 위한 라이브러리
import psycopg2 

def exec_db(command):
    #postgresql과 연결
    #데이터베이스와 통신할 수 있도록 설정을 입력
    conn = psycopg2.connect(
        #ip주소 == 내 데이터베이스의 위치
        #ip주소 == 260.32.(pc마다 다름)
        host='localhost',
        
        #데이터베이스의 이름, 권한이 있는 사용자의 이름, 비밀번호
        dbname='postgres',
        user='postgres',
        password=5449,
        port=5432
    )

#'연결'을 생성

    cursor = conn.cursor()
    cursor.execute(command)

    #fetchall() : 모든 데이터를 가져와 rows에 담아줌
    rows = cursor.fetchall()

    #데이터를 담을 리스트 생성
    #인쇄하여 결과를 확인하기 위함
    result = []
    for row in rows:
        result.append(row)

    #print(result)

    #데이터베이스와의 연결을 끊음 (필요한 것만 가져오고 끊기 위해)
    cursor.close()
    conn.close()

    return result

    #streamlit을 실행
st.write('DB Connector')

command = st.text_input('Input SQL Command')

if command:
    re = exec_db(command)

    st.divider()
    st.write("DB RESULT IS .... :")
    st.text(re)