# Fills <!--ROLES--> in carousel.src.html with one slide per role -> carousel.html
# Text matches the original carousel (Audience / Daily Work / Risk / Resources).
from pathlib import Path

# (name, font-size, [audience, daily work, risk, resources])
ROLES = [
    ("Founder", 132, ["<b>Customers</b> and <b>partners</b>", "<b>Builds</b> from scratch",
                      "<b>Company</b> failure", "<b>Ideas</b> and <b>capital</b>"]),
    ("CEO", 132, ["<b>Shareholders</b>", "Makes <b>decisions</b>",
                  "<b>Leadership</b> failure", "<b>People</b> and <b>systems</b>"]),
    ("Entrepreneur", 118, ["<b>Target</b> markets", "Tests <b>opportunities</b>",
                           "<b>Venture</b> failure", "<b>Skills</b> and <b>networks</b>"]),
    ("Business Owner", 104, ["<b>Paying</b> customers", "Manages <b>operations</b>",
                             "<b>Financial</b> losses", "<b>Staff</b> and <b>inventory</b>"]),
    ("Influencer", 132, ["<b>Followers</b>", "Creates <b>content</b>",
                         "Losing <b>relevance</b>", "<b>Content</b> and <b>creativity</b>"]),
    ("Investor", 132, ["<b>Founders</b> and <b>markets</b>", "Evaluates <b>investments</b>",
                       "<b>Capital</b> loss", "<b>Capital</b> and <b>research</b>"]),
]
KEYS = [("i-aud", "Audience", ""), ("i-work", "Daily work", ""), ("i-risk", "Risk", " risk"), ("i-res", "Resources", "")]

def slide(name, size, vals):
    cells = "".join(
        f'<div class="card{cls}"><div class="k"><svg><use href="#{ic}"/></svg>{label}</div><div class="v">{v}</div></div>'
        for (ic, label, cls), v in zip(KEYS, vals))
    return f'''<section class="slide role">
  <div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  <span class="tag">The role</span>
  <div class="name" style="font-size:{size}px">{name}<span>.</span></div>
  <div class="grid">{cells}</div>
  <div class="bot">Swipe →</div>
</section>
'''

d = Path(__file__).parent
src = (d / "carousel.src.html").read_text()
(d / "carousel.html").write_text(src.replace("<!--ROLES-->", "\n".join(slide(*r) for r in ROLES)))
print("ok")
