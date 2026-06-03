# Domain Admin

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/domain-admin)](https://pypi.org/project/domain-admin)
[![PyPI](https://img.shields.io/pypi/v/domain-admin.svg)](https://pypi.org/project/domain-admin)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/domain-admin?label=pypi%20downloads)](https://pypi.org/project/domain-admin)
[![PyPI - License](https://img.shields.io/pypi/l/domain-admin)](https://github.com/0psong/domain-admin/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/0psong/domain-admin)](https://github.com/0psong/domain-admin/releases)
[![GitHub Stars](https://img.shields.io/github/stars/0psong/domain-admin?color=%231890FF&style=flat-square)](https://github.com/0psong/domain-admin)


![](https://raw.githubusercontent.com/0psong/domain-admin/master/image/domain.svg)

基于Python + Vue3.js 技术栈实现的域名和SSL证书监测平台

用于解决，不同业务域名SSL证书，申请自不同的平台，到期后不能及时收到通知，导致线上访问异常，被老板责骂的问题

Domain Admin是一个轻量级监控方案，占用系统资源较少。同时，Domain Admin也可以作为一个Flask 和 Vue.js前后端分离的项目模板

- 项目优势
    - 集中管理: 提供一个统一的平台来管理多个域名，极大地提高了管理效率。
    - 自动提醒: 支持域名到期提醒，帮助用户避免因域名过期导致的服务中断。
    - 开源灵活: 作为开源项目，用户可以根据自身需求进行定制和扩展。
    - 社区支持: 拥有活跃的社区，可以获得持续的更新和问题支持。
    - 用户友好: 界面简洁直观，容易上手。

- 功能描述
    - 核心功能：`域名`、`SSL证书` 和 `托管证书文件` 的过期监控，到期提醒
    - 支持证书：单域名证书、多域名证书、泛域名（通配符）证书、IP证书、自签名证书
    - 证书部署：单一主机部署、多主机部署、动态主机部署
    - 通知渠道：支持邮件、Webhook、企业微信、钉钉、飞书等通知方式
    - 支持平台：macOS、Linux、Windows
    - 辅助功能：`Let’s Encrypt` SSL证书免费申请和SSL证书自动续期
    - 多语言：支持中文、英文

- 项目地址：[后端代码（GitHub）](https://github.com/0psong/domain-admin)

- 发布渠道：[PyPI](https://pypi.org/project/domain-admin)、[Releases](https://github.com/0psong/domain-admin/releases)

- 接口文档：[GitHub](https://0psong.github.io/domain-admin/)

## 安装

建议自行部署，这样比较安全。常见安装方式：

| 安装方式 | 说明 |
| --- | --- |
| Docker | 推荐用于服务器部署 |
| 源码 | 适合二次开发和本地调试 |
| pip | 适合快速安装 Python 包 |



## 项目截图

账号密码随意（例如：admin/123456），预览模式仅提供模拟数据，无法操作修改

1、网页版：

![](https://raw.githubusercontent.com/0psong/domain-admin/master/image/dashboard.png)

![](https://raw.githubusercontent.com/0psong/domain-admin/master/image/screencapture.png)

本项目采用的是前后端分离模式，前端代码在另外一个仓库。

2、移动端版：

<img src="https://raw.githubusercontent.com/0psong/domain-admin/master/image/screencapture-mini.png" width="220">

## 问题反馈交流

请通过当前项目仓库提交 Issue 或 Pull Request：

- Issues: [https://github.com/0psong/domain-admin/issues](https://github.com/0psong/domain-admin/issues)
- Pull Requests: [https://github.com/0psong/domain-admin/pulls](https://github.com/0psong/domain-admin/pulls)

## 更新日志

[CHANGELOG.md](CHANGELOG.md)

[![Stargazers over time](https://starchart.cc/0psong/domain-admin.svg)](https://starchart.cc/0psong/domain-admin)
