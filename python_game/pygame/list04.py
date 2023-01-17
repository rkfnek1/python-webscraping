class Human: # Hwman 클래스 정의 (부모 클래스)
    def __init__(self, name, life): # 생성자
        self.name = name # name 속성에 인수값 대입
        self.life = life # life 소성에 인수값 대입
        
    def info(self): # 속성값 출력 메서드
        print(self.name) # name 속성값 출력
        print(self.life) # life 속성값 출력

        
class Soldier(Human): # Human 클래스 상속, Soldier 클래스 정의
    def __init__(self, name, life, weapon): # 생성자
        super().__init__(name, life) # 부모 클래스 생성자 실행
        self.weapon = weapon # weapon 속성에 인수값 대입
        
    def info(self): # info() 메서드 오버라이드
        print("내 이름은 " + self.name) # 문자열과 name 속성값 출력
        print("내 체력은 {}".format(self.life)) # 문자열과 life 속성값 출력
        
    def talk(self): # Soldier 클래스의 새 메서드 정의
        print(self.weapon + "을(를) 장비하고, 모험을 시작합니다.") # 대사 출력

     
man = Human("톰(일반인)", 50) # 일반인 객체 생성
man.info() # 일반인 객체의 info() 메서드 실행
print("----------") # 출력 구분
prince = Soldier("알렉스(왕자)", 200, "빛의 검") # 기사 객체 생성
prince.info() # 기사 객체의 info() 메서드 실행
prince.talk() # 기사 객체의 talk() 메서드 실행