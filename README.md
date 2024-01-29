## 해시 요청 api
> 평문을 전송하면 암호화된 정보를 제공

### url
* POST encrypt/hash
  * ex> http://localhost:8080/encrypt/hash

* request
  * 파라미터

| 파라미터 명 | 데이터 타입 | 필수 여부 | 설명 |
|---|---|---|---|
| algorithm | String | O | 암호화 알고리즘 |
| salt | String | X | 해시 솔트 |
| text | String | O | 암호화 시킬 데이터 |


  ```
	{
		"algorithm": "sha1",
		"salt": "abc",
		"text": "Test Data!!!"

	}
  ```



* response
  * header 파라미터

  | 파라미터 명     | 데이터 타입  | 필수 여부 |      설명       | 
  |---|---|---|---| 
  | isSuccess    | String    |    O    | 성공 여부        | 
  | errorCode    | Numeric   |    O    | 에러 코드        | 
  | errorMessage | String    |    O    | 에러 메시지      | 

	* encrypt 파라미터

  | 파라미터 명 | 데이터 타입  |  필수 여부 |      설명       | 
  |---|---|---|---| 
  | algorithm | String    |    O    | 암호화 알로리즘    | 
  | encData   | String    |    O    | 암호화 된 데이터   | 
 
  ```
	{
		"header" : {
			"isSuccess" : true,
		  "errorCode": 0,
		  "errorMessage" : ""
		},
		"encrypt" : {
			"algorithm" : "sha1",
			"encData" : "qweasderqwrawwad"
		}
	}
  ```