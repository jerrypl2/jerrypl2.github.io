from pathlib import Path
from html import escape as esc

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT
ACADEMY = 'https://personal-university-first-light.hejun-alvin.chatgpt.site'
OPENPENSION = 'https://openpension-private-test.hejun-alvin.chatgpt.site'

CONTENT = {
 'en': {
  'lang':'en', 'name':'Jun He', 'opening':'Explore the <em>unknown</em> that was once beyond our reach.', 'caption':'A personal notebook', 'nav':['About','Interests','Projects','Writing','Contact'],
  'skip':'Skip to content', 'hero_label':'Notes on intelligence, learning & possibility',
  'subtitle':'Exploring intelligence, learning, and what we can build together.', 'explore':'Explore the projects',
  'about_kicker':'01 / ABOUT', 'about_title':'A little about me',
  'about':[
   'My background is in wireless communications and product management. I am now exploring how intelligent systems learn, adapt, and work with people over time.',
   'My interests connect AI-native radio networks, personal learning systems, and robotics. Through Aethervale Academy and hands-on experiments, I am working toward a better understanding of how ideas become useful systems—and how building those systems can change the way we learn and think.'
  ],
  'trail':['Wireless communications','Intelligent systems','Learning by building'],
  'interests_kicker':'02 / INTERESTS', 'interests_title':'Questions that<br>keep me curious',
  'interests':[
   ('Human–AI co-development','How people and AI systems can understand one another, adapt together, and learn through sustained interaction.'),
   ('Learning from experience','How intelligent systems can turn experience into knowledge, better decisions, and new capabilities.'),
   ('AI-native radio networks','How learning-based methods can improve radio resource management while remaining measurable, reliable, and practical.'),
   ('Embodied intelligence','How perception, action, and feedback come together when an intelligent system interacts with the physical world.')
  ],
  'projects_kicker':'03 / PROJECTS', 'projects_title':'Ideas in practice', 'project_note':'Work in progress, with room to learn.',
  'read_project':'About this project', 'visit_academy':'Open academy', 'access':'Invitation access',
  'visit_openpension':'Open test demo', 'openpension_access':'Test assets · invitation access',
  'writing_kicker':'04 / WRITING', 'writing_title':'Working notes', 'writing_intro':'Three starting questions. Open a note to read the thinking behind it.',
  'notes':[
   ('What should an AI learning companion learn about us?',[
    'A useful learning companion might begin with what a person knows. But a longer relationship raises more interesting questions: what do they care about, how do their goals change, and when should the system revise its understanding of them?',
    'I am interested in both directions of this relationship. The learner forms a model of the AI, while the AI forms a provisional model of the learner. Neither should become fixed. A good learning relationship should leave room for correction, disagreement, and independent judgment.'
   ],'Can sustained interaction improve a learner’s ability to ask better questions and make independent judgments—not only complete more tasks?'),
   ('Evaluation before optimization',[
    'Before choosing a model, I want to be clear about the decision it is meant to improve. In AI-native RAN, that means connecting a learning problem to a system goal, a useful baseline, and the constraints under which the decision must work.',
    'My starting point is an evaluation plan: which scenarios matter, what counts as an improvement, and which failure would make the approach unsuitable? This turns an experiment into a question that can be answered, including when the answer is disappointing.'
   ],'What evidence would convince me to keep a simpler baseline instead of deploying a more complex model?'),
   ('Learning robotics, one reproducible task at a time',[
    'A small control task is a useful place to begin: issue a command, observe what happens, and repeat it. My ROS 2 and Gazebo experiments are an opportunity to understand that loop before adding more complexity.',
    'The next direction is manipulation and imitation learning. I want each step to leave a clear record of the setup, action, observation, and result. The aim is to build understanding that can travel from one experiment to the next.'
   ],'Which part of a successful simulation remains reliable when the robot, environment, or observations change?')
  ],
  'question_label':'A question to test', 'contact_kicker':'05 / CONTACT', 'contact_title':'Keep in touch',
  'contact':'I’m interested in conversations about learning systems, AI-native networks, and how people and AI can grow together.',
  'contact_pending':'Public contact details will be added here.', 'footer':'Stay curious. Keep building.', 'top':'Back to top',
  'back':'Back to projects', 'next_label':'The next question', 'back_home':'Return to the homepage'
 },
 'zh': {
  'lang':'zh-CN', 'name':'何骏', 'opening':'探索过去无法触及的<em>未知</em>', 'caption':'一份持续生长的个人笔记', 'nav':['关于','兴趣','项目','笔记','联系'],
  'skip':'跳到正文', 'hero_label':'关于智能、学习与可能性的笔记',
  'subtitle':'探索智能、学习，以及我们能够共同创造的可能。', 'explore':'看看正在做的项目',
  'about_kicker':'01 / 关于', 'about_title':'关于我',
  'about':[
   '我的背景是无线通信与产品管理。目前，我关注智能系统如何学习、适应，以及如何与人建立长期协作关系。',
   '我的探索连接着 AI 原生无线网络、个人学习系统和机器人。通过 Aethervale Academy 和动手实验，我希望理解：如何把想法变成有用的系统，以及构建这些系统的过程，又如何改变我们的学习和思考。'
  ],
  'trail':['无线通信','智能系统','在构建中学习'],
  'interests_kicker':'02 / 兴趣', 'interests_title':'让我保持好奇的问题',
  'interests':[
   ('人与 AI 的共同发展','人与 AI 如何理解彼此、共同适应，并通过持续交互不断学习。'),
   ('从经验中学习','智能系统如何将经验转化为知识、更好的决策和新的能力。'),
   ('AI 原生无线网络','如何用学习方法改进无线资源管理，并使效果可测量、系统可靠、方案可落地。'),
   ('具身智能','智能系统与物理世界交互时，感知、行动和反馈如何共同发挥作用。')
  ],
  'projects_kicker':'03 / 项目', 'projects_title':'把想法付诸实践', 'project_note':'持续探索，也为新的理解留出空间。',
  'read_project':'了解这个项目', 'visit_academy':'打开学院', 'access':'需获得访问授权',
  'visit_openpension':'打开测试演示', 'openpension_access':'仅测试资产 · 需获得访问授权',
  'writing_kicker':'04 / 笔记', 'writing_title':'探索中的笔记', 'writing_intro':'从三个问题开始。展开笔记，看看问题背后的思考。',
  'notes':[
   ('AI 学习伙伴应该了解我们的什么？',[
    '一个有用的学习伙伴，也许会先了解一个人掌握了哪些知识。但长期关系会带来更有意思的问题：这个人在乎什么？目标如何变化？系统又应该在什么时候修正自己对他的理解？',
    '我关心这种关系的两个方向。学习者会形成对 AI 的认识，AI 也会形成对学习者的暂时理解。双方的认识都需要允许更新。一段好的学习关系，应当为纠正、分歧和独立判断保留空间。'
   ],'持续交互能否帮助学习者提出更好的问题、形成更独立的判断，而不仅仅是完成更多任务？'),
   ('优化之前，先把评估做好',[
    '在选择模型之前，我希望先弄清楚：它要改善的究竟是哪一个决策？对于 AI 原生无线网络，这意味着把学习问题与系统目标、可用的基线，以及决策必须满足的约束联系起来。',
    '我的起点是一份评估计划：哪些场景重要？什么算真正的改善？哪一种失败会让方案不再适合使用？这样，一次实验才成为一个可以回答的问题，即使答案并不令人满意。'
   ],'什么样的证据，会让我选择保留简单的基线，而不是部署更复杂的模型？'),
   ('从一个可复现的小任务开始学习机器人',[
    '一个小的控制任务，就是很好的起点：发出指令，观察结果，再重复一次。ROS 2 和 Gazebo 的实验让我有机会在增加复杂度之前，先理解这个反馈循环。',
    '下一阶段，我想逐步进入机器人操控与模仿学习。我希望每一步都留下清楚的记录：环境设置、采取的动作、观察到的现象，以及最终结果。目标是建立能够从一个实验带到下一个实验的理解。'
   ],'当机器人、环境或观测发生变化时，一次成功仿真中的哪些部分仍然可靠？')
  ],
  'question_label':'一个值得验证的问题', 'contact_kicker':'05 / 联系', 'contact_title':'保持交流',
  'contact':'期待交流学习系统、AI 原生无线网络，以及人与 AI 如何共同成长。',
  'contact_pending':'公开联系方式将补充在这里。', 'footer':'保持好奇，持续探索。', 'top':'回到顶部',
  'back':'返回项目列表', 'next_label':'下一个问题', 'back_home':'返回个人主页'
 }
}

