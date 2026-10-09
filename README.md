# Hao Li（李昊）的个人主页

基于 [al-folio v1.2](https://github.com/alshedivat/al-folio/releases/tag/v1.2) 的 Jekyll 网站。
正式域名为 <https://haolis.com>，仓库继续使用 `aquatoney/aquatoney.github.io`。

## 本次迁移

- 重构分支：`rebuild/al-folio`。
- 旧版基线：`pre-al-folio-2026-10-05`，对应提交 `e17e076`。
- 已迁入个人简介、照片、招生信息、联系方式、53 篇论文及原有 20 篇精选标记。
- 保留 `/pubs/`、48 份 `/files/` PDF、原有图片地址、域名和 Google 验证文件。
- 首页采用简洁的个人介绍、招生信息和 News；全部论文集中在 Publications，People 展示在读博士生和硕士生，Alumni 暂时留空。
- Jekyll 自动生成 `sitemap.xml`；根目录 `robots.txt` 明确指向 `https://haolis.com/sitemap.xml`。
- GitHub Pages 使用 GitHub Actions 发布：推送到 `master` 后先构建检查，再自动部署到 <https://haolis.com>；重构分支和 PR 只验证构建。

## 本地预览

需要 Ruby 3.4、Bundler 4，以及 Node.js 20 或更高版本。

```sh
bundle install
npm ci
bundle exec jekyll serve --config _config.yml,_config.local.yml
```

打开 <http://localhost:4000>。修改 `_config.yml` 后需重启预览。

本机已准备独立的 Ruby 和 Node.js 运行环境，可直接执行 `./bin/preview` 启动预览。

也可通过 Docker 运行同一套内容：

```sh
docker compose up --build
```

## 日常维护

| 内容                         | 文件                       |
| ---------------------------- | -------------------------- |
| 首页与个人资料               | `_pages/about.md`          |
| 全部论文、精选标记及资源链接 | `_bibliography/papers.bib` |
| 论文页与固定地址             | `_pages/publications.md`   |
| 联系方式与社交链接           | `_data/socials.yml`        |
| 网站、主题与插件配置         | `_config.yml`              |
| 论文附件                     | `files/`                   |

新增论文使用 BibTeX 格式，作者以 `and` 分隔。保留原有 `selected` 标记，但首页不再展示精选论文。
`pdf = {https://haolis.com/files/文件名.pdf}` 指向现有附件目录；没有可用文件时不填写 `pdf`。
`corresponding`、`ccf`、`xjtu` 保留原网站元数据。通讯作者以姓名旁的星号表示，CCF A/B/C 以徽章显示。
奖项使用 `award`、`award_name` 和 `award_url` 字段，REAL 已标注 NSDI 2026 Community Award。

首页 News 放在 `_news/`，日期依据记录在 `docs/news-sources.md`。People 页面在 `_pages/people.md`，中英文学生名单在 `_data/people.yml`。
视觉微调位于 `_sass/_site.scss`，有意覆盖的模板已通过 al-folio 升级工具登记。

以下五篇论文的 PDF 原仓库尚未提供，迁移后隐藏下载按钮，并以 `legacy_file` 保留预期文件名：

- `occamy-tc26-shan.pdf`
- `veriboost-fm26-kang.pdf`
- `accessrefinery-fse26-kang.pdf`
- `real-nsdi26-xia.pdf`
- `nanopl-nsdi26-dang.pdf`

## 构建检查

```sh
npm run lint:prettier
bundle exec al-folio upgrade audit --no-fail
JEKYLL_ENV=production bundle exec jekyll build
python3 bin/check-site.py _site
```

主题功能来自版本锁定的 Ruby 插件。升级时检查 `Gemfile` 与 `Gemfile.lock`，运行上述检查并预览页面。
模板代码遵循根目录 `LICENSE` 中的 MIT 许可；论文及个人资料保留各自权利。
