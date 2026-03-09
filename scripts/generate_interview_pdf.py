
import pypdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

def create_interview_prep_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom Styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.darkblue,
        spaceAfter=20,
        alignment=1 # Center
    )
    
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.darkblue,
        spaceBefore=15,
        spaceAfter=10
    )

    sub_header_style = ParagraphStyle(
        'SubHeader',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.black,
        spaceBefore=10,
        spaceAfter=2
    )

    normal_style = styles['Normal']
    normal_style.fontSize = 10
    normal_style.leading = 12

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=normal_style,
        leftIndent=20,
        bulletIndent=10
    )

    # --- TITLE PAGE ---
    story.append(Paragraph("XYLEM INTERVIEW PREPARATION GUIDE", title_style))
    story.append(Paragraph("Project Manager – Digital Solutions", styles['Heading2']))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Candidate:</b> Jaouher ROMDHANE", normal_style))
    story.append(Paragraph("<b>Profile:</b> Senior R&D Engineer | PMP® Certified | Digital Expert", normal_style))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("<b>STRATEGY: THE 'PERFECT MATCH'</b>", header_style))
    story.append(Paragraph("This guide is expanded to cover every angle: Technical, Managerial (PMP), and Behavioral.", normal_style))
    story.append(Paragraph("• <b>15 General Q&A</b> to show leadership and soft skills.", bullet_style))
    story.append(Paragraph("• <b>30 PMP Q&A</b> to impress the certified manager with PMBOK terminology.", bullet_style))
    story.append(Paragraph("• <b>8 Detailed Stories</b> covering your full career path.", bullet_style))
    story.append(Paragraph("• <b>6 Strategic Questions</b> to ask at the end.", bullet_style))
    
    story.append(PageBreak())

    # --- PHASE 1: THE PITCH ---
    story.append(Paragraph("PHASE 1: THE PITCH (2 Minutes)", header_style))
    story.append(Paragraph("<i>Goal: Clear, confident, and structured.</i>", normal_style))
    story.append(Spacer(1, 10))

    pitch_text = """
    "Hello, I am Jaouher. I am a <b>Senior Project Manager</b> and <b>R&D Engineer</b> with <b>10 years of experience</b>. I hold a <b>PhD in Energy & Process Engineering</b>, a <b>Generalist Engineering Degree</b>, and a <b>Master's in Transport Systems</b>.<br/><br/>
    
    I have a dual profile tailored for this role: I am <b>PMP certified</b> for management, and I am a <b>Technical Expert</b> in both Industrial Hardware and Digital Solutions.<br/><br/>
    
    I bring <b>3 key assets</b> to Xylem:<br/>
    
    1. <b>I know your Industry:</b> At <b>PSG-Dover</b>, I worked on the <b>design and optimization of pumps, compressors, and hydraulic systems</b>. I understand the physics of water and the constraints of your equipment.<br/>
    
    2. <b>I know Digital:</b> At <b>Schneider Electric</b>, I <b>piloted the development</b> of a <b>Predictive Maintenance tool</b> specifically for the <b>Wastewater sector</b>. We leveraged <b>real-time field data</b>, combining <b>Physical Laws</b> with <b>Machine Learning</b> to accurately model and predict equipment behavior.<br/>
    
    3. <b>I deliver results:</b> I am <b>PMP Certified</b>, which gives me a strong methodological framework. I use this structured mindset to <b>bridge the gap</b> between Data Scientists and Field Engineers, ensuring projects are delivered on time and on budget.<br/><br/>
    
    I want to join Xylem because you are the leader in <b>Smart Water</b>, and I want to use my skills to solve critical water challenges."
    """
    story.append(Paragraph(pitch_text, normal_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>🧠 MEMORY AID (Keywords):</b>", sub_header_style))
    story.append(Paragraph("1. <b>10 Years / PhD (Energy) / PMP</b>", bullet_style))
    story.append(Paragraph("2. <b>Hardware</b> (PSG-Dover: Design/Optimization)", bullet_style))
    story.append(Paragraph("3. <b>Digital</b> (Schneider: Field Data + Physics + AI)", bullet_style))
    story.append(Paragraph("4. <b>Management</b> (PMP Framework + Bridging Gaps)", bullet_style))

    story.append(PageBreak())

    # --- PHASE 2: EXPERIENCE STORIES ---
    story.append(Paragraph("PHASE 2: KEY EXPERIENCE STORIES (STAR Method)", header_style))
    story.append(Paragraph("<i>Selected stories optimized for oral delivery. Focus on the 'Say this' hook.</i>", normal_style))

    stories = [
        ("1. Schneider Electric (The 'Hands-On Manager' Match)", 
         "<b>Situation:</b> Leading R&D projects requiring both advanced physics and modern data science.<br/>"
         "<b>Action:</b> I held a dual role: <b>Project Manager</b> and <b>Lead Developer</b>. I personally developed the <b>Machine Learning</b> and <b>MBD models</b>, while also managing the Agile roadmap and the <b>DevOps</b> pipeline.<br/>"
         "<b>Result:</b> Delivered a complex technical solution on time by understanding the code from the inside out.<br/>"
         "<b>🗣️ Say this:</b> 'At Schneider, I wore two hats. As the Project Manager, I led the Agile ceremonies and roadmap. But I was also the Lead Developer. I personally coded the Machine Learning algorithms and the Model-Based Designs (MBD). This combination is powerful: I didn't just ask for features; I built them. This allowed me to make realistic technical decisions while keeping the project on track.'"),
        
        ("2. Triskell Consulting (The 'DevOps' Match)", 
         "<b>Situation:</b> Complex multi-physics systems needed faster iteration cycles.<br/>"
         "<b>Action:</b> I implemented a full <b>DevOps</b> approach. I used <b>Docker</b> and <b>Kubernetes</b> to containerize applications and set up <b>CI/CD pipelines</b> for automated testing and deployment.<br/>"
         "<b>Result:</b> Drastically reduced deployment time and improved reliability.<br/>"
         "<b>🗣️ Say this:</b> 'At Triskell, the engineering team was slowed down by manual deployments. I introduced a modern DevOps culture. I containerized our simulation tools using Docker and Kubernetes, and built automated CI/CD pipelines. This moved us from 'it works on my machine' to a standardized, industrial software factory, drastically reducing our time-to-market.'"),

        ("3. Carmat (The 'Critical Data' Match)", 
         "<b>Situation:</b> Developing the data infrastructure for an artificial heart (Life-Critical).<br/>"
         "<b>Action:</b> I designed complex <b>Data Pipelines</b> and developed dynamic <b>Dashboards (Power BI, Tableau)</b> for real-time monitoring. I managed this in an <b>Agile</b> environment with strict quality constraints.<br/>"
         "<b>Result:</b> Reliable data visualization for critical decision-making.<br/>"
         "<b>🗣️ Say this:</b> 'At Carmat, I worked on the data infrastructure for an artificial heart. In that environment, a data error isn't just a bug; it's a life-critical failure. I designed robust data pipelines and real-time dashboards using Power BI and Tableau. I bring this same 'Zero-Defect' mindset to Xylem: I ensure that the data driving your Smart Water solutions is 100% reliable.'"),
        
        ("4. PSG-Dover (The 'Industrial Asset' Match)", 
         "<b>Situation:</b> Optimizing industrial pumps and hydraulic systems.<br/>"
         "<b>Action:</b> I performed <b>Model-Based Design</b> and advanced simulations (Thermodynamics). I also worked on <b>predictive models</b> to anticipate equipment behavior.<br/>"
         "<b>Result:</b> Deep understanding of the physical assets Xylem sells.<br/>"
         "<b>🗣️ Say this:</b> 'At PSG-Dover, I didn't just manage projects; I was hands-on with the hardware. I used Model-Based Design and thermodynamic simulations to optimize pump performance. This means when I talk to your hydraulic engineers, I speak their language. I understand the physical constraints of the equipment, which helps me build better digital solutions for them.'"),
        
        ("5. Lusac (The 'Sustainability' Match)", 
         "<b>Situation:</b> Researching energy systems, specifically around <b>Hydrogen</b> and thermodynamics.<br/>"
         "<b>Action:</b> I conducted <b>experimental validation</b> and developed predictive models to optimize energy efficiency.<br/>"
         "<b>Result:</b> Concrete experience in sustainable energy technologies.<br/>"
         "<b>🗣️ Say this:</b> 'My work at Lusac was focused on pure energy efficiency. I developed algorithms to optimize energy consumption in complex systems, including Hydrogen applications. This experience aligns perfectly with Xylem's mission. I don't just talk about sustainability; I have the technical background to actually implement energy-saving algorithms.'"),
        
        ("6. Liebherr Aerospace (The 'Validation' Match)", 
         "<b>Situation:</b> Ensuring the reliability of air systems for aerospace.<br/>"
         "<b>Action:</b> I defined <b>test scenarios</b> and performed multi-physics modeling to validate system performance against strict requirements.<br/>"
         "<b>Result:</b> Mastery of the V-Cycle and validation protocols.<br/>"
         "<b>🗣️ Say this:</b> 'In aerospace, validation is everything. At Liebherr, I was responsible for defining the test scenarios to prove that our systems met every single requirement. I bring this structured V-Cycle mindset to Xylem. I know how to ensure that what we build is exactly what was specified, with full traceability from requirement to test.'")
    ]

    for title, content in stories:
        story.append(Paragraph(title, sub_header_style))
        story.append(Paragraph(content, normal_style))
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # --- PHASE 2.5: XYLEM VUE MASTERY ---
    story.append(PageBreak())
    story.append(Paragraph("PHASE 2.5: XYLEM VUE MASTERY (Technical Focus)", header_style))
    story.append(Paragraph("<i>Demonstrate deep knowledge of their flagship solution.</i>", normal_style))

    vue_data = [
        ("1. What is Xylem Vue?", 
         "It is a <b>vendor-agnostic</b> digital platform that unifies data from any source (SCADA, GIS, IoT) into a single view. It breaks down <b>Data Silos</b> to optimize the entire water cycle."),
        ("2. Key Technology: RT-DSS", 
         "<b>Real-Time Decision Support System.</b> It uses digital twins and analytics to help operators make data-driven decisions (e.g., preventing sewer overflows)."),
        ("3. The 'Idrica' Partnership", 
         "Xylem Vue is powered by the partnership with <b>Idrica (GoAigua)</b>, combining Xylem's hardware reach with Idrica's software architecture."),
        ("4. Why it matters (The Value)", 
         "It allows utilities to use <b>existing assets</b> (no rip-and-replace). It turns raw data into operational efficiency (OpEx reduction)."),
        ("5. My 'Vue' Pitch (The Connection)", 
         "<b>🗣️ Say this:</b> 'I understand Xylem Vue's power because I've built similar systems. At Schneider, I connected <b>field data</b> (IoT) to <b>predictive models</b> (Digital Twin) to optimize assets. I speak the language of <b>Data Integration</b> and <b>Operational Efficiency</b>, which is exactly what Xylem Vue sells.'")
    ]

    for title, content in vue_data:
        story.append(Paragraph(title, sub_header_style))
        story.append(Paragraph(content, normal_style))
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # --- PHASE 3: GENERAL Q&A ---
    story.append(Paragraph("PHASE 3: GENERAL Q&A (15 Questions)", header_style))

    qa_data = [
        ("Q1: Why Xylem?", 
         "Because Xylem is transforming from a 'Pump Company' to a 'Data Company'. I have the perfect profile: I know the <b>machines</b> (Pumps) and the <b>data</b> (AI)."),
        ("Q2: How do you manage a project? (Methodology)", 
         "I use a <b>Hybrid approach</b>. <b>PMP</b> for structure (Planning, Risk) and <b>Agile/Scrum</b> for execution (Speed, Adaptability)."),
        ("Q3: How do you handle a difficult stakeholder?", 
         "I use <b>Data</b>. I listen, I show the impact on <b>Budget/Timeline</b>, and I propose options. Data removes emotion from the decision."),
        ("Q4: What is your biggest weakness?", 
         "I am demanding on technical quality. I learned that 'Done is better than Perfect'. I now focus on <b>Business Value</b> and deadlines."),
        ("Q5: Describe your leadership style.", 
         "<b>Servant Leadership</b>. My job is to remove obstacles for my team so they can perform. I protect them from external noise."),
        ("Q6: How do you handle stress/pressure?", 
         "I stay calm and organized. I break down the big problem into small tasks (WBS) and focus on the immediate next step."),
        ("Q7: Why are you leaving your current role?", 
         "I have delivered the key projects at Schneider. I am looking for a new challenge where I can apply my skills to <b>Sustainability</b> and Water, which is a passion."),
        ("Q8: Give an example of innovation.", 
         "At Schneider, we didn't just monitor pumps; we used AI to predict failures 2 weeks in advance. That changed the business model from reactive to proactive."),
        ("Q9: How do you prioritize tasks?", 
         "I use the <b>Eisenhower Matrix</b> (Urgent vs Important). I focus on what delivers the most value to the customer (MVP approach)."),
        ("Q10: How do you handle scope creep?", 
         "I refer to the <b>Project Charter</b>. If it's new, it goes through the <b>Change Control Process</b>. Nothing is free."),
        ("Q11: How do you work with remote teams?", 
         "Over-communication and clear documentation. I use tools like JIRA and Teams, and I ensure we have regular syncs to build trust."),
        ("Q12: What makes you unique?", 
         "My dual background. Most PMs don't know Python/AI. Most Engineers don't know PMP. I have both."),
        ("Q13: Tell me about a failure.", 
         "Once, I underestimated a data integration task. It delayed us. I learned to always do a 'Proof of Concept' before committing to a timeline."),
        ("Q14: How do you motivate your team?", 
         "By giving them <b>Purpose</b>. I explain 'Why' we are doing this (e.g., saving water), not just 'What' to do."),
        ("Q15: Salary expectations?", 
         "I am looking for a fair market rate for a Senior PM with PMP and Niche Technical skills. I am open to discussing the full package.")
    ]

    for q, a in qa_data:
        story.append(Paragraph(f"<b>{q}</b>", sub_header_style))
        story.append(Paragraph(a, normal_style))

    story.append(PageBreak())

    # --- PHASE 4: PMP DEEP DIVE ---
    story.append(Paragraph("PHASE 4: PMP SPECIAL Q&A (30 Questions)", header_style))
    story.append(Paragraph("<i>Impress the PMP manager with PMBOK terminology.</i>", normal_style))

    pmp_qa_data = [
        ("1. How do you start a project?", "I create a <b>Project Charter</b> authorized by the Sponsor to define high-level scope and authority."),
        ("2. How do you identify stakeholders?", "I use a <b>Stakeholder Register</b> and analyze them using a Power/Interest Grid."),
        ("3. How do you collect requirements?", "I use interviews, workshops, and <b>Prototypes</b>. I document them in a Requirements Traceability Matrix."),
        ("4. How do you define Scope?", "I create a <b>WBS (Work Breakdown Structure)</b>. If it's not in the WBS, it's not in the project."),
        ("5. How do you handle Scope Creep?", "I enforce the <b>Change Management Plan</b>. Any change must be approved by the <b>CCB (Change Control Board)</b>."),
        ("6. How do you define the schedule?", "I define activities, sequence them, and find the <b>Critical Path</b>. That determines the project duration."),
        ("7. How do you estimate duration?", "I use <b>Bottom-Up</b> for accuracy or <b>Three-Point Estimating</b> (PERT) for uncertainty."),
        ("8. What if the project is late?", "I analyze the Critical Path. I can <b>Crash</b> (add resources) or <b>Fast Track</b> (parallel tasks)."),
        ("9. How do you estimate costs?", "I sum up activity costs to get the <b>Cost Baseline</b>, then add Management Reserves for the Total Budget."),
        ("10. How do you track performance?", "I use <b>EVM (Earned Value Management)</b>. I watch CPI (Cost) and SPI (Schedule)."),
        ("11. What is CPI?", "Cost Performance Index. If CPI < 1, we are over budget. I investigate root causes immediately."),
        ("12. How do you ensure Quality?", "<b>Quality Assurance</b> manages the process (prevention). <b>Quality Control</b> checks the product (inspection)."),
        ("13. How do you improve processes?", "I use <b>Retrospectives</b> (Agile) or Lessons Learned sessions to implement continuous improvement."),
        ("14. How do you acquire resources?", "I negotiate with functional managers. I use a <b>RACI Matrix</b> to define roles clearly."),
        ("15. How do you develop the team?", "I guide them through the <b>Tuckman Ladder</b>: Forming, Storming, Norming, Performing."),
        ("16. How do you manage conflict?", "I prefer <b>Collaborate/Problem Solve</b>. If needed, I use Compromise. I avoid Smoothing or Forcing."),
        ("17. How do you plan communications?", "I create a <b>Communications Management Plan</b>. Right info, to the right person, at the right time."),
        ("18. How do you identify risks?", "Brainstorming, SWOT analysis, and checking Lessons Learned. I create a <b>Risk Register</b>."),
        ("19. How do you analyze risks?", "Qualitative analysis (Probability x Impact) to prioritize. Quantitative (Monte Carlo) for big projects."),
        ("20. How do you respond to risks?", "For threats: <b>Avoid, Mitigate, Transfer, Accept</b>. For opportunities: Exploit, Share, Enhance, Accept."),
        ("21. What is a Secondary Risk?", "A risk that arises as a direct result of implementing a risk response."),
        ("22. How do you manage procurement?", "I define the SOW (Statement of Work). I choose Fixed Price (low risk for us) or T&M (flexibility)."),
        ("23. How do you select vendors?", "I use Source Selection Criteria (Price, Technical ability, Management approach)."),
        ("24. How do you manage stakeholders?", "I monitor their engagement levels (Unaware to Leading) and use strategies to keep them supportive."),
        ("25. What is Integration Management?", "It's my main job. Balancing all knowledge areas and making trade-offs between constraints."),
        ("26. How do you close a project?", "Obtain formal acceptance, transfer the product, document Lessons Learned, release team."),
        ("27. What is the difference between Issue and Risk?", "A Risk is uncertain (future). An Issue is happening now (present)."),
        ("28. How do you handle a Change Request?", "Analyze impact -> Identify options -> Submit to CCB -> Update plans if approved."),
        ("29. What is Rolling Wave Planning?", "Planning in detail for the near term and at a high level for the long term."),
        ("30. Why is the Project Charter important?", "It formally authorizes the project and gives the Project Manager authority to use resources.")
    ]

    for q, a in pmp_qa_data:
        story.append(Paragraph(f"<b>{q}</b>", sub_header_style))
        story.append(Paragraph(a, normal_style))

    story.append(PageBreak())

    # --- PHASE 4.5: PMP APPLIED TO XYLEM RESPONSIBILITIES ---
    story.append(Paragraph("PHASE 4.5: PMP APPLIED TO JOB RESPONSIBILITIES", header_style))
    story.append(Paragraph("<i>Direct mapping of Job Offer Responsibilities to PMP Concepts.</i>", normal_style))

    pmp_responsibility_qa = [
        ("Resp: 'Develop and maintain the project management plan'", 
         "<b>Q: What is the difference between the Project Management Plan and Project Documents?</b><br/>"
         "A: The <b>Project Management Plan</b> is the approved 'How-To' guide (Baselines, Subsidiary Plans) that requires a Change Request to update. "
         "<b>Project Documents</b> (Risk Register, Issue Log) are dynamic and updated daily."),
        
        ("Resp: 'Ensure compliance with contractual obligations'", 
         "<b>Q: How do you manage a vendor who is underperforming?</b><br/>"
         "A: I refer to the contract and the <b>SLA (Service Level Agreement)</b>. I use the <b>Control Procurements</b> process: inspections, audits, and performance reviews. If needed, I issue a formal cure notice."),

        ("Resp: 'Manage changes... effectively'", 
         "<b>Q: A client asks for a small change directly to the team. What do you do?</b><br/>"
         "A: I stop it to prevent <b>Gold Plating</b>. I ask them to submit a formal request so we can analyze the impact on cost and schedule. Nothing is free."),

        ("Resp: 'Mitigate risks'", 
         "<b>Q: What is the difference between a Contingency Plan and a Workaround?</b><br/>"
         "A: A <b>Contingency Plan</b> is proactive (planned in the Risk Register for identified risks). A <b>Workaround</b> is reactive (an unplanned response to an unidentified issue)."),

        ("Resp: 'Collaborate with internal teams... and customers'", 
         "<b>Q: How do you handle a 'High Power / High Interest' stakeholder?</b><br/>"
         "A: I use the strategy <b>'Manage Closely'</b>. I involve them in decision-making and keep them fully informed to ensure their buy-in and prevent blockers."),

        ("Resp: 'Manage multiple projects simultaneously'", 
         "<b>Q: How do you handle resource contention between two of your projects?</b><br/>"
         "A: I use <b>Resource Leveling</b> (which may extend schedule) or <b>Resource Smoothing</b> (within float). If that fails, I negotiate with Functional Managers or escalate based on strategic priority."),

        ("Resp: 'Ensure... customer satisfaction'", 
         "<b>Q: How do you validate Scope?</b><br/>"
         "A: <b>Validate Scope</b> is the formal acceptance of deliverables by the customer (User Acceptance Testing). It is different from <b>Control Quality</b>, which is internal verification by the team."),

        ("Resp: 'Identify opportunities to grow the business'", 
         "<b>Q: What is a Business Case?</b><br/>"
         "A: It explains the financial justification (ROI, NPV) for the project. As a PM, I ensure the project remains aligned with the Business Case throughout its lifecycle to deliver real value."),
         
        ("Resp: 'Health and Safety standards'", 
         "<b>Q: How do you handle a safety violation on site?</b><br/>"
         "A: Safety is a non-negotiable project constraint. I stop the work immediately (if necessary), log it as an <b>Issue</b>, perform a Root Cause Analysis, and update the Risk Register.")
    ]

    for title, content in pmp_responsibility_qa:
        story.append(Paragraph(title, sub_header_style))
        story.append(Paragraph(content, normal_style))
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # --- PHASE 4.8: PMP CHEAT SHEET ---
    story.append(Paragraph("PHASE 4.8: PMP CHEAT SHEET (Must-Know Concepts)", header_style))
    story.append(Paragraph("<i>Quick definitions to keep in mind during the interview.</i>", normal_style))

    cheat_sheet = [
        ("1. The Iron Triangle (Triple Constraint)", 
         "<b>Scope, Time, Cost.</b> You cannot change one without affecting the others. Quality sits in the middle. <br/><i>Xylem Context:</i> If a client wants a new feature (Scope), it will cost money or time."),
        ("2. WBS (Work Breakdown Structure)", 
         "Decomposition of the project into smaller, manageable chunks. <br/><i>Xylem Context:</i> Shows you are organized and won't miss details in complex digital projects."),
        ("3. Critical Path", 
         "The sequence of tasks that determines the shortest project duration. Zero float. <br/><i>Xylem Context:</i> If a task on the critical path is delayed, the delivery to the client is delayed."),
        ("4. Stakeholder Power/Interest Grid", 
         "A tool to classify stakeholders. <br/><i>Xylem Context:</i> You manage the 'High Power/High Interest' (e.g., Client Sponsor) closely, and keep 'Low Power/High Interest' (e.g., End Users) informed."),
        ("5. Risk vs. Issue", 
         "<b>Risk:</b> Uncertain event (Future). Response: Mitigate/Avoid. <br/><b>Issue:</b> Event that has happened (Present). Response: Workaround/Solve. <br/><i>Xylem Context:</i> Shows you are proactive (Risk) not just reactive (Issue)."),
        ("6. CCB (Change Control Board)", 
         "The group responsible for approving or rejecting changes. <br/><i>Xylem Context:</i> You don't say 'Yes' to every client request. You follow the process to protect the margin."),
        ("7. EVM (Earned Value Management)", 
         "Measuring performance. <b>CPI</b> (Cost Efficiency) and <b>SPI</b> (Schedule Efficiency). <br/><i>Xylem Context:</i> 'We are 10% over budget' is vague. 'Our CPI is 0.9' is professional."),
        ("8. Lessons Learned", 
         "Knowledge gained during the project. <br/><i>Xylem Context:</i> Essential for 'Innovation' roles. We don't repeat the same mistakes in the next digital rollout."),
        ("9. Agile vs Waterfall (Hybrid)", 
         "<b>Waterfall:</b> Predictive, good for hardware/construction. <b>Agile:</b> Adaptive, good for software/digital. <br/><i>Xylem Context:</i> As a Digital PM, you likely use Agile for the software part and Waterfall for the physical installation."),
        ("10. MVP (Minimum Viable Product)", 
         "The version of a new product with just enough features to satisfy early customers. <br/><i>Xylem Context:</i> Don't build the full platform at once. Release a pilot to one water utility, learn, and iterate."),
        ("11. Definition of Done (DoD)", 
         "A shared understanding of what it means for work to be complete (e.g., Code written + Tested + Documented). <br/><i>Xylem Context:</i> Ensures quality. A feature isn't 'done' until it's validated on the test bench."),
        ("12. Servant Leadership", 
         "The PM serves the team, removes obstacles, and provides resources. <br/><i>Xylem Context:</i> You are not a dictator. You are an enabler for the developers and engineers."),
        ("13. Gold Plating", 
         "Giving the customer more than what was agreed upon (extra features). <br/><i>Xylem Context:</i> Avoid this! It costs money and adds risk without guaranteed value. Stick to the Scope."),
        ("14. Technical Debt", 
         "The implied cost of additional rework caused by choosing an easy solution now instead of a better approach that would take longer. <br/><i>Xylem Context:</i> Balancing speed to market vs long-term maintainability of the digital platform."),
        ("15. Sponsor vs Customer", 
         "<b>Sponsor:</b> Provides resources and support (Internal). <b>Customer:</b> Uses the product (External). <br/><i>Xylem Context:</i> Your Sponsor might be the R&D Director; your Customer is the Water Utility company.")
    ]

    for title, content in cheat_sheet:
        story.append(Paragraph(title, sub_header_style))
        story.append(Paragraph(content, normal_style))
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # --- PHASE 5: QUESTIONS TO ASK ---
    story.append(Paragraph("PHASE 5: QUESTIONS TO ASK (6 Strategic Questions)", header_style))
    story.append(Paragraph("<i>Show you are a peer, not just a candidate.</i>", normal_style))

    questions_to_ask = [
        ("1. The PMP Connection (Methodology)", 
         "I noticed you are PMP certified. How strictly do we follow formal <b>PMBOK processes</b> versus a more flexible <b>Agile approach</b> here?"),
        ("2. Strategy (Business)", 
         "With Xylem Vue, are we focusing more on selling new digital products or optimizing existing assets for clients?"),
        ("3. Team Structure (Organization)", 
         "How does the Digital Solutions team collaborate with the core Hydraulic Design teams? Are we integrated in squads?"),
        ("4. Success Metrics (Performance)", 
         "If I take this role, what is the <b>one critical milestone</b> you need this project to hit in the first 6 months?"),
        ("5. Challenges (Reality Check)", 
         "What is the biggest hurdle to digital adoption for your water utility clients right now? Legacy systems or culture?"),
        ("6. Future (Vision)", 
         "Is Xylem looking into integrating <b>GenAI</b> for operator assistance in the near future roadmap?")
    ]

    for q, a in questions_to_ask:
        story.append(Paragraph(f"<b>{q}</b>", sub_header_style))
        story.append(Paragraph(a, normal_style))
        story.append(Spacer(1, 5))

    doc.build(story)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    create_interview_prep_pdf("interview/Xylem_Interview_Prep_Ultimate_v23.pdf")