PROJECTS = [
 {
  'slug':'aethervale', 'en':{
   'title':'Aethervale Academy','status':'Ongoing exploration',
   'description':'An exploration of AI-supported personal learning. I am developing ideas and experiences around adaptive learning, thoughtful evaluation, and long-term interaction between a learner and an AI companion.',
   'sections':[
    ('The question','What could a personal university look like when learning begins with a person’s own questions, goals, and experience? Aethervale Academy is my place to explore that question through a developing learning experience.'),
    ('What I am exploring',[
     'Learning journeys that begin with a real question and lead to something a learner can explain, use, or build.',
     'Evaluation that makes progress visible and helps identify what to work on next.',
     'An AI companion that can revise its understanding of a learner over time, while the learner also develops an understanding of the AI.'
    ]),
    ('Where it stands','A working demo exists and continues to evolve. It is an exploration of learning experiences and system design. Access to the current academy is invitation-based.')
   ],
   'question':'How can a learning system help people become more capable and more independent as their relationship with AI deepens?'
  },
  'zh':{
   'title':'Aethervale Academy','status':'持续探索',
   'description':'探索 AI 支持的个人学习。我正在围绕自适应学习、学习评估，以及学习者与 AI 伙伴的长期交互，逐步构建想法和学习体验。',
   'sections':[
    ('从一个问题开始','当学习从一个人自己的问题、目标与经验出发时，个人大学会是什么样子？Aethervale Academy 是我通过逐步构建学习体验，探索这个问题的地方。'),
    ('正在探索',[
     '从真实问题出发，让学习最终落在能够解释、使用或构建的成果上。',
     '让评估帮助学习者看清进步，并找到下一步值得投入的方向。',
     '让 AI 伙伴持续修正对学习者的理解，同时让学习者逐渐形成对 AI 的认识。'
    ]),
    ('目前的状态','项目已有可以体验的 Demo，并在持续演进中。我正在探索学习体验与系统设计。当前学院的访问需要授权。')
   ],
   'question':'随着人与 AI 的关系不断深入，学习系统如何帮助人获得更强的能力与更独立的判断？'
  }
 },
 {
  'slug':'openpension', 'en':{
   'title':'OpenPension','status':'Protocol prototype',
   'description':'Exploring decentralized pension design through a test-token prototype, with personal accumulation accounts and a longevity-sharing pool. The focus is on explicit rules, reproducible validation, and consistent implementations.',
   'sections':[
    ('The idea','OpenPension explores how pension rules can be made explicit and independently verifiable. The prototype connects a personal accumulation phase with a later longevity-sharing pool, using test assets to study the behavior of the rules.'),
    ('What I am working to make explicit',[
     'How contributions, account balances, and the transition between phases are calculated.',
     'How distributions from the longevity-sharing pool follow the stated rules.',
     'How independent Python, Solidity, and TypeScript implementations can be checked against the same specification.'
    ]),
    ('The current demo','The linked site is a private test client using test assets. Access requires authorization, and its connected test backend may need to be started separately. This is a prototype for studying and validating the design, not a live pension service.')
   ],
   'question':'Can independent implementations apply the same rules to the same inputs and produce exactly the same results?'
  },
  'zh':{
   'title':'OpenPension','status':'协议原型',
   'description':'通过测试代币原型探索去中心化养老金设计，连接个人积累账户与长寿共担池。重点是清晰的规则、可复现的验证，以及不同实现之间的一致性。',
   'sections':[
    ('项目想探索什么','OpenPension 探索如何把养老金规则明确表达出来，并让不同的人或程序能够独立验证。原型把个人积累阶段与后续的长寿共担池连接起来，使用测试资产研究这些规则的运行方式。'),
    ('正在明确与验证的内容',[
     '缴费、账户余额与阶段转换如何计算。',
     '长寿共担池的分配如何遵循已经写明的规则。',
     '如何依据同一份规格，检查 Python、Solidity 和 TypeScript 独立实现的一致性。'
    ]),
    ('当前演示','链接指向使用测试资产的私有测试客户端，需要获得访问授权，所连接的测试后台可能需要单独启动。这是用于研究与验证设计的原型，尚非实际运营的养老金服务。')
   ],
   'question':'不同的独立实现，能否依据相同规则，对相同输入给出完全一致的结果？'
  }
 },
 {
  'slug':'ai-native-ran', 'en':{
   'title':'AI-native RAN','status':'Research & experiments',
   'description':'Exploring learning-based approaches to radio resource management, including scheduling and link adaptation. My focus is on clear problem definitions, meaningful evaluation, and the path from a promising model to a useful system.',
   'sections':[
    ('From product questions to learning problems','My background in wireless communications has shaped how I approach AI: begin with a concrete decision, understand the constraints, and define what a useful improvement would mean at the system level.'),
    ('Areas of interest',[
     'Learning-based scheduling and link adaptation in radio access networks.',
     'Using network observations and logs to develop useful representations and predictions.',
     'Evaluation that connects model behavior with practical radio resource management goals.'
    ]),
    ('How I want to work','I am organizing this direction around small experiments with clear baselines. Each experiment should state its assumptions, test a specific decision, and make limitations visible. The emphasis is on understanding what is worth building and why.')
   ],
   'question':'When does a learned decision improve the whole system enough to justify its additional complexity?'
  },
  'zh':{
   'title':'AI-native RAN','status':'研究与实验',
   'description':'探索无线资源管理中的学习方法，包括调度与链路自适应。重点是清晰定义问题、建立有意义的评估，以及理解一个有潜力的模型如何成为有用的系统。',
   'sections':[
    ('从产品问题到学习问题','无线通信领域的经历影响了我理解 AI 的方式：从一个具体决策出发，理解约束，并定义什么样的改善能够在系统层面产生价值。'),
    ('关注的方向',[
     '无线接入网络中基于学习的调度与链路自适应。',
     '利用网络观测和日志，构建有用的表示与预测。',
     '把模型行为与实际无线资源管理目标联系起来的评估。'
    ]),
    ('希望采用的实践方式','我希望围绕具有清晰基线的小实验来推进这一方向。每个实验都应说明假设，验证具体决策，并呈现局限。重点是理解什么值得构建，以及为什么。')
   ],
   'question':'一个学习得到的决策，何时能为整个系统带来足够的改善，值得为它承担额外的复杂度？'
  }
 },
 {
  'slug':'robotics', 'en':{
   'title':'Robotics Learning Lab','status':'Learning in practice',
   'description':'Learning robotics through ROS 2 and Gazebo experiments, starting with simulation and basic control. The next direction is robotic manipulation and imitation learning, with LeRobot SO-101 as a possible learning platform.',
   'sections':[
    ('Understanding through small experiments','I am learning robotics by building up from simple, observable tasks. My current practice uses ROS 2 Jazzy and Gazebo to connect commands, simulated motion, and feedback.'),
    ('Practice so far',[
     'Setting up ROS 2 communication and running basic publisher–subscriber examples.',
     'Exploring Gazebo simulations and sending velocity commands to a simulated vehicle.',
     'Writing a simple command sequence to move forward, turn, and stop.'
    ]),
    ('The next direction','I want to progress toward robotic manipulation and imitation learning, potentially using LeRobot SO-101. This is a learning direction I plan to explore, with reproducible experiments as the foundation.')
   ],
   'question':'How can I carry what I learn in simulation into increasingly realistic perception and control tasks?'
  },
  'zh':{
   'title':'机器人学习实验','status':'实践学习',
   'description':'通过 ROS 2 与 Gazebo 实验学习机器人，从仿真和基础控制开始。下一阶段关注机器人操控与模仿学习，并考虑将 LeRobot SO-101 作为学习平台。',
   'sections':[
    ('通过小实验建立理解','我正在从简单、可观察的任务开始学习机器人。目前使用 ROS 2 Jazzy 与 Gazebo，把指令、仿真中的运动和反馈联系起来。'),
    ('已经开始的实践',[
     '搭建 ROS 2 通信环境，运行基础的发布与订阅示例。',
     '探索 Gazebo 仿真，并向仿真车辆发送速度指令。',
     '编写简单的指令序列，让车辆前进、转向和停止。'
    ]),
    ('下一阶段','我希望逐步进入机器人操控与模仿学习，并考虑使用 LeRobot SO-101。这是计划继续探索的学习方向，基础是清晰、可复现的小实验。')
   ],
   'question':'如何把在仿真中获得的理解，逐步带入更接近现实的感知与控制任务？'
  }
 }
]

