import re

class Check():
    '''手机号码验证类
    '''
    def check_mobile(self, mobile):
        '''手机号码验证
        '''
        #验证手机号
        REGEX1 = r'1(3\d|4[0,5-9]|5[0-3,5-9]|6[2,5,6,7]|7\d|8\d|9[1,8-9])\d{8}$'
        if re.match(REGEX1, mobile):
            return True
        #验证座机号
        REGEX2 = r'^0?(10|(2|3[1,5,7]|4[1,5,7]|5[1,3,5,7]|7[1,3,5,7,9]|8[1,3,7,9])[0-9]|91[0-7,9]|(43|59|85)[1-9]|39[1-8]|54[3,6]|(701|580|349|335)|54[3,6]|69[1-2]|44[0,8]|48[2,3]|46[4,7,8,9]|52[0,3,7]|42[1,7,9]|56[1-6]|63[1-5]|66[0-3,8]|72[2,4,8]|74[3-6]|76[0,2,3,5,6,8,9]|82[5-7]|88[1,3,6-8]|90[1-3,6,8,9])\d{7,8}$'
        if re.match(REGEX2, mobile):
            return True
        return False

