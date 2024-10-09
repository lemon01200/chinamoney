# from lzx
import re


def reg_search(text, regex_list):
    """
    自定义正则匹配函数
    :param text:需要正则匹配的文本内容
    :param regex_list:需要正则匹配的文本内容
    :return:
    """
    # 存储最终的结果
    results = []

    # 遍历每个正则表达式字典
    for regex_dict in regex_list:
        result_dict = {}

        # 遍历字典中的每个项
        for key, value in regex_dict.items():
            # 自定义正则表达式来匹配股票代码
            matches = re.findall(value, text)
            result_dict[key] = matches if matches else None

        # 存储
        results.append(result_dict)

    return results


if __name__ == '__main__':
    text = '''
    标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
    有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
    换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
    之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
    日至 2027 年 6 月 1 日止。
    '''

    # 正则表达式列表
    regex_list = [{
        '标的证券': r'股票代码：(\d{6}\.\w{2})',
        '换股期限': r'(\d{4} 年 \d{1,2} 月 \d{1,2})'
    }]

    # 调用函数
    result = reg_search(text, regex_list)

    # 输出结果
    print(result)

