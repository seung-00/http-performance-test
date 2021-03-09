# Server Performance Test

> 경희대학교 캡스톤 수업에서 진행한 프로젝트입니다.

현재 서버 개발에 다양한 언어들이 쓰이고 있다. 또한 MSA(Micro Service Architectural)와 컨테이너 기술의 확산으로 서버 구축에 있어서도 선택지가 늘었다. 본 과제는 서버 개발에 사용되는 언어들과 인프라 환경별 성능 평가를 실시하여 서버 구축에 도움될 정량적인 정보를 제공하도록 한다.
<br/>
<br/>
## Stacks

- Node.js, Python, Go

- Linux, Docker, vmware

## Methods

1. 언어별, 환경별로 서버를 구축한다.

   - 언어는 node(js), python go를 사용한다.
   - 환경은 native(Linux), vm(vmware), container(docker) 를 사용한다.

2. 클라이언트 코드를 작성한다.

3. 서버별 TPS와 CPU, Memory usage를 측정한다.

   이때 두 가지 시나리오가 존재한다.

   1. 클라이언트의 GET 메서드에 서버는 json 파일을 읽어 response 로 전달한다.
   2. 클라이언트의 GET 메서드에 서버는 MySQL Query 를 실행해 결과를 response 로 전달한다.

4. 평가된 데이터들을 시각화한다.

## Results

1. 클라이언트

   - 1초당 requset를 1회부터 200회까지 늘려가면서 측정
   - 언어, 환경에 따른 다양한 조건에서 코드를 재사용할 수 있도록 작성

2. 서버

   - vmware 사용, host os 아래 virtual machine 두 개를 두어 데이터베이스 서버와 http api 서버 분리
   - docker-compose로 데이터베이스 서버와 http api 서버 분리
   - top 명령어로 3초 간격으로 100회 cpu, memory usage log를 남기도록 스크립트 작성

3. 구조

   <img width="852" alt="스크린샷 2020-12-28 오후 10 55 53" src="https://user-images.githubusercontent.com/46865281/103231893-5376d080-497c-11eb-8d12-7eb806279d0e.png">

4. 그래프

   - **TPS**

     <img width="720" alt="스크린샷 2020-12-28 오후 10 57 48" src="https://user-images.githubusercontent.com/46865281/103231974-95a01200-497c-11eb-9ba3-61177d0d369b.png">

   - **CPU usage**

     <img width="720" alt="스크린샷 2020-12-28 오후 10 57 56" src="https://user-images.githubusercontent.com/46865281/103231977-989b0280-497c-11eb-9ae6-1eff0e940336.png">

   - **Memory usage**

     <img width="720" alt="스크린샷 2020-12-28 오후 10 58 07" src="https://user-images.githubusercontent.com/46865281/103231979-9afd5c80-497c-11eb-97d7-3d14c102205c.png">

## Conclusion

**TPS**

1. native > container > vm
2. go ≧ javascript > python

**memory usage**

1. vm (28%) > container (19%) > native (18%)
2. 언어별 차이는 없었음

**cpu usage**

1. native > container > vm
2. python > javascript > go

