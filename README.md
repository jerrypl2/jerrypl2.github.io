# 何骏 / Jun He 的个人主页

这是可以直接发布到 GitHub Pages 的静态网站。文件包包含完整的中英文网页、四个项目介绍、样式和可选的内容生成脚本。

## 本版内容

- 英文开场白：Explore the unknown that was once beyond our reach.
- 中文开场白：探索过去无法触及的未知
- 中文姓名：何骏；英文姓名：Jun He
- 项目：Aethervale Academy、OpenPension、AI-native RAN、机器人学习实验
- 英文入口：`index.html`
- 中文入口：`zh/index.html`

## 最简单的发布方式：使用 GitHub 网页

### 1. 解压文件包

解压 `jun-he-homepage-github-pages.zip`。打开解压后的文件夹，应该直接看到 `index.html`、`style.css`、`favicon.svg`、`projects`、`zh`、`scripts` 和本文件。

**上传解压后的文件与文件夹。仅上传 ZIP 不会让 GitHub Pages 自动展开并发布网页。**

### 2. 创建仓库

登录自己的 GitHub 账号，点击右上角 `+` → `New repository`。

- Repository name：`你的GitHub用户名.github.io`。必须使用 GitHub 用户名，不是显示姓名。
- Visibility：`Public`。GitHub Free 的 Pages 需要公开仓库。
- 勾选 `Add README`，便于初始化分支。
- 点击 `Create repository`。

例如，用户名是 `exampleuser`，仓库名应为 `exampleuser.github.io`。

如果已经有同名仓库，先确认原有内容。也可以创建名为 `personal-homepage` 的普通仓库，使用项目站点网址 `https://你的GitHub用户名.github.io/personal-homepage/`。本网站使用相对链接，可在此类子路径下运行。

### 3. 上传文件

在仓库的 `Code` 页面选择 `Add file` → `Upload files`，把解压后文件夹里的文件和子文件夹拖入上传区域。

**关键检查：仓库首页要直接显示 `index.html`，不能再多套一层 `jun-he-homepage-github-pages/` 或 `dist/`。**

可用提交说明：`Publish personal homepage`。提交到 `main` 分支；如果账号规则要求 Pull Request，按界面提示创建并合并到 `main` 后再继续。

下面按默认分支为 `main` 说明；如果仓库的默认分支是 `master` 或其他名称，上传目标和 Pages 的 Branch 都选择那个实际分支，保持一致。

包中附带 `.nojekyll`，用于直接发布静态文件。Mac Finder 若不显示它，可按 `Command + Shift + .` 显示隐藏文件后一起上传。也可以在 GitHub 根目录用 `Add file` → `Create new file` 新建 `.nojekyll`，内容填写一行 `Static HTML site.` 后提交；GitHub 根据文件是否存在识别它。

### 4. 开启 Pages

打开仓库 `Settings` → `Pages`，在 `Build and deployment` 中设置：

| 设置项 | 选择 |
| --- | --- |
| Source | Deploy from a branch |
| Branch | main |
| Folder | /(root) |

点击 `Save`。不需要安装 Node.js、配置主题或编写 GitHub Actions 工作流。

### 5. 查看上线结果

发布可能需要最多约 10 分钟。在 `Settings` → `Pages` 中查看发布信息并点击 `Visit site`；也可在 `Actions` 查看部署任务是否成功。

个人主站的默认地址是 `https://你的GitHub用户名.github.io/`。默认英文首页的右上角可以切换中文。中文入口是网站目录下的 `zh/index.html`。如果使用 `personal-homepage` 项目仓库，中文地址应为 `https://你的GitHub用户名.github.io/personal-homepage/zh/index.html`。

使用 `github.io` 的 Pages 网站默认提供 HTTPS。可在 Pages 设置中查看 `Enforce HTTPS`。域名可以之后再绑定。

## 上线后的公开范围

使用这条免费发布路径时，仓库中的文件和 GitHub Pages 网站都会公开。当前包只包含个人主页内容与生成脚本，不包含原托管平台的部署配置、Git 历史、访问凭据或项目后台。

主页上的 Aethervale Academy 和 OpenPension 链接指向原有的访问受限站点。公开个人主页不会改变目标站点的权限。普通访客仍可能需要登录并获得授权。OpenPension 链接是使用测试资产的测试演示，其后台可能需要单独启动。

## 后续更新

### 直接编辑网页

可以在 GitHub 中编辑对应 HTML 文件并提交。发布分支更新后，Pages 会重新部署。样式在 `style.css` 中。

### 用生成脚本同时维护两种语言

编辑 `scripts/render_site.py` 里的文案，然后在解压目录执行：

```sh
python3 scripts/render_site.py
```

它会重新生成根目录和子目录中的 10 个 HTML 页面。把更新后的文件上传或通过 Git 提交即可。生成脚本不是网站运行的必要条件；重新运行会覆盖直接对 HTML 所做的修改。

## 常见问题

- **看到仓库文件，但网站尚未上线**：确认已开启 Pages，并等待部署成功。
- **出现 404**：确认发布目录为 `main` 的 `/(root)`，且根目录直接有 `index.html`。
- **没有样式**：检查 `style.css` 是否与根目录的 `index.html` 一起上传。
- **中文或项目页打不开**：检查 `zh`、`projects` 的文件夹结构是否完整保留。
- **项目演示要求登录**：这是目标项目本身的访问权限，与 GitHub Pages 个人主页是否公开是两回事。

## 官方参考

- [GitHub Pages 快速入门](https://docs.github.com/en/pages/quickstart)
- [创建 GitHub Pages 站点](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [向仓库上传文件](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [配置发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Pages 的 HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)

此包已经准备好发布，但 GitHub 仓库的创建、上传与启用 Pages 需要在你的 GitHub 账号内完成。
