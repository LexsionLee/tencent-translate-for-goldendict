# tencent-translate-for-goldendict

Add tencent-translate for GoldenDict

本项目通过Python编程实现一个简单的程序，接受 GoldenDict 文本调用腾讯机器翻译，为其实现整句翻译。GoldenDict是一款社区维护的免费翻译工具软件，支持外挂各种词典，功能强大但不支持整句翻译。腾讯机器翻译（TMT）是腾讯云提供的一个商用翻译API，功能强大，著名的腾讯翻译君官网上表示其使用的就是TMT API。以上此处不再赘述。

笔者初学者，对Python的总学习时长不超过5小时。目前笔者只实现了英语翻译为中文，且代码有问题在所难免，大佬们勿喷。如果有大佬愿意，可以帮忙为此项目添砖加瓦。

## Todo：

- [x] 实现简单的命令行参数调用
- [ ] BUG：遇到类似“®™”的文本，会报错退出
- [ ] 实现其他语言翻译
- [ ] 用HTML输出，让翻译结果更美观

## 使用方法：

因为腾讯TMT的API免费额度有限制，所以API需要自行申请。整个配置分为申请翻译API和部署Python程序两大步。

### 申请翻译API：

目前腾讯机器翻译每月提供5百万字符的免费文本翻译额度，一般的非翻译工作者，这个量应该足够了。只需要开通机器翻译免费账户，到达月免费限额会自动中断服务，不会扣费。当然，你也可以升级付费账号，超出免费额度后付费使用。

1. 首先我们需要打开 [腾讯云](https://curl.qcloud.com/8DaYN3oj) 官网并登录，没有可先点击页面右上角注册账号，登录后需要在右上角的菜单中进行个人实名认证。

   > 以上的腾讯云官网链接包含笔者个人的腾讯云CPS推广。使用推广链接不会对您有影响，仅当您购买付费服务可能给我带来收益，介意者可以自行搜索腾讯云官网链接。谢谢！

2. 注册后点击[机器翻译 TMT页面](https://curl.qcloud.com/8DaYN3oj)上的**立即使用**按钮，会跳转到机器翻译的服务控制台。

3. 在控制台**勾选** *我已阅读···* ，然后点击免费试用，按提示免费开通机器翻译服务。为避免超出免费额度后被收费，首次开通建议选择试用版，若以后发现免费版不够用，可以随时改付费版。

4. 开通后，鼠标放在网页右上角头像上，在弹出的菜单中点击**访问管理**，然后在**左侧菜单**选择**访问密钥** --> **API 密钥管理**，进入之后会有一个弹窗提示。

5. 弹窗的内容是告诉你，在目前界面创建的密钥可以调用账号里的所有腾讯云资源，为保险起见，建议创建一个子账号，然后只给这个子账号分配需要的服务对应权限，最后使用子账号创建密钥，这样更安全。

6. 此时有两种方法：
   * 一种是忽略提示，点击 **继续使用** ，然后点击 **新建密钥** 按钮，表格里就会添加新的密钥，能看到**Secretld和SecretKey**。这样操作简单，但一旦泄露风险较大。
   * 另一种操作繁琐一些，但更安全。点击 **切换使用子账号密钥** ，会跳转到[新建用户](https://console.cloud.tencent.com/cam/user/userType)页面。点击[自定义创建](https://console.cloud.tencent.com/cam/user/create)，选择 **可访问资源并接收消息** ，然后点击 **下一步** 。新的页面中**设置用户信息**：填写用户名，备注可填写 “ 机器翻译接口-GoldenDict ” 。**访问方式：**只勾选**编程访问**。其他不必填写，完成后点击下一步。新的页面中搜索“ 机器翻译 ”，勾选 **QcloudTMTFullAccess（机器翻译（TMT）全读写访问权限）** 即可，然后点击**下一步**。最后的页面用于审阅之前几步填写的信息，确认无误后点击 **完成 ** 即可。此时就会看到这个子账户的 **SecretId和SecretKey**。
   
7. 完成上面操作后，保持页面，等待下面部署 Python 程序阶段使用 **SecretId**和**SecretKey**。

### 部署Python程序：

安装 Python3.3.6 以上，到官网下载，装的时候注意勾上pip和PATH。

安装腾讯云 SDK：

```
pip install --upgrade tencentcloud-sdk-python
```

中国大陆地区的用户可以使用国内镜像源提高下载速度，例如：

```
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
```

去GitHub下载**TencentTrans.py** 和 **favicon.ico**两个文件，随手丢在合适的地方。目录不要太深，注意不要有空格。

文本编辑器打开 **TencentTrans.py** ，修改以下两行中的内容为上一大步中申请的ID和KEY。

```
SecretId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SecretKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

GoldenDict 中点击 **编辑** --> **词书** ，在 **来源** 选项卡中选择 **程序** 选项卡。点击 **添加** 按钮，类型选择 **纯文本** ，名称填写 **`腾讯翻译君`** ，命令行填写 `python 文件路径\TencentTran.py %GDWORD%` ，图标填写 `文件路径\favicon.ico` 。

以上的路径要使用 绝对路径，类似于这样格式 `python C:\GoldenDict\XXX\Python.py` ,  `C:\GoldenDict\XXX\favicon.ico`。

填写完成后将前面的已启用打勾，点击确定按钮完成配置。这样就可以使用啦！

## 参考资料：

* [Python基础教程](https://www.runoob.com/python/python-tutorial.html)
* [腾讯云API中心](https://cloud.tencent.com/document/api)
* [腾讯云SDK中心](https://cloud.tencent.com/document/sdk/Python)
* [google-translate-for-goldendict](https://github.com/xinebf/google-translate-for-goldendict)
* [ argparse 模块官方文档](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse)

