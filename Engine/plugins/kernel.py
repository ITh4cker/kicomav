# -*- coding:utf-8 -*-
# Made by Kei Choi(hanul93@naver.com)

# 악성코드 상태값
NOT_FOUND = 0 # 악성코드 찾지 못함
INFECTED  = 1 # 감염
SUSPECT   = 2 # 의심
WARNING   = 3 # 경고

#---------------------------------------------------------------------
# KavMain 클래스
# 키콤백신 엔진 모듈임을 나타내는 클래스이다.
# 이 클래스가 없으면 백신 엔진 커널 모듈에서 로딩하지 않는다.
#---------------------------------------------------------------------
class KavMain :
    #-----------------------------------------------------------------
    # init(self)
    # 백신 엔진 모듈의 초기화 작업을 수행한다.
    #-----------------------------------------------------------------
    def init(self) :
        return 0
