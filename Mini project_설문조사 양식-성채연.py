<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="X-UA-Compatible" content="IE=edge">
    <title>문서 기본 구조</title>
</head>
<body>
    <header>
        <h1>설문조사 양식</h1>
        <p>모든 항목에 빠짐없이 체크해주십시오.</p>
    </header>
    <hr>
    <main>
        <form>
            <fieldset>
                <legend>개인정보</legend>
                <label for="name">이름</label>
                <input type="text" id="name" 
                placeholder="본명을 입력하세요."
                name="name">
                <br>
                <label for="email">이메일</label>
                <input type="text" id="email"
                placeholder="이메일을 입력하세요."
                name="email">
            </fieldset>
            <fieldset>
                <legend>설문</legend>

                <p>연령대가 어떻게 되십니까?</p>
                <input type="radio" id="teen" name="age">
                <label for="teen">10대</label>
                <input type="radio" id="twenty" name="age">
                <label for="twenty">20대</label>
                <input type="radio" id="thirty" name="age">
                <label for="thirty">30대</label>
                <input type="radio" id="fourty" name="age">
                <label for="fourty">40대</label>
                <input type="radio" id="fifty" name="age">
                <label for="fifty">50대</label>
                <input type="radio" id="other" name="age">
                <label for="other">그 외</label>

                <p>학원을 선택할 때 가장 중요하게 생각하는 것을 모두 고르시오.</p>
                <input type="checkbox" id="position" name="academy">
                <label for="position">위치</label>
                <input type="checkbox" id="price" name="academy">
                <label for="price">학원비</label>
                <input type="checkbox" id="teacher" name="academy">
                <label for="teacher">강사</label>
                <input type="checkbox" id="infra" name="academy">
                <label for="infra">시설</label>

                <p>학원에 오기 위해 이용하는 이동수단을 모두 고르시오.</p>
                <input type="checkbox" id="car"
                name="transportation">
                <label for="car">자동차</label>
                <input type="checkbox" id="bus"
                name="transportation">
                <label for="bus">버스</label>
                <input type="checkbox" id="bicycle"
                name="transportation">
                <label for="bicycle">자전거</label>
                <input type="checkbox" id="taxi"
                name="transportation">
                <label for="taxi">택시</label>
                <input type="checkbox" id="subway"
                name="transportation">
                <label for="subway">지하철</label>


            </fieldset>
            <fieldset>
                <legend>기타 의견</legend>
                <textarea cols="40" rows="3" name="comment"></textarea>
            </fieldset>
            <input type="submit">
        </form>
    </main>
    <hr>
    <footer>
    <p>입력하느라 수고하셨습니다.</p>
    </footer>
</body>
</html>