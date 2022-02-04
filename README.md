# investment-analysis

AI 주식 분석

서비스 카테고리: 분석 자료 제공 / 토론방 운영

서비스 설명: 인공지능을 이용해 과거 주식 자료를 통해 미래 동향을 예측하여 주식 매매에 도움을 주는 서비스 제공
            주식 토론방을 통한 주식 정보 획득

로그인 / 회원가입
  > 아이디(e-mail) / 비밀번호
  > 아이디(e-mail) / 비밀번호1 / 비밀번호2, 증권사 정보

주식 분석
  > 1. 주식 데이터 크롤링
  > 2. 케라스를 통한 주식 분석 자료 제공
  > 3. 결과 및 예측 자료 제공

토론방
  > 질문/답변식의 기본 토론방

front area: https://bootswatch.com/flatly/ 테마
  > 로그인) id: e-mail 형식(중복 불가), pw: 영문숫자 8글자 이상 16글자 미만의 password, nickname: 2 이상 8 이하 영문 한글 숫자(중복 불가)
  > 회원가입) id: e-mail 형식, pw1: 영문숫자 8글자 이상 16글자 미만의 password, pw2: pw1과 같은지 확인, 증권사 정보(증권사 이용률 분석), nickname: 2~8 영문 한글 숫자(중복 불가)
  
  > 주식분석) 입력창: input type(str) 주식 종목 > (table) 시가, 종가, 등락률 등의 정보 / (image) 미래 예측 그래프 / (input) 결과 및 예측 정보, 과거 조회 정보 확인
  > 추가 예정 기능: 예측 기간 선택, 분석 모델 선택, 즐겨찾기 기능

  > 토론방) 인기순 추천순 분류, 글쓰기 기능, 답글 기능, 좋아요 기능, 검색(내용 / nickname) 기능, 삭제 / 수정 기능, 사진 첨부 기능, 종목 표시 기능, 네이버 지식인과 유사하게
  > 추가 예정 기능: 내가 쓴 글 확인

  > 출처/ 권한) 데이터 정보 출처 / 모델 정보를 맹신하지 말라는 문구

back area
  > 크롤링: 야후 주식 데이터 크롤링

  > 모델: 케라스 > 순환신경망 > train /test > 미래자료 추출 > 분석 자료 및 신뢰구간 도출
  > DB: 추출한 자료를 id별로 저장

  > 토론방 DB: question_id를 통한 질문/답변 구분, 종목 표시, 사진, 글 입력, 인기순 추천순 분류, 검색 기능