class date(object):
    def __init__(self, year, month, day):
        # 私有属性
        self.__year = year
        self.__month = month
        self.__day = day

    # 将类方法object.year()转变成类属性object.year, 只是让代码更加简洁而已。
    @property
    def year(self):
        return self.__year


today = date(2021, 2, 27)
print(today.year)