def head(lang, title, prefix, alternate, description):
    c=CONTENT[lang]
    return f'''<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(description, quote=True)}">
<meta name="theme-color" content="#fbfaf7">
<title>{esc(title)}</title>
<link rel="stylesheet" href="{prefix}style.css">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{'zh-CN' if lang=='en' else 'en'}" href="{alternate}">
</head>
<body id="top">
<a class="skip" href="#main">{c['skip']}</a>'''

def header(lang, home, alternate):
    c=CONTENT[lang]
    links=''.join(f'<a href="{home}#{anchor}">{name}</a>' for anchor,name in zip(['about','interests','projects','writing','contact'],c['nav']))
    language='中文 <span>↗</span>' if lang=='en' else 'English <span>↗</span>'
    return f'''<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="{home or '#top'}" aria-label="{c['name']} — {'homepage' if lang=='en' else '个人主页'}"><span class="brand-name">{c['name']}<span style="color:var(--green)">{'.' if lang=='en' else ''}</span></span><span class="brand-caption">{c['caption']}</span></a>
<div class="header-links"><nav class="main-nav" aria-label="{'Main navigation' if lang=='en' else '主导航'}">{links}</nav><a class="language" href="{alternate}" lang="{'zh-CN' if lang=='en' else 'en'}" hreflang="{'zh-CN' if lang=='en' else 'en'}">{language}</a></div>
</div></header>'''

