# reading_test
스마트폰으로 글읽기 실험

- 스크롤로 넘기기
- 페이지로 넘기기

---

## 사용한 라이브러리

- Flask
	- <http://flask.pocoo.org/>
- Boostrap
	- <http://getbootstrap.com/>
- Swipe
	- <https://github.com/thebird/Swipe>


---

## 테이블 생성 쿼리 정리

```
CREATE TABLE `real_answer` (
  `question` varchar(10) NOT NULL,
  `answer` int(10) NOT NULL
) DEFAULT CHARSET=utf8;

CREATE TABLE `answer_log` (
  `uuid` varchar(40) NOT NULL,
  `exp_id` varchar(10) NOT NULL,
  `test_type` varchar(10) NOT NULL,
  `question` varchar(10) NOT NULL,
  `answer_value` int(10) NOT NULL,
  `is_real_test` char(1) NOT NULL
) DEFAULT CHARSET=utf8;

CREATE TABLE `time_log` (
  `uuid` varchar(40) NOT NULL,
  `exp_id` varchar(10) NOT NULL,
  `test_type` varchar(10) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `is_real_test` char(1) NOT NULL
) DEFAULT CHARSET=utf8;
```