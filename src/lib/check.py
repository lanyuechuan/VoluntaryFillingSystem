import re

class CheckTelephone():
    '''电话号码验证类
    '''
    def check(self, telephone):
        '''电话号码验证
        '''
        #验证手机号
        REGEX1 = r'1(3\d|4[0,5-9]|5[0-3,5-9]|6[2,5,6,7]|7\d|8\d|9[1,8-9])\d{8}$'
        if re.match(REGEX1, telephone):
            return True
        #验证座机号
        REGEX2 = r'^0?(10|(2|3[1,5,7]|4[1,5,7]|5[1,3,5,7]|7[1,3,5,7,9]|8[1,3,7,9])[0-9]|91[0-7,9]|(43|59|85)[1-9]|39[1-8]|54[3,6]|(701|580|349|335)|54[3,6]|69[1-2]|44[0,8]|48[2,3]|46[4,7,8,9]|52[0,3,7]|42[1,7,9]|56[1-6]|63[1-5]|66[0-3,8]|72[2,4,8]|74[3-6]|76[0,2,3,5,6,8,9]|82[5-7]|88[1,3,6-8]|90[1-3,6,8,9])\d{7,8}$'
        if re.match(REGEX2, telephone):
            return True
        return False

class CheckIdentifyNo():
    '''验证身份证合法性
    '''
    # t代表身份证号码的位数，w表示每一位的加权因子
    t = []
    w = []
    for i in range(0, 18):
        t1 = i + 1
        t.append(t1)
        w1 = (2 ** (t1-1)) % 11
        w.append(w1)
    #队列w要做一个反序
    w = w[::-1]

    def for_check(self, n):
        '''根据前17位的余数，计算第18位校验位的值
        '''
        # t = 0
        for i in range(0, 12):
            if (n + i) % 11 == 1:
                t = i % 11
        if t == 10:
            t = 'X'
        return t

    def for_mod(self, identify_no):
        '''根据身份证的前17位，求和取余，返回余数
        '''
        total = 0
        try:
            for i in range(0, 17):
                total += int(identify_no[i]) * int(self.w[i])
            total = total % 11
        except:
            pass
        return total

    def check(self, identify_no):
        '''验证身份证有效性
        '''
        if identify_no[-1] == 'X':
            if self.for_check(self.for_mod(identify_no[:-1])) == 'X':
                return True
            else:
                return False
        else:
            if self.for_check(self.for_mod(identify_no[:-1])) == int(identify_no[-1]):
                return True
            else:
                return False