def footer(lang):
    c=CONTENT[lang]
    return f'''<footer class="wrap site-footer"><span>© 2026 {c['name']}</span><span class="footer-motto">{c['footer']}</span><a href="#top">{c['top']} ↑</a></footer></body></html>'''

def section_start(anchor, kicker, title, note=''):
    note_html=f'<p class="section-note">{note}</p>' if note else ''
    return f'<section class="section" id="{anchor}" aria-labelledby="{anchor}-title"><div class="section-head"><p class="section-kicker">{kicker}</p><h2 class="section-title" id="{anchor}-title">{title}</h2>{note_html}</div><div class="section-body">'

def write_home(lang):
    c=CONTENT[lang]
    prefix='' if lang=='en' else '../'
    alternate='zh/index.html' if lang=='en' else '../index.html'
    out=DIST/'index.html' if lang=='en' else DIST/'zh'/'index.html'
    description='Jun He — exploring intelligence, learning systems, AI-native radio networks, robotics, and OpenPension.' if lang=='en' else '何骏的个人主页：探索智能、学习系统、AI 原生无线网络、机器人与 OpenPension。'
    h=head(lang, 'Jun He — Into the Unknown' if lang=='en' else '何骏 — 探索未知',prefix,alternate,description)+header(lang,'',alternate)
    h+=f'''<main class="wrap" id="main">
<section class="hero" aria-labelledby="opening"><p class="eyebrow">{c['hero_label']}</p>
<h1 class="opening-line" id="opening" lang="{c['lang']}">{c['opening']}</h1>
<div class="hero-bottom"><p class="hero-subtitle">{c['subtitle']}</p><a class="text-link" href="#projects">{c['explore']} <span class="arrow" aria-hidden="true">↘</span></a></div></section>'''
    h+=section_start('about',c['about_kicker'],c['about_title'])
    h+='<div class="about-copy">'+''.join(f'<p class="{"lead" if i==0 else ""}">{p}</p>' for i,p in enumerate(c['about']))+'</div>'
    h+='<div class="topic-trail">'+''.join(f'<span>{t}</span>' for t in c['trail'])+'</div></div></section>'
    h+=section_start('interests',c['interests_kicker'],c['interests_title'])+'<div class="interests-grid">'
    for i,(title,body) in enumerate(c['interests'],1):
        h+=f'<div class="interest"><span class="interest-num" aria-hidden="true">0{i}</span><h3 class="interest-heading">{title}</h3><p>{body}</p></div>'
    h+='</div></div></section>'
    h+=section_start('projects',c['projects_kicker'],c['projects_title'],c['project_note'])+'<div class="projects-list">'
    for p in PROJECTS:
        d=p[lang]; url=f"projects/{p['slug']}.html"
        extra=f'<a href="{ACADEMY}" target="_blank" rel="noopener noreferrer">{c["visit_academy"]} ↗</a><span class="access-note">{c["access"]}</span>' if p['slug']=='aethervale' else ''
        if p['slug']=='openpension':
            extra=f'<a href="{OPENPENSION}" target="_blank" rel="noopener noreferrer">{c["visit_openpension"]} ↗</a><span class="access-note">{c["openpension_access"]}</span>'
        h+=f'''<article class="project"><div class="project-top"><h3><a class="project-title" href="{url}">{d['title']}</a></h3><span class="project-status">{d['status']}</span></div><p>{d['description']}</p><div class="project-bottom"><a href="{url}">{c['read_project']} <span aria-hidden="true">↗</span></a>{extra}</div></article>'''
    h+='</div></div></section>'
    h+=section_start('writing',c['writing_kicker'],c['writing_title'])+f'<p class="notes-intro">{c["writing_intro"]}</p>'
    for i,(title,paragraphs,question) in enumerate(c['notes'],1):
        h+=f'<details class="note" id="note-{i}"><summary><span class="note-number" aria-hidden="true">0{i}</span><span class="note-title">{title}</span><span class="note-toggle" aria-hidden="true"></span></summary><div class="note-body">'+''.join(f'<p>{p}</p>' for p in paragraphs)+f'<div class="question"><strong>{c["question_label"]}</strong>{question}</div></div></details>'
    h+='</div></section>'
    h+=section_start('contact',c['contact_kicker'],c['contact_title'])+f'<p class="contact-copy">{c["contact"]}</p><p class="contact-pending">{c["contact_pending"]}</p></div></section></main>'+footer(lang)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(h,encoding='utf-8')

