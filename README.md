# simple-microservice-study
> Django-Flask-MYSQL-RabbitMQ를 사용한 간단한 마이크로서비스 구현 학습 코드입니다.
  <br>
* 온라인 주문 백엔드를 모티브로 작성하였습니다. 
  <br>
* 마이크로서비스 구현 이해가 목표이기에 프론트엔드는 생략하였습니다.


## Description

> 2022.05.진행
### Architecture

<img src=images/micro_architecture.png  width="60%"/>


  
  <br>

### Summary

* User_order(고객-Django)에서 고객주문과 Boss(가게 사장님-flask)의 백엔드 MYSQL을 각각 독립적으로 분리
* Internal API를 통해 각 DB의 초기값 세팅 및 테스트 by insomnia
* RabbitMQ를 사용한 상호 DB data의 consistency 유지

  

  

  <br>

  <br>

  


***

