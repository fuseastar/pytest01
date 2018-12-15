# pytest - ordering
# 安装方式：
# 命令行
# pip3 install pytest - ordering
import pytest

"""
1.标记于被测试函数，@pytest.mark.run(order=x)
2.根据order传入的参数来解决运行顺序
3.order值全为正数或全为负数时，运行顺序：值越小，优先级越高
4.正数和负数同时存在：正数优先级高
5.正数与负数同时存在是，正数优先级高
6.被正数和没被标记     被标记高于没被标记
7.被标记负数与没被标记  没标记高于被标记负数

"""
# 需求:
#         排序输出 我的朋友是小红


class test_P:
    @pytest.mark.run(order=1)
    def test04(self):
        print("我")

    @pytest.mark.run(order=3)
    def test05(self):
        print("朋友")

    @pytest.mark.run(order=4)
    def test06(self):
        print("是")

    @pytest.mark.run(order=6)
    def test07(self):
        print("小红")

    @pytest.mark.run(order=2)
    def test08(self):
        print("的")

if __name__ == '__main__':
    pytest.main("-s test_07_执行顺序.py")

    def test09():
        print("测试自动执行")