def write_project(lang,project):
    c=CONTENT[lang];d=project[lang];slug=project['slug']
    prefix='../' if lang=='en' else '../../'
    alternate=f'../zh/projects/{slug}.html' if lang=='en' else f'../../projects/{slug}.html'
    out=DIST/'projects'/f'{slug}.html' if lang=='en' else DIST/'zh'/'projects'/f'{slug}.html'
    h=head(lang,d['title']+' — '+c['name'],prefix,alternate,d['description'])+header(lang,'../index.html',alternate)
    h+=f'''<main class="wrap" id="main"><article class="project-page"><a class="back-link" href="../index.html#projects">← {c['back']}</a><p class="article-meta">{d['status']}</p><h1 class="article-title">{d['title']}</h1><p class="article-deck">{d['description']}</p>'''
    for title,body in d['sections']:
        h+=f'<section class="article-section"><h2>{title}</h2>'
        h+=('<ul>'+''.join(f'<li>{x}</li>' for x in body)+'</ul>') if isinstance(body,list) else f'<p>{body}</p>'
        h+='</section>'
    h+=f'<aside class="article-next"><div class="small-label">{c["next_label"]}</div><p>{d["question"]}</p></aside><div class="article-actions">'
    if slug=='aethervale':
        h+=f'<a class="text-link" href="{ACADEMY}" target="_blank" rel="noopener noreferrer">{c["visit_academy"]} ↗</a><span class="access-note">{c["access"]}</span>'
    elif slug=='openpension':
        h+=f'<a class="text-link" href="{OPENPENSION}" target="_blank" rel="noopener noreferrer">{c["visit_openpension"]} ↗</a><span class="access-note">{c["openpension_access"]}</span>'
    h+=f'<a class="text-link" href="../index.html#projects">{c["back_home"]} <span aria-hidden="true">↗</span></a></div></article></main>'+footer(lang)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(h,encoding='utf-8')

for language in CONTENT:
    write_home(language)
    for project in PROJECTS:write_project(language,project)
(DIST/'.nojekyll').write_text('')
print(f'Rendered {len(CONTENT) * (1 + len(PROJECTS))} HTML pages in dist/. No runtime dependencies.')
