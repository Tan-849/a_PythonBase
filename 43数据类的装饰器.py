import dataclasses


@dataclasses.dataclass
class Girl:
    # def __init__(self):
    #     self.name = "刘亦菲"
    #     self.age = 18
    age: int = 19

    def show(self):
        print("演员开始拍摄仙剑奇侠传")

    def show2(self):
        print("演员开始拍摄仙剑奇侠传")
        print(f"我的年龄是{self.age}")

    @classmethod
    def show3(cls):
        print("演员开始拍摄仙剑奇侠传")
        print(f"我的年龄是{cls.age}")


girl = Girl(20)  # 当创建对象时，传递实参过去那么实参会进行覆盖属性值
print(girl.age)
girl.show2()
print(girl.age)
girl.show3()
