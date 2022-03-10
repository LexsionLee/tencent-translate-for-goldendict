# -*- coding: utf-8 -*-

"""
Get translate from Tencent Translate
use Tencent Cloud SDK.
Author:Lexsion
Created on 2022-03-09 08:43:00
USAGE:
python3 TencentTrans.py <Text>
python TencentTrans.py Good good study,day day up!
"""

# 腾讯云API 3.0 Explorer自动生成的一堆import，我不会Python，不知道有啥用，也不敢动。
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

# 我感觉、大概是，argparse 用于命令行选项、参数和子命令解析器，textwrap 用于格式化文本换行填充。
import argparse
import textwrap

# SecretId & SecretKey 必须改成你自己申请的！
# 如何获取？参考：https://lexsion.com/index.php/archives/252/
# SecretId & SecretKey MUST CHANGE TO YOURSELF!
# For how to get? refer to: https://lexsion.com/index.php/archives/252/
SecretId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SecretKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 用于获取调用时传入的参数。
def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Get translate from Tencent Translate use Tencent Cloud SDK.
            It can translate English to Chinese.
            ----------------------------------------------------------------
            
            Note:
            Currently, the functionality of the program is simple,
            It can only be used to translate English to Chinese.
            There are no optional parameters other than the required parameters,
            A "-" sign on the parameter Text's front is prohibited!

            Please replace the SecretId & SecretKey by yours before first use!
            It can be applied for free from Tencent Cloud.
            For how to get the SecretId & SecretKey,Please refer to:
            https://lexsion.com/index.php/archives/252/
            '''))
    parser.add_argument('qText',metavar='Text', type=str, default='', help='Original text for query.')
    return parser.parse_args()

# 主程序开始的地方
try:
    cred = credential.Credential(SecretId, SecretKey)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tmt.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile)

    req = models.TextTranslateRequest()
    params = {
        "SourceText": " ",
        "Source": "en",
        "Target": "zh",
        "ProjectId": 0
    }

    # 引入原文
    args = get_args()
    params['SourceText'] = args.qText
    req.from_json_string(json.dumps(params))

    # 调用SDK的翻译接口
    resp = client.TextTranslate(req)
    # print(resp.to_json_string())
    dictResp = (resp.__dict__)

    # 打印输出原文和译文
    print("原文：",params['SourceText'])
    print(' ')
    print("译文：\n",dictResp['TargetText'])
    print(' ')

# 异常处理
except TencentCloudSDKException as err:
    print(err)