# -*- coding: utf-8 -*-
"""导出 book/ 全书为单个 HTML + PDF。"""
import subprocess, pathlib, sys

BOOK = pathlib.Path(r"E:\Dropbox\TimeSeries\book")

ORDER = [
    "第00章-写作与审阅规范.md",
    "第01章-时间序列是什么.md",
    "第02章-拆解时间序列.md",
    "第03章-随机性与分布.md",
    "第04章-平稳性与白噪声.md",
    "第05章-自相关与频域.md",
    "第06章-平滑与指数平滑.md",
    "第07章-AR与MA模型.md",
    "第08章-ARIMA与BoxJenkins.md",
    "第09章-状态空间与卡尔曼滤波.md",
    "第10章-ARCH与GARCH.md",
    "第11章-VAR协整与误差修正.md",
    "第12章-马尔可夫机制转换.md",
    "第13章-机器学习视角.md",
    "第14章-RNN与LSTM与TCN.md",
    "第15章-Transformer与长序列预测.md",
    "第16章-概率与生成式预测.md",
    "第17章-时间序列基础模型.md",
    "第18章-大语言模型与时间序列.md",
    "第19章-评估因果与可解释性.md",
    "第20章-端到端案例.md",
    "第21章-全书回顾.md",
    "附录A-术语表.md",
    "附录B-工具速查.md",
    "附录C-符号表.md",
]

CSS = """<style>
:root { --accent: #2c5f8a; }
* { box-sizing: border-box; }
body { font-family: "Microsoft YaHei","PingFang SC","Noto Sans CJK SC",sans-serif;
       font-size: 16px; line-height: 1.75; color: #222;
       max-width: 920px; margin: 0 auto; padding: 24px 32px 80px; }
h1 { font-size: 26px; border-bottom: 3px solid var(--accent); padding-bottom: 8px;
     margin-top: 48px; color: var(--accent); }
h1:first-of-type { margin-top: 0; }
h2 { font-size: 21px; margin-top: 32px; border-left: 5px solid var(--accent);
     padding-left: 10px; color: #333; }
h3 { font-size: 18px; margin-top: 24px; color: #444; }
p { margin: 10px 0; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: 14px 0; font-size: 15px; }
th, td { border: 1px solid #ccc; padding: 7px 10px; text-align: left; }
th { background: #eef3f8; }
tr:nth-child(even) td { background: #fafafa; }
code { font-family: Consolas,"Courier New",monospace; background: #f5f5f5;
       padding: 1px 5px; border-radius: 3px; font-size: 0.92em; }
pre { background: #f7f7f7; border: 1px solid #ddd; border-left: 4px solid var(--accent);
      padding: 12px 14px; overflow-x: auto; border-radius: 4px; }
pre code { background: none; padding: 0; }
blockquote { margin: 12px 0; padding: 8px 16px; background: #f2f7fb;
             border-left: 4px solid var(--accent); color: #333; }
blockquote p { margin: 4px 0; }
ul, ol { padding-left: 26px; }
li { margin: 4px 0; }
nav#TOC { background: #f8f9fa; border: 1px solid #ddd; padding: 14px 20px; margin-bottom: 20px; }
nav#TOC ul { list-style: none; padding-left: 18px; }
nav#TOC > ul { padding-left: 0; }
hr { border: none; border-top: 1px dashed #bbb; margin: 30px 0; }
@media print {
  body { font-size: 12pt; max-width: none; padding: 0; }
  h1, h2, h3 { page-break-after: avoid; }
  pre, blockquote, table { page-break-inside: avoid; }
  nav#TOC { page-break-after: always; }
}
</style>"""

header = BOOK / "_export_header.html"
header.write_text(CSS, encoding="utf-8")

out_html = BOOK / "time-series-analysis-book.html"
cmd = ["pandoc", "--standalone", "--embed-resources", "--toc", "--toc-depth=2",
       "--resource-path", str(BOOK),
       "--metadata", "title=时间序列分析：从零基础到前沿（全书 · 21 章 + 3 附录 · 含插图）",
       "--include-in-header", str(header), "--from", "markdown+smart",
       *[str(BOOK / f) for f in ORDER], "-o", str(out_html)]
print(">> pandoc 合并渲染…")
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("PANDOC FAILED:\n", r.stderr); sys.exit(1)
print("HTML OK:", out_html.name, f"{out_html.stat().st_size/1024:.0f} KB")

out_pdf = BOOK / "time-series-analysis-book.pdf"
url = out_html.resolve().as_uri()
# 注意：Edge headless 打印不渲染 base64 内嵌图片，必须用 Chrome
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
print(">> Chrome 无头打印 PDF…")
r = subprocess.run([chrome, "--headless", "--disable-gpu",
                    "--user-data-dir", str(BOOK / "_chrome_profile"),
                    "--no-pdf-header-footer", "--print-to-pdf", str(out_pdf), url],
                   capture_output=True, text=True, timeout=600)
if out_pdf.exists():
    print("PDF OK:", out_pdf.name, f"{out_pdf.stat().st_size/1024:.0f} KB")
else:
    print("PDF FAILED:\n", r.stdout, r.stderr)
