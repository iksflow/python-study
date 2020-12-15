# from packtest.sound import * - __all__에 정의된 모듈만 애스터리스크(*)의 대상으로 처리한다.
# echo2는 대상이 아니므로 호출 시 오류가 발생하게 된다.
__all__ = ['echo']