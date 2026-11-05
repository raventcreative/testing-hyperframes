# Fills <!--ROLES--> in carousel.src.html with one slide per role -> carousel.html
# Text matches the original carousel (8 topics per role).
from pathlib import Path

# (name, font-size, [identity, income, ownership, mission, audience, daily work, risk, resources])
ROLES = [
    ("Founder", 120, ["<b>Starts</b> a company", "<b>Salary</b> or <b>equity</b>", "Holds <b>founding equity</b>", "Turns <b>ideas</b> into <b>reality</b>",
                      "<b>Customers</b> and <b>partners</b>", "<b>Builds</b> from scratch", "<b>Company</b> failure", "<b>Ideas</b> and <b>capital</b>"]),
    ("CEO", 120, ["<b>Leads</b> the company", "<b>Salary</b> and <b>bonuses</b>", "May own <b>nothing</b>", "Drives <b>company vision</b>",
                  "<b>Shareholders</b>", "Makes <b>decisions</b>", "<b>Leadership</b> failure", "<b>People</b> and <b>systems</b>"]),
    ("Entrepreneur", 112, ["<b>Builds</b> businesses", "<b>Venture</b> profits", "Owns <b>ventures</b>", "Finds <b>opportunities</b>",
                           "<b>Target</b> markets", "Tests <b>opportunities</b>", "<b>Venture</b> failure", "<b>Skills</b> and <b>networks</b>"]),
    ("Business Owner", 100, ["<b>Owns</b> a business", "<b>Business</b> profits", "Owns a <b>business</b>", "Builds <b>profitability</b>",
                             "<b>Paying</b> customers", "Manages <b>operations</b>", "<b>Financial</b> losses", "<b>Staff</b> and <b>inventory</b>"]),
    ("Influencer", 120, ["<b>Influences</b> an audience", "<b>Brand</b> deals", "Owns a <b>personal brand</b>", "Builds <b>audience trust</b>",
                         "<b>Followers</b>", "Creates <b>content</b>", "Losing <b>relevance</b>", "<b>Content</b> and <b>creativity</b>"]),
    ("Investor", 120, ["Puts <b>money</b> into <b>assets</b>", "<b>Investment</b> returns", "Owns <b>assets</b>", "Grows <b>wealth</b>",
                       "<b>Founders</b> and <b>markets</b>", "Evaluates <b>investments</b>", "<b>Capital</b> loss", "<b>Capital</b> and <b>research</b>"]),
]
KEYS = [("i-id", "Identity", ""), ("i-inc", "Income", ""), ("i-own", "Ownership", ""), ("i-mis", "Mission", ""), ("i-aud", "Audience", ""), ("i-work", "Daily work", ""), ("i-risk", "Risk", " risk"), ("i-res", "Resources", "")]

def slide(name, size, vals):
    cells = "".join(
        f'<div class="card{cls}"><div class="k"><svg><use href="#{ic}"/></svg>{label}</div><div class="v">{v}</div></div>'
        for (ic, label, cls), v in zip(KEYS, vals))
    return f'''<section class="slide role">
  <div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  <div class="name" style="font-size:{size}px">{name}<span>.</span></div>
  <div class="grid">{cells}</div>
  <div class="bot">Swipe →</div>
</section>
'''

d = Path(__file__).parent
src = (d / "carousel.src.html").read_text()
(d / "carousel.html").write_text(src.replace("<!--ROLES-->", "\n".join(slide(*r) for r in ROLES)))
print("ok")
