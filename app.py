import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# [필수] st.set_page_config는 최상단에 위치합니다.
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="춘향전 어휘 탐구 학습지",
    layout="wide"
)

# 기본 스타일 설정
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #7f8c8d;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📜 춘향전 단어 찾아 쓰기 학습지</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">중학교 2학년 국어 | 본문을 읽고 뜻풀이에 맞는 알맞은 단어를 써봅시다.</div>', unsafe_allow_html=True)

# 27개 어휘 데이터
vocab_data = [
    {"번호": 1, "단어": "임기", "뜻풀이": "임무를 맡아 보는 일정한 기간"},
    {"번호": 2, "단어": "부임하다", "뜻풀이": "임명이나 발령을 받아 근무할 곳으로 가다."},
    {"번호": 3, "단어": "암행어사", "뜻풀이": "조선 시대에, 임금의 특명을 받아 지방관의 일을 탐문하고 백성의 어려움을 살펴서 개선하는 일을 맡아 하던 임시 벼슬."},
    {"번호": 4, "단어": "수령", "뜻풀이": "조선 시대에, 각 고을을 맡아 다스리던 지방관들을 통틀어 이르는 말."},
    {"번호": 5, "단어": "걸인", "뜻풀이": "남에게 구걸하여 얻어먹고 사는 사람."},
    {"번호": 6, "단어": "다담상", "뜻풀이": "손님을 대접하기 위하여 내놓은 차와 과자 등을 차린 상."},
    {"번호": 7, "단어": "개다리소반", "뜻풀이": "상다리 모양이 개의 다리처럼 휘었으며, 되는대로 마구 만들어 질이 낮은 자그마한 밥상."},
    {"번호": 8, "단어": "선선히", "뜻풀이": "성질이나 태도가 쾌활하고 시원스럽게."},
    {"번호": 9, "단어": "역졸", "뜻풀이": "예전에, 관청에 나가서 나랏일을 맡아보는 사람이 부리던 하인."},
    {"번호": 10, "단어": "어출두", "뜻풀이": "'어사출두'의 줄임말. 조선 시대에, 암행어사가 지방 관아에 중요한 사건을 처리하기 위하여 출근하여 일을 시작함."},
    {"번호": 11, "단어": "외올망건", "뜻풀이": "여러 겹이 아닌 단 하나의 올로 뜬 망건. 상투를 튼 사람이 머리카락을 거두어 올려 흘러내리지 아니하도록 머리에 두르는 그물처럼 생긴 물건."},
    {"번호": 12, "단어": "갓싸개", "뜻풀이": "갓의 겉을 바르는 몹시 얇고 사이가 촘촘하지 않고 조금 듬성듬성한 베."},
    {"번호": 13, "단어": "패랭이", "뜻풀이": "대를 쪼개 가늘게 깎은 긴 조각을 엮어 만든 갓. 조선 시대에는 역졸, 보부상 같은 신분이 낮은 사람이 씀."},
    {"번호": 14, "단어": "육모 방망이", "뜻풀이": "역졸·포졸들이 쓰던 여섯모가 진 방망이."},
    {"번호": 15, "단어": "마패", "뜻풀이": "벼슬아치가 공무로 지방에 나갈 때 역마를 모아 거두는 증표로 쓰던 등글구리 패."},
    {"번호": 16, "단어": "유밀과", "뜻풀이": "밀가루나 쌀가루 반죽을 적당한 모양으로 빚어 바싹 말린 후에 기름에 튀기어 꿀이나 조청을 바르고 튀밥, 깨 등을 입힌 과자."},
    {"번호": 17, "단어": "병부", "뜻풀이": "조선 시대에, 군대를 동원하는 표지로 쓰던 등글납작한 나무패."},
    {"번호": 18, "단어": "탕건", "뜻풀이": "벼슬아치가 갓 아래 받쳐 쓰던 관의 하나."},
    {"번호": 19, "단어": "용수", "뜻풀이": "싸리나 대오리로 만든 둥글고 긴 통. 술이나 장을 거르는 데 쓴다."},
    {"번호": 20, "단어": "멍석 구멍에 생쥐 눈 뜨듯", "뜻풀이": "겁이 나서 몸을 숨기고 바깥을 살피는 모양을 비유적으로 이르는 말."},
    {"번호": 21, "단어": "객사", "뜻풀이": "고려·조선 시대에, 각 고을에 설치하여 외국 사신이나 다른 곳에서 온 벼슬아치를 대접하고 묵게 하던 숙소."},
    {"번호": 22, "단어": "수절", "뜻풀이": "정절을 지킴."},
    {"번호": 23, "단어": "분부", "뜻풀이": "윗사람이 아랫사람에게 명령이나 지시를 내림. 또는 그 명령이나 지시."},
    {"번호": 24, "단어": "낭군", "뜻풀이": "예전에, 젊은 여자가 자기 남편이나 연인을 부르던 말."},
    {"번호": 25, "단어": "오얏", "뜻풀이": "자두."},
    {"번호": 26, "단어": "정렬부인", "뜻풀이": "조선 시대에, 정조와 지조를 굳게 지킨 부인에게 내리던 칭호."},
    {"번호": 27, "단어": "하직하다", "뜻풀이": "서울을 떠나는 벼슬아치가 임금에게 작별을 아뢰다."}
]

# 사용자의 입력값을 저장하기 위한 세션 상태
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# 바로 빈칸 퀴즈 화면 띄우기
st.subheader("✍️ 뜻풀이를 읽고 알맞은 단어를 빈칸에 작성하세요.")
st.write("---")

with st.form(key="quiz_form"):
    for item in vocab_data:
        idx = item["번호"]
        meaning = item["뜻풀이"]
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{idx}.** {meaning}")
        with col2:
            st.session_state.user_answers[idx] = st.text_input(
                f"입력_{idx}", 
                key=f"input_{idx}", 
                label_visibility="collapsed",
                placeholder="단어 입력"
            )
        st.divider()
    
    submit_btn = st.form_submit_button(label="💯 정답 제출 및 채점하기")

# 채점 결과 출력
if submit_btn:
    score = 0
    total = len(vocab_data)
    
    for item in vocab_data:
        idx = item["번호"]
        correct = item["단어"].strip()
        user_input = st.session_state.user_answers.get(idx, "").strip()
        if user_input == correct:
            score += 1
            
    st.success(f"🎉 채점 완료! 내 점수: {score} / {total} 점")
    
    results = []
    for item in vocab_data:
        idx = item["번호"]
        correct = item["단어"]
        user_input = st.session_state.user_answers.get(idx, "").strip()
        status = "✅ 정답" if user_input == correct else f"❌ 오답 (정답: {correct})"
        results.append({
            "번호": idx,
            "뜻풀이": item["뜻풀이"],
            "내가 작성한 답": user_input if user_input else "(미입력)",
            "결과": status
        })
        
    st.subheader("📋 상세 채점 내역")
    st.table(pd.DataFrame(results))
