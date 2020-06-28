#低加密指数广播攻击
#加密的是同一个m

from gmpy2 import *
from Crypto.Util.number import *
from functools import reduce


def CRT(items):
    N = reduce(lambda x, y: x * y, (i[1] for i in items))
    result = 0
    for a, n in items:
        m = N // n
        d, r, s = gcdext(n, m)
        if d != 1:
            raise Exception("Input not pairwise co-prime")
        result += a * s * m
    return result % N, N


# e, n, c
e = 0x5
n = [0x8365D1FF23709FAAEF6330AECA9C848B292E0872C5C41E8CBE9D0780F32EBFC5FCC7947BD666F06AA619F952AFB8D7C08B9211960D1916235D8AB3A60DEC45B1EF5CC21848E56D5235717186EAD51AE22A5661BDFDC42E31F9181F6AB1D070FDEBB078A9980D7A0571B587130A1D3056CBA40CBBA287CD5031838BAB893B476B,
    0x9288E1EEF599EA72113D950723A8FC0ADD096C7312D8E78911FE64A4322C4FEC96FD70B345AA5A345481FB91D8549998A90E2429DCAF1EEEC863F396479A0BBD121E36B0EFAC8D002FC95B58B5879DD75251B5CEFCBE90BF50669742821BE2E89B3831FD6F0F3EAB310E5BF3FC66D702D5FF1581EE1DEFF161EFCA359063C6AB,
    0x808B8F96E7255B3F169EE854ABE0CD0AC7A4AE1B388CBC9A234E225842208A435842C254A55855B867F3FCA78E3887C8D1663B501A5D4D5E32F3EF84847F45651A5E2FC8A091E12E2B4DB7AB41113D258E2200FFB2BBF8B7C38B0049B3E2E60C65EB8B6375F03A40DC9F9AB01FEC60E09DC8CA3644A83738BDA0CFDB2B5ABB3D,
    0x811F75BEAD6F0C3EA1560CFA4BFD4762F1DA3A30E22644AB16B1BEA5A6A1AF14F0C3C2E63865FD29241246C1473892232DAB6224AF1600F73340CBCA7BF5AF01EA1FA007E46064CE2F8DD92A9E7FA9F16CFEEE5A6CF67683BCD97F1E7E1BA73A9F86A8E4D7496393AC9727D10530A76B03B3A23321E8BDD756FCE265494F6D35,
    0x8178408D7E1155B9F5B0665A3EDFE279189567AAC333CA33A7304AE1BB9C9A921735888FB7BC9B41550817B1C0D42B2AB0304546709648F45147180AD5FC839FB8F90B2D30772718A7B45E6204CE7886122874759F93C198CE61D10555F03C13FD83E639A637D849C846D5589029533E567E12FD992D690EC5EF38569327FC8D]

c = [0x76CBCAF659936784799208C3EE2420B7BBFDBB9AA8D7C89874C11314DF5DECD3AA97F3DA89851A043AF16E6570E7D03A4F3225D49E552FAA2FB9F6A19AE95BA73ECD6E7CC05CD9C03E03E06F829042DBA4C1A91F39AC0CAD516C8DE7FB45939A2038C24C13F7F62A20040473D8F3D8339A4B30A65715F98A43CC3293E51190D5,
    0x246F3344F2C341FDA293ECB4214C14D57164CB37FB364ED14B2FE3D10C94D2365155959B481085379A9C85B9FCB86C7E3676B2BFD98DF7055D7E474CFEE6CE3529980A3FA0C537AF9C375E606E89B19D34FC801200DB462538E2E9FE80803A8EF02F662D0E5AC9C35DCE7A758B9EFD6D5FEA73BD9649C9B651E5AA5F1D96A773,
    0x3F312B5FDA3A9AA43DE2697FA001EE909DFE677AA6A48BEAF84991FF7D423596B5CC230DB4E5BE42E7C886E1FA6B39002B148F670C3B162816EFCC6341A96D3CDCF849A35B866EFB9E5F5C48DF9BBD3F065FFA3E0961EB2393C6F2689B72603B21A2E1C674EE2A1A6534CA01F5606B062FB53CA9C3EB1BEC80AC6849B090A7EF,
    0x224CD570EAF4D650AA24D51127E1657D201C8483AA690D48D58CA56AE86EA517DF43F9F130CC7CA75C8868623BA145189E2D16326A82A437516530D130161552D016ADB2D8746DC92D30F2A4D90A50A63AF038B0449CF2A3442BA6696B6485A46D47545591AADB1C68E901745D4F9231627C9E0C0A52CC7439CC45B21AE51AEE,
    0x210B2C8CA031259D2EF22A2561B23B794B3740382BD0A89EF7DB9E62463C8649EF5983EB94CFF6F0D6A1881A0D4E190EF8A1ACC20DA5DA71AE31705A5501B6856C151449DFC76B7026A9FAB74AA4B41C7F58ECCDC35777866C117D3BE1E37A4576E34C90DF7B8146F1BDF841D1362287A4922CB9A80221EC165E48F0BFFD4EDE]

data = list(zip(c, n))
x, n = CRT(data)
M = iroot(mpz(x), e)[0].digits()
m = long_to_bytes(M)
print(m)
# m = t is a f